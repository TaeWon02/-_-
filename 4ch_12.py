numbers=[1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
col=[]
counter={}
for number in numbers:
    if number not in col:
        col.append(number)
    if number in counter:
        counter[number]+=1
    else:
        counter[number]=1
print("\n".join([
    "사용된 숫자의 종류는 {}개입니다.",
    "참고: {}"
]).format(len(col), counter))

counter1={}
for i in numbers:
    if i not in counter1:
        counter1[i]=0
    counter1[i]+=1
print(
    f"{numbers}에서"
    f"사용된 숫자의 종류는 {len(counter1)}개입니다."
    )
print()
print(f"참고:{counter}")