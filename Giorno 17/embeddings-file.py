"""
mini_semantic_search.py – versione 2
OpenAI + FAISS + import PDF/DOCX
"""

from pathlib import Path
import os, re, math, numpy as np
import faiss, openai
import pdfplumber  # → PDF
from docx import Document  # → DOCX
from tqdm import tqdm  # barra di avanzamento

MODEL_NAME = "text-embedding-3-small"
CHUNK_SIZE = 400  # caratteri circa (≈ 150 token) – puoi adattare


# ---------------------------------------------------------------------------
# 1) Utilità per spezzare il testo lungo in chunk gestibili dall’API
# ---------------------------------------------------------------------------
def split_into_chunks(text: str, chunk_size: int = CHUNK_SIZE):
    # taglia su punti o newline, senza “segare” le frasi a metà
    sentences = re.split(r"(?<=[\.\?!])\s+", text.strip())
    chunks, buff = [], ""
    for s in sentences:
        if len(buff) + len(s) <= chunk_size:
            buff += " " + s
        else:
            chunks.append(buff.strip())
            buff = s
    if buff:
        chunks.append(buff.strip())
    return chunks or [""]  # evita lista vuota


# ---------------------------------------------------------------------------
# 2) Caricamento testo da file
# ---------------------------------------------------------------------------
def load_texts_from_file(path: str | Path) -> list[str]:
    path = Path(path)
    ext = path.suffix.lower()
    if ext == ".pdf":
        return read_pdf(path)
    elif ext in {".docx", ".doc"}:
        return read_docx(path)
    elif ext == ".txt":
        return read_txt(path)
    else:
        raise ValueError("Formato non supportato: usa PDF o DOCX")


def read_pdf(pdf_path: Path) -> list[str]:
    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            pages.append(page.extract_text() or "")
    text = "\n".join(pages)
    return split_into_chunks(text)


def read_docx(docx_path: Path) -> list[str]:
    doc = Document(docx_path)
    paragraphs = [p.text for p in doc.paragraphs]
    text = "\n".join(paragraphs)
    return split_into_chunks(text)


def read_txt(txt_path: Path) -> list[str]:
    with open(txt_path, "r", encoding="utf-8") as f:
        text = f.read()
    return split_into_chunks(text)


# ---------------------------------------------------------------------------
# 3) Embedding helper
# ---------------------------------------------------------------------------
def embed(texts: list[str]) -> np.ndarray:
    # 🔸 rimuove chunk vuoti o solo whitespace
    clean_texts = [t for t in texts if t and t.strip()]
    if not clean_texts:
        raise ValueError("La lista di input è vuota dopo il filtraggio.")

    embeddings = []
    BATCH = 96
    for i in tqdm(range(0, len(clean_texts), BATCH), desc="Embedding"):
        batch = clean_texts[i : i + BATCH]
        try:
            resp = openai.embeddings.create(model=MODEL_NAME, input=batch)
        except openai.BadRequestError as e:
            # stampa il batch incriminato per debug e rilancia
            print("\nBatch con problema:", batch)
            raise
        embeddings.extend(d.embedding for d in resp.data)

    X = np.array(embeddings, dtype="float32")
    faiss.normalize_L2(X)
    return X


# ---------------------------------------------------------------------------
# 4) Costruzione indice
# ---------------------------------------------------------------------------
def build_index(vectors: np.ndarray):
    index = faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors)
    return index


# ---------------------------------------------------------------------------
# 5) Ricerca
# ---------------------------------------------------------------------------
def semantic_search(index, vectors, texts, query, k=5):
    q_vec = embed([query])
    D, I = index.search(q_vec, k)
    for rank, (score, idx) in enumerate(zip(D[0], I[0]), 1):
        print(f"{rank:>2}. score={score:.3f}  → {texts[idx]}…\n")


# ---------------------------------------------------------------------------
# 6) Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import argparse, sys

    parser = argparse.ArgumentParser(
        description="Semantic search (OpenAI + FAISS) con dataset manuale o da file."
    )
    parser.add_argument("--file", help="PDF o DOCX da indicizzare")
    args = parser.parse_args()

    # Dataset di partenza ----------------------------------------------------
    if args.file:
        corpus_texts = load_texts_from_file(args.file)
        print(f"✔  Estratti {len(corpus_texts)} chunk da {args.file}")
    else:
        corpus_texts = [
            "Il Colosseo è uno degli anfiteatri romani più famosi.",
            "La pizza napoletana tradizionale prevede pomodoro San Marzano e mozzarella di bufala.",
            "La teoria della relatività ristretta fu pubblicata da Einstein nel 1905.",
            "Il Vesuvio domina il golfo di Napoli ed è un vulcano ancora attivo.",
        ]

    # Embedding + indice -----------------------------------------------------
    corpus_vecs = embed(corpus_texts)
    idx = build_index(corpus_vecs)
    print(f"✔  Indice FAISS con {idx.ntotal} vettori pronto!")

    # Loop di query ----------------------------------------------------------
    while True:
        q = input("\nDomanda (ENTER per uscire): ").strip()
        if not q:
            sys.exit()
        semantic_search(idx, corpus_vecs, corpus_texts, q, k=3)
