import pandas as pd
import numpy as np
from sympy import primefactors


def inner_product(number):
    """Calculates the product of the integers in an n-digit number"""
    product = 1
    while number > 0:
        product *= (number % 10)
        number //= 10

    return product


df = pd.DataFrame([ [0, 0, 0] for i in range(6)],
                  index=[210, 144, 54, 135, 4, 49],
                  columns=[6615, 15552, 430])

print(df)

for i in df.index:
    print(primefactors(i, verbose=True))