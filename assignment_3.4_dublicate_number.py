#WAP to remove dublicate elements from list
# using set

"""l = [22,34,43,54,22,34,55,54]
print("orignal list")
print(l)

n = set(l)
print("new list")
print(n)"""

l = [22,34,43,54,22,34,55,54]

print("orignal list")
print(l)
n = []

for i in l:
    if i not in n:
        n.append(i)
print("new list without dublicate elements")
print(n)



