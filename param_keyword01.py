def print_n_times(*values, n=2):
    for i in range(n):
        #values는 리스트처럼 활용한다.
        #*values는 가변 매개변수, n은 기본 매개변수
        for value in values:
            print(value)
        print()
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)
        #n=3이라고 입력했을 때랑 그냥 3만 입력했을 때의 차이 확인