import os  # prendiamo l intero modulo

from os import path  # apriamo il modulo e prendiamo solo la funzione path


# fuori dal pacchetto
import mio_pacchetto.modulo1

# dentro al pacchetto
from .modulo_vicino_nel_pacchetto import funzione_o_variabile
