"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in 
the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or 
special characters included in the string, they should be returned as they are. Only letters from the 
latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.

test.assert_equals(rot13("test"),"grfg")
test.assert_equals(rot13("Test"),"Grfg")
"""

def rot13(message):
    a = 'abcdefghijklmnopqrstuvwxyz'
    A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    finalMessage = ''
    
    for i in range(len(message)):
        if message[i] in a:
            if a.find(message[i])+13 >= len(a):
                sobra = a.find(message[i])+13-len(a)
                finalMessage += a[sobra]
            else:    
                finalMessage += a[a.find(message[i])+13]
        
        elif message[i] in A:
            if A.find(message[i])+13 >= len(A):
                sobra = A.find(message[i])+13-len(A)
                finalMessage += A[sobra]
            else:    
                finalMessage += A[A.find(message[i])+13]

        else:
            finalMessage += message[i]

    return finalMessage

print(rot13('n'))





