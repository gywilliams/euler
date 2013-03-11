def isprime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i+1
    return True

def nextprime(n):
    while not isprime(n+1):
        n = n+1
    return n+1

X = 600851475143
p = 2
while not isprime(X):
    if X % p == 0:
        X = X / p
    else:
        p = nextprime(p)
print X

X = 600851475143
i = 2
while X != 1:
    if X % i == 0:
        X = X / i
    else:
        i = i + 1
print i

