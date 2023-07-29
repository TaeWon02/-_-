from urllib import request as re
target=re.urlopen("https://google.com")
output=target.read()
print(output)