# Write a Menu driven program to insert,update,remove, 
#and access the array element in python

bikes = ["kawasaki","honda","yamaha","TVS","BMW"]
print(bikes)

print("1 - insert a element")
print("2 - update a element")
print("3 - remove a element")
print("4 - access a element")

num = int(input("enter your choice - "))

if num == 1:
    bikes.append("suzuki")
    print(bikes)

elif num == 2:
    bikes[0] = "suzuki"
    print(bikes)
    
elif num == 3:
    bikes.pop(0)
    print(bikes)

elif num == 4:
    print(bikes[0])

else :
    print("enter valid choice")