"""
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should 
be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
"""



def namelist(names):
    llista = []
    if len(names) > 2:
        for i in names:
            llista.append(i["name"])
            #print(llista)    
        junts1 = ', '.join(llista[0:-1])
        totsJunts = junts1 + ' & ' + llista[-1]
    
    elif len(names) == 2:
        for i in names:
            llista.append(i["name"])
        totsJunts = llista[0] + ' & ' + llista[1]

    else:
        none = ''
        if names == ([]):
            totsJunts = none

        else:
            for i in names:
                totsJunts = i["name"]
            
    return totsJunts


names = ([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])

namelist(names)

print(namelist(names))


def namelist(names):
    if len(names)==0: return ''
    if len(names)==1: return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']


def namelist(names):
  return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ",1)[::-1]











