for i in range(10):
    print("*"*i)
print()
output=""
for i in range(1, 10):
    for j in range(0, i):
        output+="*"
    output+="\n"
print(output)