from math import sqrt
def checkOpen(x,y):
    fav = 10
    z = x*x + 3*x + 2*x*y + y + y*y + fav
    binz = "{0:b}".format(z)
    bits = binz.count('1')
    if bits % 2 is 0:
        return '.'
    else:
        return '#'
def dist(x1,y1,x2,y2):
    x3 = x2-x1
    x3 = x3*x3
    y3 = y2-y1
    y3 = y3*y3
    return sqrt(x3+y3)
class Building():
    building = []
    x = 1
    y = 1
    w = 0
    h = 0
    def __init__(self,w,h):
        self.w = w
        self.h = h
        for y in range(h):
            row = []
            for x in range(w):
                row.append(checkOpen(x,y))
            self.building.append(row)

    def draw(self):
        head = '  '
        for x in range(self.w):
            head = head + "{0:0>2}".format(x)
        print(head)
        for x in range(self.h):
            row = "{0:0>2}".format(x)
            for ch in self.building[x]:
                row = row + '|' + ch
            print(row)
        print('\n\n')

    def step(self,x,y):
        self.building[y][x] = 'O'
        self.x = x
        self.y = y
        self.draw()

    def unstep(self,x,y):
        self.building[y][x] = checkOpen(x, y)

    def mark(self,x,y):
        self.building[y][x] = 'K'

    def canX(self,destX):
        pos = False
        neg = False
        if self.x > -1 and self.x < self.w + 1:
            if self.building[self.y][self.x + 1] == '.':
                pos = True
        if self.x > 0 and self.x < self.w - 1:
            if self.building[self.y][self.x - 1] == '.':
                neg = True
        if self.x > destX:
            if neg:
                return True,-1
            elif pos:
                return True,1
            else:
                return False,0
        elif self.x < destX:
            if pos:
                return True,1
            elif neg:
                return True,-1
            else:
                return False,0
        else:
            return False,0
    def canY(self,destY):
        pos = False
        neg = False
        if self.y > -1 and self.y < self.h + 1:
            if self.building[self.y + 1][self.x] == '.':
                pos = True
        if self.y > 0 and self.y < self.h - 1:
            if self.building[self.y - 1][self.x] == '.':
                neg = True
        if self.y > destY:
            if neg:
                return True,-1
            elif pos:
                return True,1
            else:
                return False,0
        elif self.y < destY:
            if pos:
                return True,1
            elif neg:
                return True,-1
            else:
                return False,0
        else:
            if pos:
                return True,1
            elif neg:
                return True,-1
            else:
                return False,0

    def goToEnd(self,z,dirt,step):
        end = False
        count = 0
        if dirt:
            row = self.building[self.y]
            i = self.x
            while i is not z and not end:
                ch = row[i]
                if ch == '#' or i is 0 or i is self.w-1:
                    end = True
                else:
                    count = count + 1
                if step > 0:
                    i = i + 1
                else:
                    i = i -1
        else:
            i = self.y
            while i is not z and not end:
                row = self.building[i]
                ch = row[self.x]
                if ch == '#' or i is 0 or i is self.h-1:
                    end = True
                else:
                    count = count + 1
                if step > 0:
                    i = i + 1
                else:
                    i = i - 1
        return count

    def choose(self,destX,destY):
        countXP = self.goToEnd(destX, True, 1)
        countXN = self.goToEnd(destX, True, -1)
        countYP = self.goToEnd(destY, False, 1)
        countYN = self.goToEnd(destY, False, -1)
        distXP = dist(self.x+countXP, self.y, destX, destY)
        distXN = dist(self.x-countXN, self.y, destX, destY)
        distYP = dist(self.x, self.y+countYP, destX, destY)
        distYN = dist(self.x, self.y-countYN, destX, destY)
        distX = 0
        distY = 0
        countX = 0
        countY = 0
        if countXN > countXP:
            countX = countXN
            distX = distXN
        elif countXN < countXP:
            countX = countXP
            distX = distXP
        elif distXN < distXP:
            countX = countXN
            distX = distXN
        else:
            countX = countXP
            distX = distXP
        if countYN > countYP:
            countY = countYN
            distY = distYN
        elif countYN < countYP:
            countY = countYP
            distY = distYP
        elif distYN < distYP:
            countY = countYN
            distY = distYN
        else:
            countY = countYP
            distY = distYP
        print('CountX: ' + str(countX))
        print('CountY: ' + str(countY))
        if countX > countY:
            return True
        elif countX < countY:
            return False
        elif distX < distY:
            return True
        else:
            return False

    def route(self,destX,destY):
        x = self.x
        y = self.y
        coords = {}
        path = []
        steps = 0
        self.mark(destX, destY)
        self.step(x, y)
        while (x is not destX or y is not destY):# and steps < 25:
            canX, dirX = self.canX(destX)
            canY, dirY = self.canY(destY)
            if canX and canY:
                if self.choose(destX,destY):
                    x = x + dirX
                else:
                    y = y + dirY
            elif y is not destY and canY:
                y = y + dirY
            elif x is not destX and canX:
                x = x + dirX
            elif x is not destX and canY:
                y = y + dirY
            elif y is not destY and canX:
                x = x + dirX
            coor = str(x) + ',' + str(y)
            if coor not in coords.keys():
                steps = steps + 1
                coords[coor] = steps
                path.append((x,y))
            else:
                steps = coords[coor]
                z = path.index((x,y))
                for z in range(z,len(path)):
                    px,py = path[z]
                    self.unstep(px, py)
            print('Step ' + str(steps))
            self.step(x, y)
            x = self.x
            y = self.y
        print('Step ' + str(steps))



building = Building(40,40)
building.draw()
building.route(31, 39)
