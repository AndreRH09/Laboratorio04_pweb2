from interpreter import draw
from chessPictures import *

line1 = knight.join(knight.negative())
line2 = knight.negative().join(knight)

img = line1.up(line2)
draw(img)