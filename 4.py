def palindrome(x):
    y = len(str(x))/2
    return x[len(x)-y:len(x)][::-1] == x[0:y]

x = 999
y = 999
largest = 0
while x > 0:
    print 'x = '+str(x)
    while y > 0:
        print 'y = '+str(y)
        p = str(x*y)
        print 'x*y = '+p
        if palindrome(p) and x*y > largest:
            largest = x*y
            print 'largest = '+str(largest)
        y = y - 1
    x = x - 1
    y = x

print largest