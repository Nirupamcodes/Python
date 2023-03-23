import array as ar
n = ar.array('i',[4,5,8,64,54,24])
sum = 0
for i in n:
    if i % 2 == 0:
        sum = sum+i
print(sum)