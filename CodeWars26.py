# Multiplication Tables

"""
Create a function that accepts dimensions, of Rows x Columns, as parameters in order to create a multiplication table
sized according to the given dimensions. **The return value of the function must be an array, and the numbers must be
Fixnums, NOT strings.

Example:

multiplication_table(3,3)

1 2 3
2 4 6
3 6 9

-->[[1,2,3],[2,4,6],[3,6,9]]

Each value on the table should be equal to the value of multiplying the number in its first row times the number in its
first column.
"""


def multiplication_table(row, col):
    diccionari = {}

    for c in range(1, row + 1):
        diccionari[c] = []

    for a in range(1, col + 1):
        diccionari[1].append(a)

    for a in diccionari.keys():
        if a != 1:
            diccionari[a] = [x * a for x in diccionari[1]]

    llista_definitiva = []

    for a in diccionari.values():
        llista_definitiva.append(a)

    return llista_definitiva
