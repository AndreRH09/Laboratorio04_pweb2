from interpreter import draw
from chessPictures import *



#fichas negras 
image = rock.negative()
image = image.setBackground(square)

pieces = [knight, bishop,queen,king,bishop,knight,rock]

print(len(pieces))

for i in range(len(pieces)):
    line = pieces[i]     
    line = line.negative()
    if (i%2 ==0):
        line = line.setBackground(square.negative())
    else:
        line = line.setBackground(square)
    image = image.join(line)

line = pawn.negative()
line = line.setBackground(square.negative())
for i in range(7):
    lineaux = pawn.negative()
    if (i%2 ==1):
        lineaux = lineaux.setBackground(square.negative())
    else:
        lineaux = lineaux.setBackground(square)
    line = line.join(lineaux)
image.up(line)

#casillas vacias
line = square.negative()
for i in range(7):
    if (i%2 ==1):
        line = line.join(square.negative())
    else:
        line = line.join(square)



for a in range(4):
    if (a%2 ==0):
        image = image.up(line.horizontalMirror())
    else:
        image = image.up(line)

#fichas blancas
line = pawn
line = line.setBackground(square)
for i in range(7):
    lineaux = pawn
    if (i%2 ==0):
        lineaux = lineaux.setBackground(square.negative())
    else:
        lineaux = lineaux.setBackground(square)
    line = line.join(lineaux)
image.up(line)



line =  rock
line = line.setBackground(square.negative()) 
for i in range(len(pieces)):
    lineaux = pieces[i]     
    if (i%2 ==1):
        lineaux = lineaux.setBackground(square.negative())
    else:
        lineaux = lineaux.setBackground(square)
    line = line.join(lineaux)

image.up(line)

draw(image)