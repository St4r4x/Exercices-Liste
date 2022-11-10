# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:26:48 2022

@author: st4r4x
"""

# Exercice 4 :

import random
liste_activite = ["Se reposer", "Se distraire", "Travailler"]


jour_equilibre = [1, 2, 3]


def semaine():
    liste_semaine = []
    for i in range(7):
        liste_semaine.append(jour_equilibre)
    return liste_semaine


def mois():
    liste_mois = []
    for i in range(4):
        liste_mois.append(semaine())
    return liste_mois


def annee():
    liste_annee = []
    for i in range(12):
        liste_annee.append(mois())
    return liste_annee


annee=[]


def simulation(liste):
    a = random.randint(1, 3)
    travail = 10
    repos = 10
    joie = 10
    jour = [1, 2, 3]
    annee.append(jour)
    for i in range(365):
        for j in jour:
            if j == 1:
                repos += 3
                travail -= 1
            if j == 2:
                joie += 2
                travail -= 1
                repos -= 1
            else:
                travail += 2
                repos -= 2
                joie -= 1
        if travail < repos:
            if travail < joie:
                annee.append([3, 3, a])
            else:
                annee.append([2, 2, a])
        if repos < travail:
            if repos < joie:
                annee.append([1, 1, a])
            else:
                annee.append([2, 2, a])
        if joie < travail:
            if joie < repos:
                annee.append([2, 2, a])
            else:
                annee.append([1, 1, a])

    return travail, repos, joie


sim = simulation(annee)
