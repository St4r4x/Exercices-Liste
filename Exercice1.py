# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:42:05 2022

@author: st4r4x
"""

# Exercice 1 :
import random

liste_entier = list(range(101))
liste_dup = liste_entier[:]


def supElement(liste):
    milieu_liste = int((len(liste))/2)
    liste.pop(milieu_liste)
    return liste


supElement(liste_dup)


def melangeListe(liste):
    liste_melange = []
    liste_travail = liste[:]
    for i in range(len(liste_travail)):
        a = random.randint(0, len(liste_travail)-1)
        liste_melange.append(liste_travail[a])
        liste_travail.pop(a)
    liste = liste_melange[:]
    return liste


liste_entier = melangeListe(liste_entier)


for i in range(len(liste_entier)):
    if liste_entier[i] not in liste_dup:
        print(i)


def funIdxRetire(listeComplete, listeIncomplete):
    for i in range(len(listeComplete)):
        isIn = False
        for j in listeIncomplete:
            if listeComplete[i] == j:
                isIn = True
        if not isIn:
            return i
