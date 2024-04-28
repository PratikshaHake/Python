#List datatype

#Heterogeneous
#Ordererd
#Indexed
#Mutable
#Allows duplicate



Arr=[11,78.90,True,"Marvellous",11]

print("Length of lis is: ",len(Arr))
print(Arr[3])
print(Arr[0])
Arr[0]=21
print(Arr[0])

Arr.append(51)
print("Length of lis is: ",len(Arr))
print(Arr)

for i in Arr:
    print(i)