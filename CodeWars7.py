"""
Given two integers a and b, which can be positive or negative, find the sum of all the numbers between 
including them too and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
"""

""" def get_sum(a,b):
    llista = []
    if a == b:
        return a 
    else:
        if a > b:
            for i in range(b, a+1):
                llista.append(i)
        else:
            for i in range(a, b+1):
                llista.append(i)
        return sum(llista)

a = 4
b = 7
print(get_sum(a,b)) """


def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

a = 4
b = 7
print(get_sum(a,b))