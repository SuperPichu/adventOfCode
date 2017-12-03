data = open('input.txt','r').readlines()
add = []

for line in data:
    lineList = []
    for n in line.replace('\n','').split('\t'):
        lineList.append(int(n))
    for a in lineList:
        for b in lineList:
            x = a % b
            if x is 0 and a is not b:
                add.append(a//b)
print(sum(add))
