#!/usr/bin/env python3
########################################################################################################################
# Purpose: get even Fibonacci numbers using Binet's formula
# Programmer: Andrew Art
########################################################################################################################



import math


def f(quant: int=0) -> int:
    '''Print even numbers from the Fibonacci sequence.

    :param quant: required quantity of even Fibonacci numbers

    :returns: status (0 if successful)
    '''
    phi = (1 + math.sqrt(5)) / 2
    even_counter = 0
    fib_index = 0
    while even_counter < quant:
        F_i = round(pow(phi, fib_index) / math.sqrt(5))
        if even_counter != 0:
            print(", ", end="", flush=True)
        print(str(F_i), end="", flush=True)
        even_counter += 1
        fib_index += 3

    return 0


f(4)
