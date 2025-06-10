import tkinter as tk
import random
from pathlib import Path
from PIL import Image, ImageTk, ImageOps  # Pillow per ridimensionamento e specchiatura

# Costanti per l'interfaccia grafica
BAR_LENGTH = 120  # Lunghezza barra HP
BAR_HEIGHT = 15  # Altezza barra HP
ANIM_STEPS = 6  # Numero di passi dell'animazione di attacco
ANIM_PIXELS = 10  # Pixel di movimento per ogni passo dell'animazione
ANIM_DELAY = 40  # Millisecondi tra i frame dell'animazione
SPRITE_MAX = (
    96  # Dimensione massima (lato più lungo) per ogni sprite dopo il ridimensionamento
)


class Move:
    """Struttura semplice per rappresentare una mossa di un Pokémon"""

    def __init__(self, name: str, dmg_min: int, dmg_max: int):
        self.name = name  # Nome della mossa
        self.dmg_min = dmg_min  # Danno minimo
        self.dmg_max = dmg_max  # Danno massimo

    def damage(self) -> int:
        """Calcola un danno casuale nell'intervallo specificato"""
        return random.randint(self.dmg_min, self.dmg_max)


class Pokemon:
    def __init__(
        self,
        name: str,
        max_hp: int,
        moves: list["Move"],
        sprite_path: Path,
        mirror: bool = False,
    ):
        self.name = name  # Nome del Pokémon
        self.max_hp = max_hp  # HP massimi
        self.hp = max_hp  # HP correnti (inizialmente = max)
        self.moves = moves  # Lista delle mosse disponibili
        self.sprite_path = sprite_path  # Percorso del file immagine dello sprite
        self.sprite_img: tk.PhotoImage | None = (
            None  # Immagine caricata (inizialmente None)
        )
        self.mirror = mirror  # Se True, specchia l'immagine orizzontalmente

    def take_hit(self, dmg: int):
        """Riduce gli HP del danno ricevuto, minimo 0"""
        self.hp = max(self.hp - dmg, 0)

    @property
    def fainted(self) -> bool:
        """Restituisce True se il Pokémon è svenuto (HP = 0)"""
        return self.hp == 0

    def hp_text(self) -> str:
        """Restituisce una stringa con HP correnti/massimi"""
        return f"{self.hp}/{self.max_hp}"


class BattleUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Mini Pokémon Battle – v5 (correct positions & paths)")

        # ========== Canvas (campo di battaglia) ========== #
        self.canvas = tk.Canvas(
            root, width=500, height=300, bg="#d0f0ff", highlightthickness=0
        )
        self.canvas.pack()

        # ========== Configurazione Pokémon e mosse ========== #
        # Mosse di Pikachu
        pika_moves = [
            Move("Thunder Shock", 12, 18),
            Move("Quick Attack", 8, 14),
            Move("Electro Ball", 10, 20),
            Move("Iron Tail", 6, 22),
        ]
        # Mosse di Charmander
        char_moves = [
            Move("Ember", 10, 16),
            Move("Scratch", 8, 12),
            Move("Flamethrower", 14, 20),
            Move(
                "Smokescreen", 0, 0
            ),  # Nessun danno - possibili effetti di stato futuri
        ]

        # Creazione dei Pokémon giocatore e nemico
        self.player = Pokemon(
            "Pikachu",
            100,
            pika_moves,
            Path(r"Giorno 10\pikachu.png"),
            mirror=False,  # Il Pokémon del giocatore guarda normalmente
        )
        self.enemy = Pokemon(
            "Charmander",
            100,
            char_moves,
            Path(r"Giorno 10\charmender.png"),
            mirror=True,  # Il nemico è specchiato per guardare verso il giocatore
        )

        # Carica le immagini degli sprite
        self._load_sprites()

        # ========== Posizionamento sprite (Pikachu in basso-destra) ========== #
        self.player_item = self.canvas.create_image(
            355, 150, image=self.player.sprite_img, anchor="nw"
        )
        self.enemy_item = self.canvas.create_image(
            70, 40, image=self.enemy.sprite_img, anchor="nw"
        )

        # ========== Barre HP ========== #
        # Barre del nemico (in alto-sinistra)
        self.enemy_bar_bg = self.canvas.create_rectangle(
            50, 0, 50 + BAR_LENGTH, BAR_HEIGHT, outline="black"
        )
        self.enemy_bar = self.canvas.create_rectangle(
            50, 0, 50 + BAR_LENGTH, BAR_HEIGHT, fill="green", outline=""
        )
        self.enemy_hp_text = self.canvas.create_text(
            50 + BAR_LENGTH / 2, BAR_HEIGHT + 10, text=self.enemy.hp_text()
        )

        # Barre del giocatore (sopra Pikachu)
        self.player_bar_bg = self.canvas.create_rectangle(
            350, 120, 350 + BAR_LENGTH, 120 + BAR_HEIGHT, outline="black"
        )
        self.player_bar = self.canvas.create_rectangle(
            350, 120, 350 + BAR_LENGTH, 120 + BAR_HEIGHT, fill="green", outline=""
        )
        self.player_hp_text = self.canvas.create_text(
            350 + BAR_LENGTH / 2, 120 + BAR_HEIGHT + 10, text=self.player.hp_text()
        )

        # ---------- Etichetta per i messaggi ---------- #
        self.msg_var = tk.StringVar(value="A wild Charmander appeared!")
        tk.Label(root, textvariable=self.msg_var, font=("Arial", 12), pady=4).pack()

        # ---------- Pulsanti delle mosse ---------- #
        self.moves_frame = tk.Frame(root)
        self.moves_frame.pack()
        self.move_buttons: list[tk.Button] = []
        for i, mv in enumerate(self.player.moves):
            btn = tk.Button(
                self.moves_frame,
                text=mv.name,
                width=15,
                command=lambda idx=i: self.player_attack(idx),
            )
            btn.grid(row=i // 2, column=i % 2, padx=4, pady=4)  # Griglia 2x2
            self.move_buttons.append(btn)

        # Pulsante per ricominciare
        tk.Button(root, text="Restart 🔄", width=15, command=self.restart).pack(pady=4)

    # ------------------------------------------------------------------ #
    #                             Metodi di supporto                     #
    # ------------------------------------------------------------------ #
    def _load_sprites(self):
        """Carica e opzionalmente specchia gli sprite; ridimensiona il lato più lungo a SPRITE_MAX."""
        for poke in (self.player, self.enemy):
            path = poke.sprite_path
            if path.exists():  # Se il file esiste
                img = Image.open(path)
                if poke.mirror:  # Specchia se necessario
                    img = ImageOps.mirror(img)
                w, h = img.size

                # Fattore di ridimensionamento: rende Charmander più piccolo
                if poke.name == "Charmander":
                    scale = (SPRITE_MAX * 0.6) / max(w, h)  # 40% più piccolo
                else:
                    scale = SPRITE_MAX / max(w, h)

                # Ridimensiona l'immagine mantenendo le proporzioni
                img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
                poke.sprite_img = ImageTk.PhotoImage(img)
            else:
                # Crea un'immagine placeholder se il file non esiste
                ph = Image.new("RGBA", (SPRITE_MAX, SPRITE_MAX), "#cccccc")
                poke.sprite_img = ImageTk.PhotoImage(ph)
                print(f"[WARN] File sprite non trovato per {poke.name}: {path}")

    @staticmethod
    def _hp_color(ratio: float) -> str:
        """Determina il colore della barra HP in base al rapporto HP correnti/massimi"""
        if ratio > 0.5:
            return "green"  # Verde se HP > 50%
        if ratio > 0.25:
            return "orange"  # Arancione se HP tra 25% e 50%
        return "red"  # Rosso se HP < 25%

    def _update_bars(self):
        """Aggiorna le barre HP e il testo per entrambi i Pokémon"""
        for poke, bar, txt, x0, y0 in [
            (self.enemy, self.enemy_bar, self.enemy_hp_text, 50, 0),
            (self.player, self.player_bar, self.player_hp_text, 350, 120),
        ]:
            ratio = poke.hp / poke.max_hp
            # Ridimensiona la barra in base agli HP rimanenti
            self.canvas.coords(bar, x0, y0, x0 + BAR_LENGTH * ratio, y0 + BAR_HEIGHT)
            # Cambia colore in base agli HP
            self.canvas.itemconfig(bar, fill=self._hp_color(ratio))
            # Aggiorna il testo degli HP
            self.canvas.itemconfigure(txt, text=poke.hp_text())

    def _disable_moves(self):
        """Disabilita tutti i pulsanti delle mosse"""
        for b in self.move_buttons:
            b.config(state="disabled")

    def _enable_moves(self):
        """Abilita tutti i pulsanti delle mosse"""
        for b in self.move_buttons:
            b.config(state="normal")

    # ------------------------------------------------------------------ #
    #                           Loop di battaglia                         #
    # ------------------------------------------------------------------ #
    def player_attack(self, idx: int):
        """Gestisce l'attacco del giocatore"""
        if self.player.fainted or self.enemy.fainted:
            return
        move = self.player.moves[idx]
        dmg = move.damage()
        self.msg_var.set(f"{self.player.name} used {move.name}!\nDamage: {dmg}")
        self._disable_moves()  # Disabilita i pulsanti durante l'animazione
        # Avvia l'animazione di attacco (movimento verso l'alto)
        self._animate_attack(
            self.player_item, -ANIM_PIXELS, lambda: self._after_player_attack(dmg)
        )

    def _after_player_attack(self, dmg: int):
        """Chiamata dopo l'animazione dell'attacco del giocatore"""
        self.enemy.take_hit(dmg)  # Applica il danno al nemico
        self._update_bars()  # Aggiorna le barre HP
        if self.enemy.fainted:
            self._end_battle(victory=True)  # Il giocatore vince
        else:
            # Dopo 600ms, il nemico contrattacca
            self.root.after(600, self._enemy_attack)

    def _enemy_attack(self):
        """Gestisce l'attacco del nemico"""
        if self.player.fainted or self.enemy.fainted:
            return
        move = random.choice(self.enemy.moves)  # Sceglie una mossa casuale
        dmg = move.damage()
        self.msg_var.set(f"{self.enemy.name} used {move.name}!\nDamage: {dmg}")
        # Avvia l'animazione di attacco (movimento verso il basso)
        self._animate_attack(
            self.enemy_item, ANIM_PIXELS, lambda: self._after_enemy_attack(dmg)
        )

    def _after_enemy_attack(self, dmg: int):
        """Chiamata dopo l'animazione dell'attacco del nemico"""
        self.player.take_hit(dmg)  # Applica il danno al giocatore
        self._update_bars()  # Aggiorna le barre HP
        if self.player.fainted:
            self._end_battle(victory=False)  # Il giocatore perde
        else:
            self.msg_var.set("Choose your move!")
            self._enable_moves()  # Riabilita i pulsanti per il prossimo turno

    # ------------------------------------------------------------------ #
    #                           Animazioni                               #
    # ------------------------------------------------------------------ #
    def _animate_attack(self, item: int, dy: int, callback):
        """Anima il movimento di un Pokémon durante l'attacco"""

        def step(n: int):
            if n < ANIM_STEPS:
                # Muove lo sprite di dy pixel verticalmente
                self.canvas.move(item, 0, dy)
                # Programma il prossimo passo dell'animazione
                self.root.after(ANIM_DELAY, step, n + 1)
            else:
                # Riporta lo sprite alla posizione originale
                self.canvas.move(item, 0, -dy * ANIM_STEPS)
                # Esegue la callback (solitamente applica il danno)
                callback()

        step(0)  # Inizia l'animazione

    # ------------------------------------------------------------------ #
    #                          Fine / Riavvio                           #
    # ------------------------------------------------------------------ #
    def _end_battle(self, victory: bool):
        """Gestisce la fine della battaglia"""
        msg = "You win!" if victory else "You lose!"
        who = self.enemy.name if victory else self.player.name
        self.msg_var.set(f"{msg} {who} fainted!")
        self._disable_moves()  # Disabilita le mosse alla fine della battaglia

    def restart(self):
        """Riavvia la battaglia ripristinando tutto allo stato iniziale"""
        # Ripristina gli HP di entrambi i Pokémon
        self.player.hp = self.player.max_hp
        self.enemy.hp = self.enemy.max_hp
        # Aggiorna le barre HP
        self._update_bars()
        # Riposiziona gli sprite alle coordinate iniziali
        self.canvas.coords(self.player_item, 355, 150)
        self.canvas.coords(self.enemy_item, 70, 40)
        # Ripristina il messaggio iniziale
        self.msg_var.set("A wild Charmander appeared!")
        # Riabilita i pulsanti delle mosse
        self._enable_moves()


# Punto di ingresso del programma
if __name__ == "__main__":
    try:
        import PIL  # noqa: F401
    except ImportError:
        # Verifica che Pillow sia installato
        raise SystemExit("Pillow non è installato. Esegui: pip install pillow")

    # Crea la finestra principale e avvia l'interfaccia
    root = tk.Tk()
    BattleUI(root)
    root.mainloop()  # Avvia il loop degli eventi di tkinter
