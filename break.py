i=0
while True:
    print("{}번째 반복입니다.".format(i))
    i+=1
    input_text=input("반복을 종료합니까?(y/n)")
    if input_text in ["Y", "y"]:
        print("반복을 종료합니다.")
        break