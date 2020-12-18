"""
Summation
Write a program that finds the summation of every number from 1 to num. The number will always be a positive 
integer greater than 0.

For example:

summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
"""

""" def summation(num):
    llista = []
    count = 1
    for i in range(num):
        llista.append(count)
        count += 1
    return sum(llista)

num = 98
summation(num)
print(summation(num)) """


def summation(num):
    return sum(range(1,num+1))
num = 98
summation(num)
print(summation(num))