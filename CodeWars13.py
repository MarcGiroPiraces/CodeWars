"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that 
determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. 
Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
"""


def is_isogram(string):

    string1 = string.lower()
    
    if len(string) == 0:
        return True

    for i in string1:
        if string1.count(i) == 1:
            recompte = True
        else:
            recompte = False
            break
    return recompte

string = "agklmopqro"   
is_isogram(string)
print(is_isogram(string))


def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True