output=""
for i in range(1, 15):
    for j in range(0, 14-i):
        output+=" "
    for k in range(1, 2*i-1+1):
        output+="*"
    output+="\n"
print(output)