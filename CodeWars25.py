# Array.diff

"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the
result.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
"""

# Solucio
# def array_diff(a, b):
#     c = []
#     for elements in a:
#         if elements not in b:
#             c.append(elements)
#     return c


# List Comprehension
# def array_diff(a, b):
#     c = []
#     [c.append(elements) for elements in a if elements not in b]
#     return c


def array_diff(a, b):
    c = []
    return [elements for elements in a if elements not in b]


