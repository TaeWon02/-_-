dna=input("염기 서열을 입력해주세요: ")
ATGC={
    "a":0,
    "t":0,
    "g":0,
    "c":0
}#딕셔너리의 키에 대응되는 값들을 0으로 초기화시켜야 한다.
for i in dna:
    ATGC[i]+=1
for j in ATGC:
    print(f"{j}의 개수: {ATGC[j]}")