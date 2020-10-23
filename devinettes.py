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
    tent = 0
    nb_parties_jouées = 0
    nb_essais_effectués = 0
    nb_essais = 0

    trouver_nombre(nombre_aleatoire, sequence, tentatives, tent, nb_parties_jouées, nb_essais_effectués)


def trouver_nombre(nombre_aleatoire, sequence, tentatives, tent, nb_parties_jouées, nb_essais_effectués):
    """
    Affiche progressivement une séquence de nombre à partir de 1 en montant

    :param nombre_aleatoire: jusqu'à ou compter
    """
    nrEssai = 1
    chiffre = 0

    while chiffre != nombre_aleatoire:

        chiffre = lire_chiffre(nrEssai, sequence, nombre_aleatoire, nb_parties_jouées, nb_essais_effectués)
        sequence.append(chiffre)
        nrEssai += 1
        nb_essais_effectués += 1

        if chiffre > nombre_aleatoire:
         print("> Votre nombre est trop grand...")
         verifier_nb_essai(nrEssai, nombre_aleatoire, tentatives, nb_parties_jouées, nb_essais_effectués)

        elif chiffre < nombre_aleatoire:
         print("> Votre nombre est trop petit...")
         verifier_nb_essai(nrEssai, nombre_aleatoire, tentatives, nb_parties_jouées, nb_essais_effectués)

    gagner(sequence, nb_parties_jouées, nb_essais_effectués)

def  lire_chiffre(nr, sequence, nr_aleatoire, nb_parties_jouées, nb_essais_effectués):
    while True:
        try:
            print("Essai ", nr, ": ", end='')
            # chiffre = int(input())
            ligne = input()
            verifierLigne(ligne, nr, sequence, nr_aleatoire, nb_parties_jouées, nb_essais_effectués)

            chiffre = int(ligne)
        except ValueError:
            print(">>> ERREUR: Entrez un nombre entier svp")
            continue
        else:
            return chiffre
            break

def verifier_nb_essai(nr, nr_aleatoire, tentatives, nb_parties_jouées, nb_essais_effectués):
    if nr == 11:
        print("> Désolé, vous avez échoué après ", tentatives, "tentatives")
        print("> Le nombre choisi était: ", nr_aleatoire)
        recommencer(nb_parties_jouées, nb_essais_effectués)

def  gagner(sequence, nb_parties_jouées, nb_essais_effectués):
    print("> Bravo, vous avez deviné le nombre")
    print("> Votre séquence gagnante est:", sequence)
    recommencer(nb_parties_jouées, nb_essais_effectués)

def echouer(nr, nr_aleatoire,nb_parties_jouées, nb_essais_effectués):
    print("> Désolé, vous avez échoué après ", nr, "tentatives")
    print("> Le nombre choisi était: ", nr_aleatoire)
    recommencer(nb_parties_jouées, nb_essais_effectués)

def recommencer(nb_parties_jouées, nb_essais_effectués):

    while True:

        print("Voulez-vous rejouer? [O/N] ", end='')
        reponse = input()
        print("")
        nb_parties_jouées +=1
        if reponse == 'O' or reponse == 'o' or reponse == 'oui':
            nombre_aleatoire = random.randrange(101)
            sequence = []
            tentatives = 10
            tent = 0
            trouver_nombre(nombre_aleatoire, sequence, tentatives, tent, nb_parties_jouées, nb_essais_effectués)
        elif reponse == 'N' or reponse == 'n' or reponse == 'non':
            print("   Nombre de parties jouées: ", nb_parties_jouées)
            print("  Nombre d'essais effectués: ",nb_essais_effectués)
            print("Moyenne d'essais par partie: ",nb_essais_effectués/nb_parties_jouées)
            print("Au revoir !")
            break
        else:
            print("Choix invalide")

def verifierLigne(ligne, nr, sequence, nr_aleatoire, nb_parties_jouées, nb_essais_effectués):
    if ligne == 'PPP':
       nb_essais_effectués += 1
       echouer(nr, nr_aleatoire, nb_parties_jouées, nb_essais_effectués)
    if ligne == 'GGG':
       nb_essais_effectués += 1
       sequence.append(ligne)
       gagner(sequence, nb_parties_jouées, nb_essais_effectués)

if __name__ == '__main__':
    main()


