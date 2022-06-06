from interpreter import draw
from chessPictures import *
primero = knight.negative()
InverNegro = primero.verticalMirror()
InverBlanco = knight.verticalMirror()
lin1 = knight.join(primero)
lin2 = InverNegro.join(InverBlanco)
tercero = lin2.up(lin1)
draw(tercero)