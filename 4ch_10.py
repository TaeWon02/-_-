maximum=0
for i in range(1, 100):
    if i*(100-i)>maximum:
        maximum=i*(100-i)
        max_i=i
print("최대가 되는 경우: {}*{}= ".format(max_i, max_i), maximum)
#2번 줄은 for i in range(1, 100//2+1)로 표시하는 것이 더 낫다.