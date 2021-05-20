#!/usr/bin/env python3
########################################################################################################################
# Purpose: get even Fibonacci numbers using Machine Learning techniques
# Programmer: Andrew Art
########################################################################################################################



import numpy as np
import tensorflow as tf
import math


def f(quant: int=0) -> int:
    '''Print even numbers from the Fibonacci sequence.

    :param quant: required quantity of even Fibonacci numbers

    :returns: status (0 if successful)
    '''
    if isinstance(quant, int) != True or quant <= 0 or quant > 6:
        print("Invalid argument")
        return 1

    # Get model from storage
    try:
        model = tf.keras.models.load_model("fibmodel")
    except IOError as e:
        print("Error: ", str(e))
        return 2

    # Use the model to predict an even Fibonacci number from its index
    x_values = np.linspace(start=0, stop=quant-1, num=quant, dtype=int)
    y_estimated = model.predict(x_values).astype(int)

    for i in range(len(y_estimated)):
        print(math.ceil(y_estimated[i][0] / 2.) * 2, end="", flush=True)
        if i+1 != len(y_estimated):
            print(", ", end="", flush=True)
    print("")

    return 0


f(4)
