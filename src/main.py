import numpy as np

def saisie_entier(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Erreur : veuillez entrer un entier.")

a = saisie_entier("Entrer le premier terme : ")
b = saisie_entier("Entrer le second terme : ")
c = saisie_entier("Entrer le troisième terme : ")
d = saisie_entier("Entrer le quatrième terme : ")

print ("")
x = np.array([a, b, c, d], dtype=float)
X = np.fft.fft(x)

print("Voici votre DFT : ", X)
