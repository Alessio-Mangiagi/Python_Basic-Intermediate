### Giorno 14
* **Teoria: Confezionamento dell’app: icona, file eseguibile con PyInstaller**

1. Cos’è il packaging di un’app
2. Differenze tra script e applicazione
3. Preparazione del file `.py` finale
4. Struttura del progetto completo
5. Inserimento di un’icona personalizzata
6. Formato dell’icona: `.ico`
7. Creazione dell’icona o conversione da `.png`
8. Introduzione a PyInstaller
9. Installazione di PyInstaller
10. Comando base per creare un `.exe`
11. Opzione `--onefile` e `--noconsole`
12. Gestione delle risorse esterne (icone, immagini)
13. Integrazione di file extra in PyInstaller
14. Debug di errori comuni nel build
15. Distribuzione e testing dell’eseguibile

* **Pratica: Creazione di un eseguibile standalone del progetto GUI**

1. Preparazione del file Python funzionante
2. Creazione di un’icona `.ico`
3. Posizionamento dell’icona nella cartella progetto
4. Comando `pyinstaller --onefile nomefile.py`
5. Verifica creazione cartella `dist/`
6. Aggiunta di `--icon=icona.ico`
7. Uso dell’opzione `--noconsole`
8. Inclusione di file statici nel bundle
9. Test dell’eseguibile generato
10. Distribuzione su altra macchina
11. Gestione delle dipendenze esterne
12. Firma del file per Windows (facoltativo)
13. Creazione di un file `.bat` per lanciare l’app
14. Compressione della cartella finale
15. Invio dell’app ad altri utenti per test