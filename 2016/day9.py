inp = open('day9t.txt','r')
inp = list(inp.read().replace('\n',''))
print(len(inp))
index = 0
while index < len(inp):
    ch = inp[index]
    if ch is '(':
        start = index
        end = inp.index(')',index)
        tmp = ''
        for c in inp[index+1:end]:
            tmp = tmp + str(c)
        #print(tmp)
        l, t = tmp.split('x')
        l = int(l)
        t = int(t)
        tmp = inp[end+1:end+1+l]
        for x in range(start,end+1+l):
            del inp[start]
            #print(inp)
        final = ''
        for x in range(t):
            for c in tmp:
                final = final + str(c)
        #print(final)
        final = list(final)
        final.reverse()
        for c in final:
            inp.insert(start,c)
        #print(inp)
        #index = start + (l*t)
    else:
        index = index + 1
    #print(index)
print(len(inp))
