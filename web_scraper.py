#!/usr/bin/env python3
########################################################################################################################
# Purpose: get even Fibonacci numbers using Web Scraping
# Programmer: Andrew Art
########################################################################################################################



from urllib.request import Request, urlopen
from urllib import error


def get_webcontent(uri: str="") -> str:
    '''Acquire the content of a specified webpage.
    :param uri: webpage address

    :raises IOError: unable to retrieve data from *uri*

    :returns: webpage content
    '''
    req = Request(uri, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html_bytes = urlopen(req).read()
        html = html_bytes.decode("utf-8")
        return html
    except (error.HTTPError, error.URLError) as e:
        raise IOError(e.__dict__)


def f(quant: int=0) -> int:
    '''Print even numbers from the Fibonacci sequence.

    :param quant: required quantity of even Fibonacci numbers

    :returns: status (0 if successful)
    '''
    if isinstance(quant, int) != True or quant <= 0 or quant > 300:
        print("Invalid argument")
        return 1

    # Retrieve Fibonacci series' data from an external source
    url = "http://www.fullbooks.com/The-first-1001-Fibonacci-Numbers.html"
    try:
        raw_fibo_data = get_webcontent(url)
    except IOError as e:
        print("Web service error: " + str(e))
        return 2

    # F_0
    print(0, end="", flush=True)
    # Extract even Fibonacci numbers
    even_counter = 1
    next_even_index = 3
    for line in raw_fibo_data.splitlines():
        if even_counter == quant:
            break
        position_fibnum = line.split(" ")
        try:
            if (int(position_fibnum[0]) == next_even_index):
                fib_num = int(position_fibnum[1][:-len("<br>")])
                print(", " + str(fib_num), end="", flush=True)
                even_counter += 1
                next_even_index += 3
        except ValueError as e:
            pass
    print("")

    if even_counter != quant:
        print("Failed to extract all required even Fibonacci numbers")
        return 3
    return 0


f(4)
