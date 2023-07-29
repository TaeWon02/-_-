array1=[]
for i in range(0, 20, 2):
    array1.append(i**2)
print(array1)
print()
array2=[i**2 for i in range(0, 20, 2)]
print(array2)