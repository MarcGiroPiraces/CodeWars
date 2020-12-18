"""Well met with Fibonacci bigger brother, AKA Tribonacci.

It works like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. 

So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this 
sequence:
[1, 1 ,1, 3, 5, 9, 17, 31, ...]

You need to create a fibonacci function that given a signature array/list, returns the first n elements, signature 
included of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty 
array (except in C return NULL) and be ready for anything else which is not clearly specified ;) """

""" def tribonacci(signature, n):
    
    llista = []
    iteracions = n - len(signature)
    a = signature[0]
    b = signature[1]
    c = signature[2]
    if n == 0:
        return llista
    elif n == 1:
        llista1 = [a]
        print(llista1)
        
    elif n == 2:
        llista2 = [a,b]
        print(llista2)
    elif n == 3:
        llista3 = [a,b,c]
        print(llista3)
    else:
        for i in range (0,iteracions):
            d = a + b + c
            llista.append(d)
            a = b
            b = c
            c = d
        llistaDefinitiva = signature + llista
        print (llistaDefinitiva)
signature = [1,1,1]
n = 4


tribonacci(signature,n) """


def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): 
      res.append(sum(res[-3:]))
  return res

signature = [1,2,1]
n = 10
print (tribonacci(signature,n))






