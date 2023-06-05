from interpreter import draw
from chessPictures import *



image = square
for i in range(7):
    if (i%2 ==0):
        image = image.join(square.negative())
    else:
        image = image.join(square)


line = square 
for i in range(7):
    if (i%2 ==0):
        line = line.join(square.negative())
    else:
        line = line.join(square)



for a in range(3):
    if (a%2 ==0):
        image = image.up(line.horizontalMirror())
    else:
        image = image.up(line)
draw(image)





