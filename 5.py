j = 2
k = 1
while j < 21:
    if k % j != 0:
        i = 2
        fresult = k
        factor = j
        while i < j:
            while factor % i == 0 and fresult % i == 0:
                factor = factor / i
                fresult = fresult / i
            i = i + 1
        k = k * factor
    j = j+1
print k