inp = open('day12.txt','r')
regs = [0,0,1,0]
con = {'a':0,'b':1,'c':2,'d':3}
instructions = []
for line in inp:
    line = line.replace('\n', '')
    instruction = {}
    lineSplit = line.split(' ')
    instruction['cmd'] = lineSplit[0]
    instruction['a'] = lineSplit[1]
    if len(lineSplit) > 2:
        instruction['b'] = lineSplit[2]
    instructions.append(instruction)
index = 0
while index < len(instructions):
    instruction = instructions[index]
    #print(instruction)
    jump = False
    if instruction['cmd'] == 'cpy':
        if instruction['a'].isdigit():
            regs[con[instruction['b']]] = int(instruction['a'])
        else:
            value  = regs[con[instruction['a']]]
            regs[con[instruction['b']]] = int(value)

    elif instruction['cmd'] == 'inc':
        regs[con[instruction['a']]] = regs[con[instruction['a']]] + 1

    elif instruction['cmd'] == 'dec':
        regs[con[instruction['a']]] = regs[con[instruction['a']]] - 1

    elif instruction['cmd'] == 'jnz':
        x = instruction['a']
        if x.isdigit():
            x = int(x)
        else:
            x = regs[con[instruction['a']]]
        if x is not 0:
            index = index + int(instruction['b'])
            jump = True

    if not jump:
        index = index + 1
print(regs)
