number=int(input("정수 입력>"))
if number%2==0:
    print("입력하신 정수는\
          {}입니다. {}는(은) 짝수입니다."\
          .format(number, number))
else:
    print("입력하신 정수는\
          {}입니다. {}는(은) 홀수입니다."\
          .format(number, number))
    #조건문의 자동 들여쓰기 때문에 출력에 공백이 생긴다

number=int(input("정수 입력>"))
if number%2==0:
    print((
        "입력하신 정수는"
        "{}입니다. {}는(은) 짝수입니다."
    ).format(number, number))
else:
    print((
        "입력하신 정수는"
        "{}입니다. {}는(은) 홀수입니다."
    ).format(number, number))
    #공백을 없앨 수 있다.