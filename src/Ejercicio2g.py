from interpreter import draw
from chessPictures import *


def buildMainRow(isWhite):
    if isWhite:
        row = square.negative().under(rock)
        row = row.join(square.under(knight))
        row = row.join(square.negative().under(bishop))
        row = row.join(square.under(queen))
        row = row.join(square.negative().under(king))
        row = row.join(square.under(bishop))
        row = row.join(square.negative().under(knight))
        row = row.join(square.under(rock))
        return row
    else:
        row = square.under(rock.negative())
        row = row.join(square.negative().under(knight.negative()))
        row = row.join(square.under(bishop.negative()))
        row = row.join(square.negative().under(queen.negative()))
        row = row.join(square.under(king.negative()))
        row = row.join(square.negative().under(bishop.negative()))
        row = row.join(square.under(knight.negative()))
        row = row.join(square.negative().under(rock.negative()))
        return row


def buildPawnRow(isWhite):
    if isWhite:
        row = square.under(pawn)
        row = row.join(square.negative().under(pawn))
        row = row.join(square.under(pawn))
        row = row.join(square.negative().under(pawn))
        row = row.join(square.under(pawn))
        row = row.join(square.negative().under(pawn))
        row = row.join(square.under(pawn))
        row = row.join(square.negative().under(pawn))
        return row
    else:
        row = square.negative().under(pawn.negative())
        row = row.join(square.under(pawn.negative()))
        row = row.join(square.negative().under(pawn.negative()))
        row = row.join(square.under(pawn.negative()))
        row = row.join(square.negative().under(pawn.negative()))
        row = row.join(square.under(pawn.negative()))
        row = row.join(square.negative().under(pawn.negative()))
        row = row.join(square.under(pawn.negative()))
        return row


# Creando medio tablero vacio. La otra mitad se agregará ya con las piezas

row = square.join(square.negative()).horizontalRepeat(3)
rowInv = row.verticalMirror()
emptyBoard = rowInv.up(row).verticalRepeat(2)

# Creando filas principales para piezas blancas y negras

mainRowWhite = buildMainRow(True)
mainRowBlack = buildMainRow(False)

# Creando filas de peones para piezas blancas y negras

pawnRowWhite = buildPawnRow(True)
pawnRowBlack = buildPawnRow(False)

# Ensamblando el tablero

# Primero se ensambla la fila de peones y sus demás piezas para las piezas negras
blackPieces = pawnRowBlack.up(mainRowBlack)
# Luego se ensambla la fila de peones y sus demás piezas para las piezas blancas
whitePieces = mainRowWhite.up(pawnRowWhite)
# Ahora se pone las piezas negras encima en el top y las blancas al inferior
board = whitePieces.up(emptyBoard.up(blackPieces))

# Dibujando el tablero
draw(board)
