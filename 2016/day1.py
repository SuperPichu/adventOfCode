puzzle = 'R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5'
import turtle as tur
#wn = tur.Screen()
turtle = tur.Turtle()
turtle.speed(0)
turtle.left(90)
startX = turtle.xcor()
startY = turtle.ycor()
print('Start: ' + str(startX) + ', ' + str(startY))
turtle.pd()
positions = []
for instruct in puzzle.split(', '):
    direction = instruct[:1]
    length = int(instruct[1:])
    if direction == 'R':
        turtle.right(90)
    elif direction == 'L':
        turtle.left(90)
    x = 0
    while x < length:
        turtle.fd(1)
        pos = turtle.pos()
        if pos not in positions:
            positions.append(pos)
        else:
            print('Second time')
            secondX = turtle.xcor()
            secondY = turtle.ycor()
            print('Second: ' + str(secondX) + ', ' + str(secondY))
            dist = abs(startX - secondX) + abs(startY - secondY)
            print(dist)
        x = x + 1
endX = turtle.xcor()
endY = turtle.ycor()
print('End: ' + str(endX) + ', ' + str(endY))
dist = abs(startX - endX) + abs(startY - endY)
print(dist)
