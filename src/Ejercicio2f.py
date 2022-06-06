from interpreter import draw
from chessPictures import *

negativo= square.negative()

lin1= negativo.join(square)
lin2=square.join(negativo)
union= lin1.up(lin2)
union2 =union.horizontalRepeat(3)
draw(union2.verticalRepeat(2))
