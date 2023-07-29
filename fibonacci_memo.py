dictionary={
    1:1,
    2:1
}
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output=fibonacci(n-1)+fibonacci(n-2)
        dictionary[n]=output
        return output
print("fibonacci(50): ",fibonacci(50))
#한 번 계산한 값을 딕셔너리에 저장해서 계산량이 줄어든다.