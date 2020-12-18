# What's a Perfect Power anyway?

"""
A perfect power is a classification of positive integers:

In mathematics, a perfect power is a positive integer that can be expressed as an integer power of another positive
integer. More formally, n is a perfect power if there exist natural numbers m > 1, and k > 1 such that mk = n.

Your task is to check wheter a given integer is a perfect power. If it is a perfect power, return a pair m and k with
mk = n as a proof. Otherwise return Nothing, Nil, null, NULL, None or your language's equivalent.

Note: For a perfect power, there might be several pairs. For example 81 = 3^4 = 9^2, so (3,4) and (9,2) are valid
solutions. However, the tests take care of this, so if a number is a perfect power, return any pair that proves it.

Examples
isPP(4) => [2,2]
isPP(9) => [3,2]
isPP(5) => None
"""
import math

def isPP(n):
    for a in range(2, int(math.sqrt(n)) + 1):
        max_number = int(math.sqrt(n))
        min_number = 0
        answer = int((max_number + min_number) / 2)
        answer_anterior = 0
        while answer_anterior != answer:
            answer_anterior = answer
            if pow(a, answer) == n:
                return [a, answer]
            elif pow(a, answer) > n:
                max_number = answer
            elif pow(a, answer) < n:
                min_number = answer
            answer = int((max_number + min_number) / 2)
    return None


"""
def isPP(n):
    for i in range(2, n+1):
        for j in range(2, n+1):
            if i**j > n:
                break
            elif i**j == n:
                return [i, j]
    return None
"""

print(isPP(59049))
