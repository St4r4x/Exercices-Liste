# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:29:59 2022

@author: st4r4x
"""
A = [list(range(100)), list(range(100, 0, -1))]
B = [list(range(100, 200)), list(range(200, 100, -1))]



def additionMatrice(liste1, liste2):
    add = []
    for i in range(len(A)):
        add.append([])
        for j in range(len(B[i])):
            add[i].append(A[i][j]+B[i][j])
    return add


print(additionMatrice(A, B))
