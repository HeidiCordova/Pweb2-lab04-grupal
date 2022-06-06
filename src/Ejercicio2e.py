from interpreter import draw
from chessPictures import *
#crear un patron
negativo= square.negative()
unir= negativo.join(square)
#repetir el patron
draw(unir.horizontalRepeat(3))
