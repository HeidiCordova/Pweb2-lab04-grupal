from interpreter import draw
from chessPictures import *

blacksquare = square.negative()
lin1 = square.join(blacksquare)
lin2 = lin1.horizontalRepeat(3)
draw(lin2)

