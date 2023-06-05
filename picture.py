from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

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
    newimg = []
    for cadena in self.img:
      line=''
      for charact in cadena:
        line = charact + line
      newimg.append(line)

    return Picture(newimg)

  def negative(self):
    negative = []
    # obtiene las cadenas del arreglo
    for cadena in self.img:
      line= ""
      # obtiene los caracteres de la cadena
      for char in cadena:
        # Ingresa el character inverso en una linea
        line = line+self._invColor(char)
      # Agrega el character inverso al nuevo arreglo que formara la img
      negative.append(line)
    return Picture(negative)

  def join(self, p):
    newimg = []
    for x in range (len(self.img)):
      newimg.append(self.img[x]+p.img[x])
    return Picture(newimg)

  def up(self, p):
    newimg = self.img
    for x in range (len(p.img)):
      newimg.append(p.img[x])
    return Picture(newimg)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)
