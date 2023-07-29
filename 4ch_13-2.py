dna=input("염기 서열을 입력해주세요: ")
ATGC={}
for i in dna:
    if i not in ATGC:
        ATGC[i]=0
    ATGC[i]+=1
for j in ATGC:
    print(f"{j}의 개수: {ATGC[j]}")