#String Letter Counting
"""
Take an input string and return a string that is made up of the number of occurences of each english 
letter in the input followed by that letter, sorted alphabetically. The output string shouldn't contain 
chars missing from input (chars with 0 occurence); leave them out.

An empty string, or one with no letters, should return an empty string.

Notes:

the input will always be valid;
treat letters as case-insensitive
Examples
"This is a test sentence."  ==>  "1a1c4e1h2i2n4s4t"
""                          ==>  ""
"555"                       ==>  ""
"""

def string_letter_count(s):
    paraula = ''
    llistaRecompte = []
    definitiu = ''
    frase = s.lower()
    for letters in frase:
        if letters.isalpha() == True:
            paraula += letters
            paraula = sorted(paraula)
    for elements in paraula:
        llistaRecompte += [str(paraula.count(elements)) + elements]
    llistaRecompte = list(dict.fromkeys(llistaRecompte))
    definitiu = ''.join(llistaRecompte)
    return definitiu
    
print(string_letter_count('This is a test sentence.'))

