n = input("enter a name - ")
count = 0
print(f"vovels in string {n}:",end=' ')
for i in n:
    #print(i)
    if i in ['a','e','i','o','u']:
        count = count + 1
        print(i,end=' ')
print()
print("number of vowels :",count )

# write a program to print count of each vowel in a string
# eg - eleanora  a-2, e-2, o-1
