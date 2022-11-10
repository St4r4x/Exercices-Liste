# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 16:25:36 2022

@author: st4r4x
"""

# Exercice 2 :
import random
import string

alphabet = list(string.ascii_lowercase)
liste_voyelle = ["a", "e", "i", "o", "u", "y"]
liste_domaine = ["gmail", "yahoo", "wanadoo", "hotmail", "caramail"]
liste_terminaison = [".fr", ".com", ".ru", ".net", ".li", ".eu"]
liste_consonne = []

for i in alphabet:
    if i not in liste_voyelle:
        liste_consonne.append(i)


def nomDeDomaine(liste1, liste2):
    nom_domaine = random.choice(liste_domaine)+random.choice(liste_terminaison)
    return nom_domaine


def motAleatoire(taille):
    mot = ""
    for i in range(taille):
        if i % 2 == 0:
            a = random.randint(0, len(liste_consonne)-1)
            mot += liste_consonne[a]
        else:
            b = random.randint(0, len(liste_voyelle)-1)
            mot += liste_voyelle[b]
    return mot


def regroupement(taille, liste1, liste2):
    mail = motAleatoire(taille) + "@" + nomDeDomaine(liste1, liste2)
    return mail


print(regroupement(10, liste_domaine, liste_terminaison))
