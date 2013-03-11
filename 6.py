n = 100
sofsum = (n*n*(n+1)*(n+1))/4
squares = 0
i = 1
while i < n+1:
    squares = squares + i*i
    i = i + 1
print sofsum - squares

