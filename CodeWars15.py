# Break camelCase

"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
solution("camelCasing")  ==  "camel Casing"

Sample Tests:

1. Test.assert_equals(solution("helloWorld"), "hello World")

2. Test.assert_equals(solution("camelCase"), "camel Case")

3. Test.assert_equals(solution("breakCamelCase"), "break Camel Case")
"""


def solution(s):
    paraula = ''
    for a in s:
        if a.isupper():
            paraula += ' ' + a 
        else:
            paraula += a
    return paraula


print(solution('helloWorld'))
