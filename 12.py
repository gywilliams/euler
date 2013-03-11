def issquare(n):
    if n == int(n ** (0.5)) * int(n ** (0.5)):
        return True
    else:
        return False
def countfactors(n):
    i = 1
    nfactors = 0
    while i < n ** (0.5):
        if n % i == 0:
            nfactors = nfactors + 1
        i = i + 1
    if issquare(n):
        return nfactors*2 + 1
    else:
        return nfactors*2
print countfactors (76564125)
i = 1
triangle = 0
triangle = triangle + i
while countfactors(triangle) < 502:
    #    print 'triangle is '+str(triangle)
    i = i + 1
    triangle = triangle + i
#    print 'i is '+str(i)
print triangle


