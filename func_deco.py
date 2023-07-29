#함수데코레이터 생성
def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    return wrapper
#굳이 test안에 wrapper를 넣어서 return시킬 필요가 있나
@test
def hello():
    print("hello")
hello()
test(hello)