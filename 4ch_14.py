dna=input("염기 서열을 입력해주세요:")
codon={
    "cta":0,
    "caa":0,
    "tgt":0,
    "cag":0,
    "tat":0,
    "acc":0,
    "cat":0,
    "cgc":0,
    "att":0,
    "agc":0,
    "cgg":0
}
for i in range(0, len(dna), 3):
    codon[dna[i:i+3]]+=1
print(codon)
#아래는 정답지
nucleos=input("염기 서열을 입력해주세요: ")
counter={}
for i in range(0, len(nucleos), 3): #len 안에 있는 문자열을 알아서 인식 한듯
    codon=nucleos[i:i+3]
    if len(codon)==3:
        if codon not in counter:
            counter[codon]=0
        counter[codon]+=1
print(counter)