# Write a program to print the element in array,
# divisible by 5 and 3 a = [15, 55 ,30, 65 ,75,33,120]

a = [15, 55 ,30, 65 ,75,33,120]
print("array list - ",a)
count = 0
print("divisible by 3 - ")

while (count<=6) :
    if a[count] % 3 == 0:
        print(a[count],end=',')
    count = count + 1
counts = 0

print(" ")
print("divisible by 5 - ")
while (counts<=6) :
    if a[counts] % 5 == 0:
        print(a[counts],end=',')
    counts = counts + 1



    


