from interpreter import draw
from chessPictures import *
primero = knight.join(knight.negative())
segundo = knight.negative().join(knight)
draw(segundo.up(primero))
