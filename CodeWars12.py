"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""

def find_uniq(arr):
    arr.sort()
    if arr[0] == arr[1]:
        numDiferent = arr[-1]
    else:
        numDiferent = arr[0]
    return numDiferent

arr = [ 1, 1, 1, 2, 1, 1 ]
find_uniq(arr)

print(find_uniq(arr))


def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b



