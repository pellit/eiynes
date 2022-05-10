# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:46:51 2022

@author: WPEDEV001
"""

import random




def generateRandon():
    lista = [{'id':i  ,'edad':random.randint(1,101)} for i in range(10)]
    return lista
    

dicList = generateRandon()
print(f'Lista de inicio =  {dicList}')
print('________________________________________')
dicList.sort(key=lambda p: p['edad'],reverse=True)
print(f'Ordenada de mayor a menor = {dicList}')
print('________________________________________')
idMin = dicList[-1]['id']
idMax = dicList[0]['id']
print(f'Persona de mas edad para el id = {idMax}')
print(f'Persona de menos edad para el id = {idMin}')
