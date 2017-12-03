class Bot:
    value1 = None
    value2 = None
    highDest = None
    lowDest = None
    num = None
    def __str__(self):
        return 'value1: ' + str(self.value1) + ' value2: ' + str(self.value2)
    def give(self, value):
        if self.value1 is None:
            self.value1 = value
        elif self.value2 is None:
            self.value2 = value
    def high(self):
        value = None
        if self.value1 is None:
            value = self.value2
        elif self.value2 is None:
            value = self.value1
        elif self.value1 > self.value2:
            value = self.value1
            self.value1 = None
        else:
            value = self.value2
            self.value2 = None
        return value
    def low(self):
        value = None
        if self.value1 is None:
            value = self.value2
        elif self.value2 is None:
            value = self.value1
        elif self.value1 < self.value2:
            value = self.value1
            self.value1 = None
        else:
            value = self.value2
            self.value2 = None
        return value
    def canRun(self):
        if self.value1 is not None and self.value2 is not None:
            return True
        else:
            return False
    def values(self):
        values = []
        values.append(self.value1)
        values.append(self.value2)
        return values
    def set(self,num):
        self.num = num
inp = open('day10.txt','r')
bots = []
for x in range(209):
    bot = Bot()
    bots.append(bot)
outputs = [None] * 20
for line in inp:
    line = line.replace('\n','')
    if line.startswith('value'):
        value = int(line.split('value ')[1].split(' goes to')[0])
        botNum = int(line.split(' goes to bot ')[1])-1
        bots[botNum].give(value)
    else:
        botNum = int(line.split('bot ')[1].split(' gives')[0])-1
        bots[botNum].lowDest = line.split('gives low to ')[1].split(' and')[0]
        bots[botNum].highDest = line.split(' and high to ')[1]
while None in outputs:
    index = 0
    for bot in bots:
        if bot.canRun():
            print('running bot ' + str(index+1))
            if 'output' in bot.highDest:
                outputs[int(bot.highDest.split(' ')[1])-1] = bot.high()
            else:
                bots[int(bot.highDest.split(' ')[1])-1].give(bot.high())
            if 'output' in bot.lowDest:
                outputs[int(bot.lowDest.split(' ')[1])-1] = bot.low()
            else:
                bots[int(bot.lowDest.split(' ')[1])-1].give(bot.low())
        index = index + 1
        print(outputs)
        #print(bot.__str__() + ' index: ' + str(index))
