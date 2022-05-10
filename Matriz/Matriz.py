# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:05:57 2022

@author: WPEDEV001
"""

import numpy as np   
  
#Matriz construida con numeros de 0-5
# Matiz cuadrada
dim = 5
v = np.random.randint(5, size=(dim , dim))
mRes = np.zeros(shape=(dim,dim))
print(v) 
print(mRes) 
# bools = np.apply_along_axis(lambda x: v[:,0][x] == sequence, 0, idx_mat)
# print("v[:,0] = ", v[1,0])#[fila,columna]
# print("h[0,:] = ", v[0,3])


i = 0
j = 0
for i in range(3):#filas
    print("i - "  + str(i))
    for j in range(3):#columnas


outputV1 = repr(v).count("0, 1, 2, 3") 
outputV2 = repr(v).count("1, 2, 3, 4")
outputV3 = repr(v).count("2, 3, 4, 5") 
 
if outputV1:
    print(F'Se encontro la secuecnia  v1 {outputV1} veces')
    i = 0
    j = 0
    for i in range(2):#filas
        print("i - "  + str(i))
        for j in range(4 ):#columnas
            if (v[i+1,j] == v[i,j] + 1) and (v[i+2,j] == v[i+1,j] + 1) and (v[i+3,j] == v[i+2,j] + 1):
                print("posicion incial [" + str(i) + ", " + str(j) + "]")
                print("posicion final [" + str(i+4) + ", " + str(j) + "]")
                # if v[i+2,j] == v[i+1,j] + 1:
                    # print("2 - 3 serie de primero y segundo")
                    # if v[i+3,j] == v[i+2,j] + 1:
                    #     print("3 - 4 serie de primero y segundo")
                

elif outputV2:
    print(F'Se encontro la secuecnia  v2 {outputV2} veces')
    for i in range(2):#filas
        print("i - "  + str(i))
        for j in range(4):#columnas
            if (v[i+1,j] == v[i,j] + 1) and (v[i+2,j] == v[i+1,j] + 1) and (v[i+3,j] == v[i+2,j] + 1):
                print("serie de primero y segundo en posicion incial [" + str(i) + ", " + str(j) + "]")
                print("serie de primero y segundo en posicion final [" + str(i+4) + ", " + str(j) + "]")
elif outputV3:
    print(F'Se encontro la secuecnia  v3 {outputV3} veces')
    for i in range(2):#filas
        print("i - "  + str(i))
        for j in range(4):#columnas
            if (v[i+1,j] == v[i,j] + 1) and (v[i+2,j] == v[i+1,j] + 1) and (v[i+3,j] == v[i+2,j] + 1):
                print("serie de primero y segundo en posicion incial [" + str(i) + ", " + str(j) + "]")
                print("serie de primero y segundo en posicion final [" + str(i+4) + ", " + str(j) + "]")
else :
    print('No se encontraron secuencias de numeros consecutivos')