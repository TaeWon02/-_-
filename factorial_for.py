def fatorial(n):
    output=1
    for i in range(1, n+1):
        output*=i
    return output
print("5!: ", fatorial(5))
#재귀 함수로 팩토리얼 구하기
def factorial1(n):
    if n==0:
        return 1
    else:
        return n*factorial1(n-1)
print("5!: ", factorial1(5))