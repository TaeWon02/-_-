from lambda03 import books
from operator import itemgetter
print("#가장 저렴한 책")
print(min(books, key=itemgetter("가격")))
print()
print("#가장 비싼 책")
print(max(books, key=itemgetter("가격")))