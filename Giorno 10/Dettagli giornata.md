### Giorno 10
* **Teoria: Layout manager: pack, grid, place**

1. Cos'è un layout manager
2. Perché usare i layout manager in GUI
3. Introduzione al layout `.pack()`
4. Opzioni di `.pack()` – `side`, `fill`, `expand`
5. Introduzione al layout `.grid()`
6. Sistema a righe e colonne con `.grid()`
7. Opzioni di `.grid()` – `row`, `column`, `padx`, `pady`
8. Introduzione al layout `.place()`
9. Coordinate assolute con `.place()`
10. Differenze tra `.pack()`, `.grid()` e `.place()`
11. Vantaggi e svantaggi di ogni sistema
12. Quando combinare layout manager
13. Restrizioni nell’uso combinato (`pack` vs `grid`)
14. Best practice nei layout complessi
15. Approccio modulare con `Frame` e layout dedicati

* **Pratica: Organizzazione di widget in colonne e righe**

1. Creazione di un'interfaccia con `.grid()`
2. Inserimento di etichette su righe distinte
3. Allineamento di input e label nella stessa riga
4. Utilizzo di colonne multiple con `column=0`, `column=1`
5. Inserimento di pulsanti in griglia
6. Utilizzo di `sticky` per l’allineamento
7. Applicazione di `padx` e `pady`
8. Espansione del layout con `columnspan`
9. Inserimento di spazi verticali tra righe
10. Creazione di una griglia con 3 colonne
11. Inserimento di un `Frame` come cella della griglia
12. Layout complesso con sezioni logiche
13. Uso di `.place()` per elementi decorativi
14. Combinazione di `pack` e `grid` con `Frame` separati
15. Testing della responsività del layout