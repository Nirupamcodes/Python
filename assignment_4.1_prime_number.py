num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   
   for i in range(2,num):
       if (num % i) == 0:
           print("prime number")
           break
   else:
       print("is a prime number")
       
else:
   print("not a prime number")