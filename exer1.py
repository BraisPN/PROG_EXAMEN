#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exercicio 1. Crea unha función recursiva decimal_to_binario(numero: int) -> str que obteña o número binario dun número N decimal. 
Axuda: https://ed.team/blog/sistemas-binarios-y-decimales.
"""

__author__ = "Brais Pose Nieto"

def decimal_to_binario(n:int,binario:str) -> str:

    if type(n) is not int:
        raise ValueError
    
    if type(binario) is not str:
        raise ValueError

    if n > 1:
        binario = decimal_to_binario(n // 2,binario)
        
    binario += str(n % 2)
        
    return binario


try:
    print(decimal_to_binario(n = int(input("Decimal -> ")),binario=""))

except ValueError:
    print("--Erro--")