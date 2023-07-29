import datetime
now=datetime.datetime.now()
question=input("인삿말 입력: ")
if question=="안녕"\
    or question=="안녕하세요":
    print("안녕하세요.")
elif question=="지금 몇 시야?"\
    or question=="지금 몇 시예요?":
    print("지금은 {}시입니다.".format(now.hour))
else:
    print("{}".format(question))
