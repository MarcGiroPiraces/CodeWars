

""" def solution(string):
    novaParaula = []
    recompte = -1
    for i in range(len(string)):
        novaParaula.append(string[recompte])
        recompte = recompte - 1
    
    paraulaFinal=''.join(novaParaula)
    print(paraulaFinal)
string = 'hello'

solution(string) """


def solution(string):
    llista = []
    for lletres in range(len(string)):
        llista.append(string[lletres])
    llista.reverse()
    paraulaFinal = ''.join(llista)
    print(paraulaFinal)
string = 'hello'
solution(string)
