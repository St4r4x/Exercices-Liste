# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:14:08 2022

@author: st4r4x
"""
table_multiplication = []
for i in range(10):
    # remettre la table à zero entre chaque occurence de i
    table = []
    # insere la nouvelle liste dans le tableau
    for j in range(10):
        table.append(i*j)
    table_multiplication.append(table)

print(table_multiplication[int(input("Le premier chiffre à multiplier : "))][int(
    input("Le second chiffre à multiplier : "))])
