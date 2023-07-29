def 하노이(x):
    
x=int(input("원판의 개수를 입력하세요: "))
if x==1:
    print("{}탑->{}탑".format("A", "B"))
if x>=2:
