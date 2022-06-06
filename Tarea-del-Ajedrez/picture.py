
from colors import *

class Picture:
  def _init_(self, img):
    self.img = img

  def _eq_(self, other):
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
    fig1_self=[]
    fig2_p=[]
    for value1 in self.img:
      fig1_self.append(value1[::])
    for value2 in p.img:
      fig2_p.append(value2[::])

    figTotal = []
    for i in range(len(p.img)):
      figTotal.append(fig1_self[i]+fig2_p[i])
      
    return figTotal

  def up(self, p):
    return Picture(None)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    vertical = []
    for value in self.img:
      vertical.append(value[::-1])
    return vertical*n
  
  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)
