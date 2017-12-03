def rotate(l, n):
    return l[-n:] + l[:-n]
class Box:
    box = []
    width = 50
    height = 6
    def __init__(self):
        for x in range(self.height):
            row = []
            for x in range(self.width):
                row.append('.')
            self.box.append(row)

    def print(self):
        for row in self.box:
            st = ''
            for char in row:
                st = st + char
            print(st)
    def rect(self,l,w):
        for x in range(w):
            row = self.box[x]
            for y in range(l):
                row[y] = '#'
            self.box[x] = row
    def rotc(self,x,l):
        tmp = []
        for row in self.box:
            tmp.append(row[x])
        tmp = rotate(tmp, l)
        for i in range(len(self.box)):
            row = self.box[i]
            row[x] = tmp[i]
            self.box[i] = row
    def rotr(self,y,l):
        self.box[y] = rotate(self.box[y],l)
    def lit(self):
        count = 0
        for row in self.box:
            for char in row:
                if char is '#':
                    count = count + 1
        return count
box = Box()
# box.rect(3,2)
# box.print()
# print()
# box.rotc(1,1)
# box.print()
# print()
# box.rotr(0,4)
# box.print()
# print()
# box.rotc(1,1)
# box.print()
# print()
inp = open('day8.txt','r')
for line in inp:
    line = line.replace('\n', '')
    if line.startswith('rect'):
        line = line.split('rect ')[1]
        line = line.split('x')
        box.rect(int(line[0]), int(line[1]))
    elif 'row' in line:
        line = line.split('row ')[1]
        line = line.split(' by ')
        row = line[0]
        row = int(row.split('=')[1])
        leng = int(line[1])
        box.rotr(row,leng)
    elif 'column' in line:
        line = line.split('column ')[1]
        line = line.split(' by ')
        col = line[0]
        col = int(col.split('=')[1])
        leng = int(line[1])
        box.rotc(col,leng)
    box.print()
    print()
print(box.lit())
