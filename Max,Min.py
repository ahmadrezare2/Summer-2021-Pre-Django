list=[]
x1=int(input("Enter your first number: "))
x2=int(input("Enter your second number: "))
x3=int(input("Enter your third number: "))
list.append(x1),list.append((x2)),list.append((x3))
list.sort()
print("max is: ",list[-1])
print("min is: ",list[0])

