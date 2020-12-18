# Simple Pig Latin

"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text):
    frase = text.split(' ')
    llista_paraules = []

    for paraula in frase:
        nova_paraula = ''
        if paraula.isalpha():
            for index in range(len(paraula)):
                if index == 0:
                    pass
                else:
                    nova_paraula += paraula[index]
            nova_paraula += paraula[0] + 'ay'
            llista_paraules.append(nova_paraula)

        else:
            llista_paraules.append(paraula)

    return ' '.join(llista_paraules)
