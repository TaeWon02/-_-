import datetime
now=datetime.datetime.now()
print("#datetime.timedelta로 시간 더하기")
after=now+datetime.timedelta(\
    weeks=1,\
    days=1,\
    hours=1,\
    minutes=1,\
    seconds=1)#몇 년 후를 구하는 기능이 없다.
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}")\
.format(*"년월일시분초"))
print("#now.replace()로 1년 더하기")
output=now.replace(year=(now.year+1), day=(now.day+1)) #매개변수 추가 가능
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}")\
.format(*"년월일시분초"))#1년 후를 구할 때는 replace()함수를 사용해야한다.