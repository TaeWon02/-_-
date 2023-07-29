def flatten(data):
    output=[]
    for item in data:
        if type(item)==list:
            output+=item
        else:
            output.append(item)
    return output
example=[[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본: ", example)
print("변환: ", flatten(example))
#2차원보다 큰 리스트에 대해서 평탄화가 이루어지지 않는다.