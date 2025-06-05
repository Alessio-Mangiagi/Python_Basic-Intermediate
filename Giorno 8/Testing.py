import pandas as pd # type: ignore

# Crea un dizionario di dati
data = {
    'Nome': ['Anna', 'Luca', 'Marco', 'Giulia'],
    'Età': [23, 21, 25, 22],
    'Voto': [28, 30, 27, 29]
}

# Crea un DataFrame dai dati
df = pd.DataFrame(data)

# Visualizza il DataFrame
print("DataFrame:")
print(df)

# Calcola la media della colonna 'Voto'
media_voto = df['Voto'].mean()
print(f"\nMedia dei voti: {media_voto}")
