#모듈로 소수 찾기
from primePy import primes
to100primes=primes.upto(1000)
to10primes=primes.upto(100)
output=list(set(to100primes)-set(to10primes))
output.sort()
print(output, len(output), "개")