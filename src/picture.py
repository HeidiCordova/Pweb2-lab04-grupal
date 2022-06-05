
from colors import *


class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen """
        vertical = []
        for value in self.img:
            vertical.append(value[::-1])
        return vertical

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        return Picture(None)

    def negative(self):
        """ Devuelve un negativo de la imagen """
        return Picture(None)

    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento 
            al lado derecho de la figura actual """
        return Picture(None)

    def up(self, p):
        # Utilizamos listas por comprensión para añadir las figuras
        newPicture = [line for line in p.img]
        # Utilizamos el operador += para añadir las segunda figura también por listas por comprensión
        newPicture += [line for line in self.img]
        # Retornamos la nueva figura
        return Picture(newPicture)

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p sobre la
            figura actual """
        newPicture = []
        # Recorremos las filas de la figura p (argumento - va encima)
        for i in range(len(p.img)):
            tempLine = ""
            # Recorremos cada caracter de la fila
            for j in range(len(p.img[i])):
                if p.img[i][j] != " ":  # Si el caracter no es un espacio
                    # Añadimos el caracter a la nueva fila
                    tempLine += p.img[i][j]
                else:  # Si el caracter es un espacio
                    # Añadimos el caracter de la figura actual (la que irá detrás)
                    tempLine += self.img[i][j]
            # Añadimos la nueva fila a la nueva figura
            newPicture.append(tempLine)
        return Picture(newPicture)

    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado
            la cantidad de veces que indique el valor de n """
        return Picture(None)

    def verticalRepeat(self, n):
        vertical = []
        for value in self.img:
            vertical.append(value[::-1])
        return vertical*n
    # Extra: Sólo para realmente viciosos

    def rotate(self):
        """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
        o antihorario"""
        return Picture(None)
