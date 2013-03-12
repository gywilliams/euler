'''
n -> n/2 (n is even)
n -> 3n+1 (n is odd)
Which starting number under one million produces the longest chain?
'''
i = 1
longX = []
length = 0
while i < 1000001:
    j = i
    X = []
    X.append(j)
    while j != 1:
        if j % 2 == 0:
            j = j/2
        else:
            j = 3*j+1
        X.append(j)
    if len(X) > length:
        longX = X
        length = len(X)
        print 'longest is '+str(longX[0])
    i = i + 1
