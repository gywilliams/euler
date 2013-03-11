#"""
def isprime(x):
    i = 3
    while i < x:
        if x % i == 0:
            return False
        i = i+1
    if x in (0,1):
        return False
    return True

j = 1
prime = 0
check = 1
while j < 10001:
    if isprime(check):
        prime = check
        j = j+1
        print str(check)+' is prime number '+str(j)
    check = check + 2
    print 'check is now '+str(check)
print prime
#runtime 2:08

"""
def isprime(x):
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i = i+1
    if x in (0,1):
        return False
    return True

j = 0
prime = 0
check = 0
while j < 10001:
    if isprime(check):
        prime = check
        j = j+1
        print str(check)+' is prime number '+str(j)
    check = check + 1
    print 'check is now '+str(check)
print prime
#runtime 2:12
"""