def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")
output=test()#제너레이터 함수는 먼저 어떤 변수에 할당한다.
print("D 지점 통과")
a=next(output)#next()함수에, 제너레이터 함수가 할당된 변수를 할당한다.
print(a)
print("E 지점 통과")
b=next(output)
print(b)
c=next(output)
print(c)
next(output)#함수가 yield 키워드를 찾지 못하면 stopiteration 발생