import math
#creamos la clase
class Punto:
    
    def _init_(self, x, y):
        self.x=x
        self.y=y

    def _str_(self):
        cadena = "(" + str(self.x) + "," + str(self.y) +")"
        return cadena
    
    def cuadrante(self):
        cuadrante = None
        if self.x > 0 and self.y > 0:
            cuadrante = 'Primer cuadrante'
        elif self.x > 0 and self.y < 0:
            cuadrante = 'Cuarto cuadrante'
        elif self.x < 0 and self.y > 0:
            cuadrante = 'Segundo cuadrante'
        elif self.x < 0 and self.y < 0:
            cuadrante = 'Tercer cuadrante'
        elif self.x == 0 and self.y != 0:
            cuadrante = 'Sobre el eje Y'
        elif self.x != 0 and self.y == 0:
            cuadrante = 'Sobre el eje X'
        elif self.x == 0 and self.y == 0:
            cuadrante = 'Punto de origen'
        return cuadrante