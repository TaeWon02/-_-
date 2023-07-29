numbers=[1, 2, [3, 4], 5, [6, 7], [8, 9]]
new_numbers=[]
for i in numbers:
    if type(i)!=list:
        new_numbers.append(i) #append는 딕셔너리, 리스트 모두 사용 가능
    else:
        for j in i:
            new_numbers.append(j)
print("\n".join([
      "{}를 평탄화하면",         #왜 줄바꿈이 적용되지 않지?->쉼표를 써야한다
      "{}입니다."
      ]).format(numbers, new_numbers))