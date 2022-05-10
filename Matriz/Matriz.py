# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:05:57 2022

@author: Gustavo Pellicore
"""

import numpy as np   
  
#Matriz construida con numeros de 0-5
# Matiz cuadrada
dim = 5

mResH = np.zeros(shape=(dim,dim))
mResV = np.zeros(shape=(dim,dim))
estado = True

while estado == True:
    v = np.random.randint(11, size=(dim , dim))#numero entre 0 - 10
    print(v) 

    #resta por filas por filas
    for i in range(5):#columnas
        for j in range(5):#filas
            if (i+1 < 5):
                mResH[i+1,j]=v[i+1,j] - v[i,j]
            else :
                break
            
    # print(f'Matriz de pasos por filas \n {mResH}')   
    
    ocurrenciaH = 0
    
    for i in range(5):#filas
        for j in range(5):#filas
            if (i+3 < 5) and ((mResH[i,j] == 0) or (mResH[i,j] == 1)) and (mResH[i+1,j] == 1) and (mResH[i+2,j] == 1) and (mResH[i+3,j] == 1):
                # print(f'{mResH[i,j]} , {mResH[i+1,j]} , {mResH[i+2,j]} , {mResH[i+3,j]}')
                ocurrenciaH += 1
                print(f'{ocurrenciaH} - Se encontro una secuencia en columna, desde [{i+1},{j+1}] hasta [{i+3+1},{j+1}]')
                estado = False
                break
                
            elif (i+4 < 5) and ((mResH[i+1,j] == 0) or (mResH[i+1,j] == 1)) and (mResH[i+2,j] == 1) and (mResH[i+3,j] == 1) and (mResH[i+4,j] == 1):
                # print(f'{mResH[i+1,j]} , {mResH[i+2,j]} , {mResH[i+3,j]} , {mResH[i+4,j]}')
                ocurrenciaH += 1
                print(f'{ocurrenciaH} - Se encontro una secuencia en columna, desde [{i+2},{j+1}] hasta [{i+4+1},{j+1}]')
                estado = False
                break
    

    for j in range(5):#filas
        for i in range(5):#columnas
            if (j+1 < 5):
                mResV[i,j+1]=v[i,j+1] - v[i,j]
            else :
                break   
            
    # print(f'Matriz de pasos por columnas \n {mResV}')
       
    ocurrenciaV = 0
              
    for i in range(5):#filas
        for j in range(5):#filas
            if (j+3 < 5) and ((mResV[i,j] == 0) or (mResV[i,j] == 1)) and (mResV[i,j+1] == 1) and (mResV[i,j+2] == 1) and (mResV[i,j+3] == 1):
                # print(f'{mResV[i,j]} , {mResV[i,j+1]} , {mResV[i,j+2]} , {mResV[i,j+3]}')
                ocurrenciaV += 1
                print(f'{ocurrenciaV} - Se encontro una secuencia en fila, desde [{i+1},{j+1}] hasta [{i+1},{j+3+1}]')
                estado = False
                break
                
            elif (j+4 < 5) and ((mResV[i,j+1] == 0) or (mResV[i,j+1] == 1)) and (mResV[i,j+2] == 1) and (mResV[i,j+3] == 1) and (mResV[i,j+4] == 1):
                # print(f'{mResV[i,j+1]} , {mResV[i,j+2]} , {mResV[i,j+3]} , {mResV[i,j+4]}')
                ocurrenciaV += 1
                print(f'{ocurrenciaV} - Se encontro una secuencia en fila, desde [{i+2},{j+1}] hasta [{i+5},{j+1}]')
                estado = False
                break
