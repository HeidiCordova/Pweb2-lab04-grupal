from interpreter import draw
from chessPictures import *
primero = knight.negative()
lin1 = knight.join(primero)
lin2 = primero.join(knight)
tercero = lin1.up(lin2)
draw(tercero)
