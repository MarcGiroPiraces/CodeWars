""" 
Given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
"""

def alphabet_position(text):
    import string
    abecedari = list(string.ascii_lowercase)
    abecedari1 = ''.join(abecedari)
    textMinuscul = text.lower() 
    llista = []
    count = 0
    while len(text) >= count + 1 :
        if textMinuscul[count].isalpha() == True:
            posicioLletra = abecedari1.index(textMinuscul[count])+1
            llista.append(str(posicioLletra))
            count += 1
        else:
            count += 1
        textNumeros = ' '.join(llista)
    return textNumeros        

text = "The sunset sets at twelve o' clock."
alphabet_position(text)

print(alphabet_position(text))



def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

def alphabet_position(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ')