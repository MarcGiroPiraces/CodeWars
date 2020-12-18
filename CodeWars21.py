#String incrementer
"""
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100
"""
def increment_string(strng):
    text = ''
    numerosLlista = []
    numerosText = 0
    for a in range(len(strng)):
        if strng[a].isalpha() == True:
            text += strng[a]

        else:
            numerosLlista.append(strng[a])

    numerosText = int(''.join(numerosLlista)) +1
    
    textFinal = text + str(numerosText)
    print(textFinal)
    return textFinal
    
increment_string('fooo')



        
