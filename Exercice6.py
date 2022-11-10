# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 11:58:12 2022

@author: st4r4x
"""

# Exercice 6 :

import random

liste1 = list(range(100))


def melangeListe(liste):
    liste_melange = []
    liste_travail = liste[:]
    for i in range(len(liste_travail)):
        a = random.randint(0, len(liste_travail)-1)
        liste_melange.append(liste_travail[a])
        liste_travail.pop(a)
    liste = liste_melange[:]
    return liste


liste_melangee = melangeListe(liste1)


def maximum(liste):
    maxi = 0
    idx = 0
    for i in range(len(liste)):
        if maxi < liste[i]:
            maxi = liste[i]
            idx = i
    liste.pop(idx)
    return maxi, idx


def minimum(liste):
    mini = liste[0]
    idx = 0
    for i in range(len(liste)):
        if mini > liste[i]:
            mini = liste[i]
            idx = i
    liste.pop(idx)
    return mini, idx


# maxi = maximum(liste_melangee)[0]
# idx_max = maximum(liste_melangee)[1]
# mini = minimum(liste_melangee)[0]
# idx_min = minimum(liste_melangee)[1]
liste_triee = []

for i in range(len(liste_melangee)):
    liste_triee.append(maximum(liste_melangee)[0])
