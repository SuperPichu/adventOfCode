inp = open('day6.txt','r')
columns = ['','','','','','','','']
for line in inp:
    line = line.replace(' ','')
    line = line.replace('\n', '')
    x = 0
    for ch in line:
        columns[x] = columns[x] + ch
        x = x + 1
print(columns)
final = ''
for column in columns:
    counts = {}
    for ch in column:
        if ch in counts:
            counts[ch] = counts[ch] + 1
        else:
            counts[ch] = 1
    sortedCounts = sorted(counts.items(), key=lambda x: (-x[1], x[0]), reverse=True)
    print(sortedCounts)
    final = final + sortedCounts[0][0]
print(final)
