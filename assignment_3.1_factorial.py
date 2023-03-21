#n = (int(input("enter a number - ")))
"""num = 5
factorial = 1
for i in range(1,num + 1):
       factorial = factorial*i
print("The factorial of",num,"is",factorial)"""



def factorial(n):
    
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)
num = int(input("enter a number - "))
result = factorial(num)
print("the factorial of number is ")
print(result)
