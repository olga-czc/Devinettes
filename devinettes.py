#!/usr/bin/env python3
"""
Jeu de devinettes.

Par olga Cazacioc
"""
import random


def main():
    """
    Fonction principale
    """
    print("Bonjour, je m'appele Olax 2020 \nJ'ai choisi un nombre entier entre 1 et 100"
         "\nPouvez-vous le deviner?")

    nombre_aleatoire= random.randrange(101)
    sequence = []
    trouver_nombre(nombre_aleatoire, sequence)

def trouver_nombre(nombre_aleatoire, sequence):
    """
    Affiche progressivement une séquence de nombre à partir de 1 en montant

    :param nombre_aleatoire: jusqu'à ou compter
    """
    nrEssai = 1
    chiffre = 0

    while chiffre != nombre_aleatoire:

        chiffre = lire_chiffre(nrEssai)
        sequence.append(chiffre)
        nrEssai += 1

        if chiffre > nombre_aleatoire:
         print("> Votre nombre est trop grand...")
         verifier_nb_essai(nrEssai, nombre_aleatoire)

        elif chiffre < nombre_aleatoire:
         print("> Votre nombre est trop petit...")
         verifier_nb_essai(nrEssai, nombre_aleatoire)

    print("Bravo, vous avez deviné le nombre")
    print("Votre séquence gagnante est:", sequence)

def  lire_chiffre(nr):
    while True:
        try:
            print("Essai ", nr, ": ", end='')
            chiffre = int(input())
        except ValueError:
            print(">>> ERREUR: Entrez un nombre entier svp")
            continue
        else:
            return chiffre
            break

def verifier_nb_essai(nr, nr_aleatoire):
    if nr == 11:
        print("> Désolé, vous avez échoué après 10 tentatives")
        print("> Le nombre choisi était: ", nr_aleatoire)

if __name__ == '__main__':
    main()