data = list(open('input.txt','r').read())[:-1]
add = []
step = int(len(data)/2)
for x in range(len(data)):
    y = x + step
    if not y < len(data):
        y = y - len(data)
        if data[x] is data[y]:
            add.append(int(data[x]))
            print(sum(add))
