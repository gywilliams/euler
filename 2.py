total = 0
l = 1
m = 2
while m < 4000000:
    if m % 2 == 0:
        total = m + total
    m = m + l
    l = m - l
print total