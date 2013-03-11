
def issquare(n):
    if int(n ** (0.5)) * int(n ** (0.5)) == int(n):
        return True
    else:
        return False

a = 2
b = 499

while a < 500:
    while a+b < 1000 and b<500:
        if issquare(a ** (2) + b ** (2)):
            c = (a ** (2) + b ** (2)) ** (0.5)
            if a + b + c == 1000:
                product = a * b * c
        b = b+1
    a = a+1
    b = 501-a

print 'product is '+str(product)



