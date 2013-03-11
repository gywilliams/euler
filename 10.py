n = 2
X = [2]

def isprime(n,X):
    i = 0
    while X[i] <= n ** (0.5) and i < len(X):
        if n % X[i] == 0:
            return False
        i = i+1
    return True


while X[len(X)-1]<2000000:
    if isprime(n,X) and X[len(X) -1 ] != n:
        X.append(n)
        n = n+1
    else:
        n = n+1

sum = 0
j = 0
while j < len(X)-1:
    sum = sum + int(X[j])
    j = j+1

print 'sum is '+str(sum)