data = open('input.txt','r')
count = 0
def check(words):
    for word in words:
        if words.count(word) > 1:
            return False
    return True

for line in data.readlines():
    line = line.replace('\n','')
    words = line.split(' ')
    if check(words):
        count = count + 1
print(count)
