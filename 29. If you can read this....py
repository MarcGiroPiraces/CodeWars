# If you can read this...

"""
The idea for this Kata came from 9gag today.here

You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet) wiki.

Like this:

Input:

If, you can read?

Output:

India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?

Notes

The set of used punctuation is .!?.
Punctuation should be kept in your return string, but spaces should not.
Xray should not have a dash within.
Every word and punctuation mark should be seperated by a space ' '.
There should be no trailing whitespace
"""


def to_nato(words):
    traductor = {'a': 'Alfa', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo', 'f': 'Foxtrot', 'g': 'Golf',
                 'h': 'Hotel', 'i': 'India', 'j': 'Juliett', 'k': 'Kilo', 'l': 'Lima', 'm': 'Mike', 'n': 'November',
                 'o': 'Oscar', 'p': 'Papa', 'q': 'Quebec', 'r': 'Romeo', 's': 'Sierra', 't': 'Tango', 'u': 'Uniform',
                 'v': 'Victor', 'w': 'Whiskey', 'x': 'Xray', 'y': 'Yankee', 'z': 'Zulu'}
    llista = []

    for letter in words:
        if letter == ' ':
            pass
        elif traductor.get(letter.lower(), False):
            llista.append(traductor[letter.lower()])
        else:
            llista.append(letter)

    # print(llista)
    return ' '.join(llista)


print(to_nato('If, you can read?'))


