from math import sqrt
import timeit
import datetime
from os import times
import numpy as np


def NumberofDivisors(number):
    nod = 0
    for j in range(1, int(sqrt(number))):
        if number % j == 0:
            nod += 2
    if int(sqrt(number)) * int(sqrt(number)) == number:
        nod -= 1
    return nod


number = 0
i = 1
while NumberofDivisors(number) < 500:
    number += i
    i += 1
print(number)
