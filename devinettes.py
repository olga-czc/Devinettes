#!/usr/bin/env python3
"""
Jeu de devinettes.

Par olga Cazacioc
"""
import random

# Constantes
MAX_ESSAIS = 10
NOMBRE_MAX = 100
CHEAT_CODE_ECHOUER = 'PPP'
CHEAT_CODE_GAGNER = 'GGG'


def main():
    """
    Fonction principale
    """
    print("Bonjour, je m'appele Olax 2020 \nJ'ai choisi un nombre entier entre 1 et 100"
          "\nPouvez-vous le deviner?")

    nombre_aleatoire = random.randrange(NOMBRE_MAX)
    sequence = []

    tentatives = 0
    nb_parties_jouées = 0
    nb_essais_effectués = 0

    trouver_nombre(nombre_aleatoire, sequence, tentatives, nb_parties_jouées, nb_essais_effectués)


def trouver_nombre(nombre_aleatoire, sequence, tentatives, nb_parties_jouées, nb_essais_effectués):
    """
    Compare le nombre donné avec le nombre généré

    :param nombre_aleatoire:
    :param sequence:
    :param tentatives:
    :param nb_parties_jouées:
    :param nb_essais_effectués:
    """

    tentatives += 1
    chiffre = 0

    while chiffre != nombre_aleatoire:

        chiffre = lire_chiffre(tentatives, sequence, nombre_aleatoire, nb_parties_jouées, nb_essais_effectués)
        sequence.append(chiffre)
        tentatives += 1
        nb_essais_effectués += 1

        if chiffre > nombre_aleatoire:
            print("> Votre nombre est trop grand...")
            verifier_nb_essai(nombre_aleatoire, tentatives, nb_parties_jouées, nb_essais_effectués)

        elif chiffre < nombre_aleatoire:
            print("> Votre nombre est trop petit...")
            verifier_nb_essai(nombre_aleatoire, tentatives, nb_parties_jouées, nb_essais_effectués)

    gagner(sequence, nb_parties_jouées, nb_essais_effectués)


def lire_chiffre(nr, sequence, nr_aleatoire, nb_parties_jouées, nb_essais_effectués):
    """
    Verifie le nombre donné

    :param nr:
    :param sequence:
    :param nr_aleatoire:
    :param nb_parties_jouées:
    :param nb_essais_effectués:
    :return:
    """
    while True:
        try:
            print("Essai ", nr, ": ", end='')
            ligne = input()
            verifier_ligne(ligne, nr, sequence, nr_aleatoire, nb_parties_jouées, nb_essais_effectués)

            chiffre = int(ligne)
        except ValueError:
            print(">>> ERREUR: Entrez un nombre entier svp")
            continue
        else:
            return chiffre


def verifier_nb_essai(nr_aleatoire, tentatives, nb_parties_jouées, nb_essais_effectués):
    """
    Verifie si le nombre d'essais ne depasse pas le nombre maximal d'essais

    :param nr_aleatoire:
    :param tentatives:
    :param nb_parties_jouées:
    :param nb_essais_effectués:
    """
    if tentatives == MAX_ESSAIS + 1:
        print("> Désolé, vous avez échoué après ", MAX_ESSAIS, "tentatives")
        print("> Le nombre choisi était: ", nr_aleatoire)
        recommencer(nb_parties_jouées, nb_essais_effectués)


def gagner(sequence, nb_parties_jouées, nb_essais_effectués):
    """
    Affiche le résultat si gagné

    :param sequence:
    :param nb_parties_jouées:
    :param nb_essais_effectués:
    """
    print("> Bravo, vous avez deviné le nombre")
    print("> Votre séquence gagnante est:", sequence)
    nb_parties_jouées += 1
    recommencer(nb_parties_jouées, nb_essais_effectués)


def echouer(nr, nr_aleatoire, nb_parties_jouées, nb_essais_effectués):
    """
    Affiche le résultat si echoué

    :param nr:
    :param nr_aleatoire:
    :param nb_parties_jouées:
    :param nb_essais_effectués:
    """
    print("> Désolé, vous avez échoué après ", nr, "tentatives")
    print("> Le nombre choisi était: ", nr_aleatoire)
    recommencer(nb_parties_jouées, nb_essais_effectués)


def recommencer(nb_parties_jouées, nb_essais_effectués):
    """
    Reset du jeu ou fin

    :param nb_parties_jouées:
    :param nb_essais_effectués:
    """
    while True:

        print("Voulez-vous rejouer? [O/N] ", end='')
        reponse = input()
        print("")
        if reponse == 'O' or reponse == 'o' or reponse == 'oui':
            nombre_aleatoire = random.randrange(NOMBRE_MAX)
            sequence = []
            tentatives = 0
            trouver_nombre(nombre_aleatoire, sequence, tentatives, nb_parties_jouées, nb_essais_effectués)
        elif reponse == 'N' or reponse == 'n' or reponse == 'non':
            nb_essais_effectués += 1
            print("   Nombre de parties jouées: ", nb_parties_jouées)
            print("  Nombre d'essais effectués: ", nb_essais_effectués)
            print("Moyenne d'essais par partie: ", nb_essais_effectués / nb_parties_jouées)
            print("Au revoir !")
            break
        else:
            print("Choix invalide")


def verifier_ligne(ligne, nr, sequence, nr_aleatoire, nb_parties_jouées, nb_essais_effectués):
    """
    Verifie le cheat code

    :param ligne: input d'utilisateur
    :param nr:
    :param sequence:
    :param nr_aleatoire:
    :param nb_parties_jouées:
    :param nb_essais_effectués:
    """
    if ligne == CHEAT_CODE_ECHOUER:
        echouer(nr, nr_aleatoire, nb_parties_jouées, nb_essais_effectués)

    elif ligne == CHEAT_CODE_GAGNER:
        sequence.append(ligne)
        gagner(sequence, nb_parties_jouées, nb_essais_effectués)


if __name__ == '__main__':
    main()
