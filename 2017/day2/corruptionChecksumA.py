data = open('input.txt','r').readlines()
add = []

for line in data:
    lineList = []
    for n in line.replace('\n','').split('\t'):
        lineList.append(int(n))
    maximum = max(lineList)
    minimum = min(lineList)
    x = maximum - minimum
    add.append(x)
print(sum(add))    
