import array as ar

a = ar.array('i', [1,3,5,7,9,10,15,20,14,18])
print(a)

even_list = []
odd_list = []
for x in a:
    if x%2==0:
        even_list.append(x)
    else:
        odd_list.append(x)

print("even list - ",even_list)
print("odd list - ",odd_list)


