n = 2 ** (1000)
i = 0
sum = 0
while i < len(str(n)):
    sum = sum + int(str(n)[i])
    i = i+1

print sum

