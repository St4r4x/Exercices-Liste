# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 09:19:36 2022

@author: st4r4x
"""

# Exercice 3 :


def listeFibo(taille):
    liste_fibo = [0, 1]
    for i in range(1, taille-1):
        x = liste_fibo[i]+liste_fibo[i-1]
        liste_fibo.append(x)
    return liste_fibo


liste_fibo = listeFibo(100)


def fiboAdd(liste):
    liste_fibo_fibo = []
    for i in range(1, 99):
        x = liste[i-1]+liste[i+1]
        liste_fibo_fibo.append(x)
    return liste_fibo_fibo


liste_fibo_fibo = fiboAdd(liste_fibo)
liste_dup = liste_fibo_fibo[:]

for i in liste_fibo:
    for j in liste_dup:
        if i == j:
            liste_dup.remove(j)

somme = 0
for x in liste_dup:
    somme = x+somme
