# Build Tower
"""
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;

For example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]

and a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
"""
def tower_builder(n_floors):
    tower = []
    tower2 = []
    element = '*'
    for i in range(n_floors):
        if i == 0:
            tower.append(element)
        else:
            tower.append((((i+1)*2)-1)*element)
    llargada = len(tower[-1])
    for a in tower:
        tower2.append(a.center(llargada,' '))
    
    return tower2

print(tower_builder(20))
