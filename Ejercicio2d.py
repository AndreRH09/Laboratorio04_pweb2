from interpreter import draw
from chessPictures import *


image = square

for i in range(7):
    if (i%2 ==0):
        image = image.join(square.negative())
    else:
        image = image.join(square)

draw(image)





