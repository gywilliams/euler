units = {1: 'one', 2: 'two', 3:'three', 4:'four', 5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
tens = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
hundreds = {100:'hundred'}
i = 123

def twod2text(n):
    l = len(str(n))
    if int(str(n)[l-2:l]) in tens:
        return tens[int(str(n)[l-2:l])]
    else:
        return tens[int(str(n)[l-2])*10]+units[int(str(n)[l-1])]

def threed2text(n):
    l = len(str(n))
    if str(n)[1:3] == '00':
        return units[int(str(n)[l-3])]+hundreds[100]
    elif str(n)[1] == '0':
        return units[int(str(n)[l-3])]+hundreds[100]+'and'+units[int(str(n)[l-1])]
    else:
        return units[int(str(n)[l-3])]+hundreds[100]+'and'+twod2text(n)

i = 1
length = 0
num = ''
while i < 10:
    num = units[i]
    length = length + len(num)
    i = i+1
    num = ''
while i < 100:
    num = twod2text(i)
    length = length + len(num)
    i = i + 1
    num = ''
while i < 1000:
    num = threed2text(i)
    length = length + len(num)
    i = i + 1
    num = ''
length = length + len('onethousand')
print length

