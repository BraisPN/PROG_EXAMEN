#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exercicio 2. Crea unha función recursiva suma_dixitos(n: int) -> int en Python que calcule a suma dos díxitos dun número enteiro positivo. 
A suma de díxitos é o resultado de sumar todos os díxitos individuais dun número. Por exemplo, para o número 1234, a suma dos díxitos é 1 + 2 + 3 + 4 = 10.

A función debe incluír unha condición base para o caso cando n é menor que 10 e polo tanto ten só un díxito.
A función debe chamarse a si mesma para sumar o último díxito e a suma dos díxitos restantes do número.
"""

__author__ = "Brais Pose Nieto"

def suma_dixitos(n: int) -> int:
    if type(n) is not int:
        raise ValueError

    if n < 10:
        return n
    else:
        return n % 10 + suma_dixitos(n // 10)


try:
    print(suma_dixitos(n = int(input("Numero ->"))))

except ValueError:
    print("--Error--")