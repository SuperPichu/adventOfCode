import ulamspiral

def find(i,spiral):
    y = 0
    for line in spiral.split('\n '):
        line = ' '.join(line.split())
        x = 0
        for n in line.split(' '):
            n = int(n)
            if n == i:
                return x+1,y+1
            x = x + 1
        y = y + 1
x = 300000
spiral = ulamspiral.UlamSpiral(x).show()
r = 0
ex,ey = find(289326,spiral)
sx,sy = find(1,spiral)
if sx > ex:
    r = r + sx - ex
else:
    r = r - sx + ex
if sy > ey:
    r = r + sy - ey
else:
    r = r - sy + ey
print(r)