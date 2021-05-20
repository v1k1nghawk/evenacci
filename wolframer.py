#!/usr/bin/env python3
########################################################################################################################
# Purpose: get even Fibonacci numbers using Wolfram Alpha API
# Programmer: Andrew Art
########################################################################################################################



import wolframalpha


def ask_wolfram(query: str="") -> str:
    '''Use Wolfram Alpha API to answer a question.
    :param query: question to Wolfram Alpha

    :raises IOError: unable to retrieve data Wolfram Alpha

    :returns: answer from Wolfram Alpha
    '''
    appid = 'Valid Wolfram Alpha AppID' # Modify this
    client = wolframalpha.Client(appid)
    try:
        response = client.query(query)
        return next(response.results).text
    except Exception as e:
        raise IOError(str(e))
        return ""


def f_multiple(quant: int=0) -> int:
    '''Print even numbers from the Fibonacci sequence using multiple queries.

    :param quant: required quantity of even Fibonacci numbers

    :returns: status (0 if successful)
    '''
    if isinstance(quant, int) != True or quant <= 0:
        print("Invalid argument")
        return 1

    even_counter = 0
    overall_counter = 0
    while even_counter < quant:
        try:
            fib_num = int(ask_wolfram("Fibonacci number " + str(overall_counter)))
            if fib_num % 2 == 0:
                if even_counter != 0:
                    print(", ", end="", flush=True)
                print(str(fib_num), end="", flush=True)
                even_counter += 1
                overall_counter += 1
        except (ValueError, IOError) as e:
            if "Invalid appid" in str(e):
                print("Error: ", str(e))
                return 2
            else: # retry
                pass
        else:
            overall_counter += 1
    print("")
    return 0


def f(quant: int=0) -> int:
    '''Print even numbers from the Fibonacci sequence using two queries at most.

    :param quant: required quantity of even Fibonacci numbers

    :returns: status (0 if successful)
    '''
    if isinstance(quant, int) != True or quant <= 0:
        print("Invalid argument")
        return 1

    try:
        # F_0
        wolfram_answer = ask_wolfram("Fibonacci number 0")

        if quant > 1:
            wolfram_answer += ", " + ask_wolfram("even Fibonacci numbers " + str(quant - 1))
            wolfram_answer = wolfram_answer.split(" (", 1)[0].replace(' |', ',')
        print(wolfram_answer)
    except IOError as e:
        print("Error: ", str(e))
        return 2
    else:
        return 0


f(4)
