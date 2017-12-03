inp = open('day9.txt','r')
inp = list(inp.read().replace('\n',''))
print(len(inp))
index = 0
while index < len(inp):
    ch = inp[index]
    if ch is '(':
        start = index
        end = inp.index(')',index)
        tmp = inp[index+1:end]
        #print(tmp)
        i = tmp.index('x')
        ls = tmp[:i]
        l = ''
        for s in ls:
            l = l + str(s)
        l = int(l)
        ts = tmp[i+1:]
        t = ''
        for s in ts:
            t = t + str(s)
        t = int(t)
        tmp = inp[end+1:end+1+l]
        tmp.reverse()
        for x in range(start,end+1+l):
            del inp[start]
        for x in range(t):
                for c in tmp:
                    inp.insert(start,c)
        #print(inp)
        #index = start + (l*t)
    else:
        index = index + 1
    #print(index)
print(len(inp))
