import numpy as np

def saisie_entier(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Erreur : veuillez entrer un entier.")

# --- 1. Saisie du nombre de termes ---
N = saisie_entier("Combien de termes voulez-vous saisir ? ")

# --- 2. Saisie des N valeurs ---
x = []
for i in range(N):
    valeur = saisie_entier(f"Entrer le terme n°{i+1} : ")
    x.append(valeur)

# Conversion en tableau numpy
x = np.array(x, dtype=float)

# --- 3. Calcul de la DFT ---
X = np.fft.fft(x)

# --- 4. Affichage ---
print("\nVoici votre DFT :")
print(X)