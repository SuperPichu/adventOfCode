data = list(open('input.txt','r').read())[:-1]
add = []
if data[0] is data[len(data)-1]:
    add.append(int(data[0]))
for x in range(len(data)-1):
    if data[x] is data[x+1]:
        add.append(int(data[x]))
print(sum(add))
