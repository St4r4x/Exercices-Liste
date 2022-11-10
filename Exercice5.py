# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 11:25:52 2022

@author: st4r4x
"""

# Exercice 5 :


def mutismum(phrase):
    phrase_temp = ""
    for i in phrase:
        if i == "p":
            phrase_temp += "m"
        elif i == "m":
            phrase_temp += "p"
        elif i == "P":
            phrase_temp += "M"
        elif i == "M":
            phrase_temp += "P"
        else:
            phrase_temp += i
    return phrase_temp


print(mutismum(input("Vous vouliez dire ? ")))
