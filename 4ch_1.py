numbers=[273, 103, 5, 32, 65, 9, 72, 800, 90]
for number in numbers:
    if number%2==0:
        print("{}은 짝수입니다.".format(number))
    else:
        print("{}은 홀수입니다.".format(number))
    if len(str(number))==1:
        print("{}은 1 자릿수입니다.".format(number))
    elif len(str(number))==2:
        print("{}은 2 자릿수입니다.".format(number))
    else:
        print("{}은 3 자릿수입니다.".format(number))