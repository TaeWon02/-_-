def wrapper(function):
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
def hello():
        print("hello")
wrapper(hello)