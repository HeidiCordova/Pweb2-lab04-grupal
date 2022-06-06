
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
    cambioHorizon = self.img
    listHorizon = []
    """Se cambio la imagen horizontalmente"""
    ultimo = len(self.img) - 1
    while (ultimo >= 0):
      listHorizon.append(cambioHorizon[ultimo])
      ultimo = ultimo - 1
      
    return Picture(listHorizon)
    

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negativo = []
    for x in range(len(self.img)):
      inv = ""
      """Se guardara cada elemento ya invertido"""
      for a in self.img[x]:
        inv += self._invColor(a)
      negativo.append(inv)

    return Picture(negativo)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    return Picture(None)

  def up(self, p):
    return Picture(None)

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
      newPicture = self.img
      i = 0
      while i < n:
          # usamos map para hacer que se repita cada string, por ejemplo si
          # la primera fila fuera " a ", ahora sería " a  a "
          newPicture = map(lambda x, y: x + y, newPicture, self.img)
          i += 1
      return Picture(list(newPicture))

  def verticalRepeat(self, n):
    vertical = []
    for value in self.img:
      vertical.append(value[::])
    return vertical * n
  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)
