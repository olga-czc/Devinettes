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
    tentatives = 10


    trouver_nombre(nombre_aleatoire, sequence, tentatives)


def trouver_nombre(nombre_aleatoire, sequence, tentatives):
    """
    Affiche progressivement une séquence de nombre à partir de 1 en montant

    :param nombre_aleatoire: jusqu'à ou compter
    """
    nrEssai = 1
    chiffre = 0

    while chiffre != nombre_aleatoire:

        chiffre = lire_chiffre(nrEssai, tentatives)
        sequence.append(chiffre)
        nrEssai += 1

        if chiffre > nombre_aleatoire:
         print("> Votre nombre est trop grand...")
         verifier_nb_essai(nrEssai, nombre_aleatoire, tentatives)

        elif chiffre < nombre_aleatoire:
         print("> Votre nombre est trop petit...")
         verifier_nb_essai(nrEssai, nombre_aleatoire, tentatives)

    print("> Bravo, vous avez deviné le nombre")
    print("> Votre séquence gagnante est:", sequence)
    recommencer()

def  lire_chiffre(nr, tentatives):
    while True:
        try:
            print("Essai ", nr, ": ", end='')
            # chiffre = int(input())
            ligne = input()
            chiffre = int(ligne)
            #if ligne == 'PPP':
             #   sortir(tentatives)
              #  return ligne
        except ValueError:
            print(">>> ERREUR: Entrez un nombre entier svp")
            continue
        else:
            return chiffre
            break

def verifier_nb_essai(nr, nr_aleatoire, tentatives):
    if nr == 11:
        print("> Désolé, vous avez échoué après ", tentatives, "tentatives")
        print("> Le nombre choisi était: ", nr_aleatoire)
        recommencer()

def sortir(tentatives):
    print("> Désolé, vous avez échoué après ", tentatives, "tentatives")

def recommencer():

    while True:

        print("Voulez-vous rejouer? [O/N] ", end='')
        reponse = input()
        if reponse == 'O' or reponse == 'o' or reponse == 'oui':
            nombre_aleatoire = random.randrange(101)
            sequence = []
            tentatives = 10
            trouver_nombre(nombre_aleatoire, sequence, tentatives)
        elif reponse == 'N' or reponse == 'n' or reponse == 'non':
            print("Au revoir !")
            break
        else:
            print("Choix invalide")



if __name__ == '__main__':
    main()


