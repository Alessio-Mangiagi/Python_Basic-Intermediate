MSG = {
    "it": {
        "nome": "Qual'è il nome del tuo animale? ",
        "specie": "Di che specie è il tuo animale? ",
        "specie_err": "Specie non riconosciuta. Al momento puoi scegliere tra: cane, gatto, pesce, pappagallo.",
        "act": "Vuoi interagire con {nome}? (Y/N) ",
        "comand": (
            "Ecco le interazioni possibili:\n"
            "1. parla\n2. seduto\n3. terra\n4. bravo\n5. biscotto\n6. osserva\n7. vado via\n"
            "Scrivi il comando: "
        ),
        "confused": "{nome} è confuso. Non conosce quel comando.\nProva ancora.",
        "error": "Non ho capito, le risposte accettate sono Y e N.\nRiprova."
    },
    "en": {
        "nome": "What's your animal's name? ",
        "specie": "What species is your animal? ",
        "specie_err": "Species not recognized. You can choose: dog, cat, fish, parrot.",
        "act": "Do you want to interact with {nome}? (Y/N) ",
        "comand": (
            "Here are the possible interactions:\n"
            "1. speak\n2. sit\n3. down\n4. good\n5. treat\n6. look\n7. go away\n"
            "Type the command: "
        ),
        "confused": "{nome} is confused. Doesn't know that command.\nTry again.",
        "error": "I didn't understand, accepted answers are Y and N.\nTry again."
    }
}

Animal_act = {
    "General": {
        "exit": {
            "it": "Arrivederci! Grazie per aver giocato.",
            "en": "Goodbye! Thanks for playing."
        }
    },
    "Cane": {
        "parla": {
            "it": "Il cane {nome} abbaia: Bau Bau!",
            "en": "The dog {nome} barks: Woof Woof!"
        },
        "seduto": {
            "it": "Dici: 'Seduto!' Il cane {nome} si siede.",
            "en": "You say: 'Sit!' The dog {nome} sits."
        },
        "terra": {
            "it": "Dici: 'A terra!' Il cane {nome} si sdraia.",
            "en": "You say: 'Down!' The dog {nome} lies down."
        },
        "bravo": {
            "it": "Dici: 'Bravo!' Il cane {nome} scodinzola felice.",
            "en": "You say: 'Good boy!' The dog {nome} wags its tail happily."
        },
        "biscotto": {
            "it": "Dai un biscotto al cane {nome}. Lo mangia con gusto!",
            "en": "You give a biscuit to the dog {nome}. It eats it happily!"
        },
        "osserva": {
            "it": "Osservi il cane {nome}. Ti guarda in attesa di un comando.",
            "en": "You watch the dog {nome}. It looks at you waiting for a command."
        }
    },
    "Gatto": {
        "parla": {
            "it": "Il gatto {nome} dice: Miao!",
            "en": "The cat {nome} says: Meow!"
        },
        "seduto": {
            "it": "Dici: 'Seduto!' Il gatto {nome} ti ignora.",
            "en": "You say: 'Sit!' The cat {nome} ignores you."
        },
        "terra": {
            "it": "Dici: 'A terra!' Il gatto {nome} ti ignora.",
            "en": "You say: 'Down!' The cat {nome} ignores you."
        },
        "bravo": {
            "it": "Dici: 'Bravo!' Il gatto {nome} ti ignora.",
            "en": "You say: 'Good!' The cat {nome} ignores you."
        },
        "biscotto": {
            "it": "Dai un biscotto al gatto {nome}. Osserva il cibo e ci dà qualche colpetto con la zampa.",
            "en": "You give a biscuit to the cat {nome}. It looks at the food and pats it with its paw."
        },
        "osserva": {
            "it": "Osservi il gatto {nome}. Si stiracchia e comincia a leccarsi.",
            "en": "You watch the cat {nome}. It stretches and starts licking itself."
        }
    },
    "Pesce": {
        "parla": {
            "it": "Il pesce {nome} boccheggia e ti osserva.",
            "en": "The fish {nome} gasps and looks at you."
        },
        "seduto": {
            "it": "Dici: 'Seduto!' Il pesce {nome} sembra confuso.",
            "en": "You say: 'Sit!' The fish {nome} looks confused."
        },
        "terra": {
            "it": "Dici: 'A terra!' Il pesce {nome} guarda preoccupato il pavimento.",
            "en": "You say: 'Down!' The fish {nome} looks worried at the floor."
        },
        "bravo": {
            "it": "Dici: 'Bravo!' Il pesce {nome} nuota felice.",
            "en": "You say: 'Good!' The fish {nome} swims happily."
        },
        "biscotto": {
            "it": "Dai un biscotto al pesce {nome}. Si avvicina alla superficie per mangiare le briciole!",
            "en": "You give a biscuit to the fish {nome}. It comes to the surface to eat the crumbs!"
        },
        "osserva": {
            "it": "Osservi il pesce {nome}. Nuota nel suo acquario.",
            "en": "You watch the fish {nome}. It swims in its aquarium."
        }
    },
    "Pappagallo": {
        "parla": {
            "it": "Il pappagallo {nome} dice: 'Ciao WRAAA!'",
            "en": "The parrot {nome} says: 'Hello WRAAA!'"
        },
        "seduto": {
            "it": "Dici: 'Seduto!' Il pappagallo {nome} si accuccia sul tavolo.",
            "en": "You say: 'Sit!' The parrot {nome} crouches on the table."
        },
        "terra": {
            "it": "Dici: 'A terra!' Il pappagallo {nome} vola sul pavimento.",
            "en": "You say: 'Down!' The parrot {nome} flies to the floor."
        },
        "bravo": {
            "it": "Dici: 'Bravo!' Il pappagallo {nome} zompetta felice.",
            "en": "You say: 'Good!' The parrot {nome} hops happily."
        },
        "biscotto": {
            "it": "Dai un biscotto al pappagallo {nome}. Lo afferra con una zampa e lo sminuzza con il becco.",
            "en": "You give a biscuit to the parrot {nome}. It grabs it with a foot and shreds it with its beak."
        },
        "osserva": {
            "it": "Osservi il pappagallo {nome}. Vola su un trespolo e si sistema le piume con il becco.",
            "en": "You watch the parrot {nome}. It flies to a perch and preens its feathers with its beak."
        }
    }
}