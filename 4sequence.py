def palindrome(x):
    y = len(str(x))/2
    return x[len(x)-y:len(x)][::-1] == x[0:y]

"""
x = 999
i = 0
while i < 2:
    print x
    i = i + 1
"""

x = 999
j = 1
while j < 5:
    i = 0
    while i < 2:
        print x
        k = 1
        while k < j:
            x = x + 1
            print x
            k = k + 1
        i = i + 1
    x = x - j
    j = j + 1

