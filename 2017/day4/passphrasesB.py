from itertools import permutations

def check(words):
    for word in words:
        if words.count(word) > 1:
            return False
        perms = set(permutations(word))
        for p in perms:
            s = ''
            for l in p:
                s = s + l
            if s in words and s != word:
                return False
    return True
data = open('input.txt','r')
count = 0
for line in data.readlines():
    line = line.replace('\n','')
    words = line.split(' ')
    if check(words):
        count = count + 1
print(count)