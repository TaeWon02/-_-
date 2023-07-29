numbers=[1,2,4,5,2,3,5,1,2,1,5,2,7,8,2,9]
counter={}
for number in numbers:
    if number in counter:
        counter[number]+=1
    else:
        counter[number]=1
print(counter)