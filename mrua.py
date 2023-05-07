import replit
from titulo import movimientoMRUA
def movimientoacelerado():
  try:
    class Movimiento:
      def __init__(self,velocidadInicial,aceleracion,tiempo):
        self.velocidadInicial = velocidadInicial
        self.aceleracion = aceleracion
        self.tiempo = tiempo
    def distancia(x,y,z):
      cuadrado = lambda x: x ** 2
      distancia = x * z + (0.5*y*cuadrado(z))
      return distancia
    def validaciontiempo(z):
      while z < 0:
        z = float(input("""!!!No hay tiempo negativo, digite un valor valido¡¡¡
        Digite el tiempo recorrido por el objeto: """))
      return z
      
    seguir = 1
    while seguir == 1:
      movimientoMRUA()
      print("""
      Este programa calcula la distancia que recorre un objeto con aceleración constante partiendo desde el reposo (posicion = 0) o con movimiento (velocidad inicial != 0)
    """)
      opcion = int(input("""
      ¿Como actua el objeto al cuál le desea calcular la distancia?
      1) Partiendo desde el reposo
      2) Partiendo con una velocidad inicial
      
      """))
     
      if opcion == 1:
        movimientoaux = Movimiento(0,float(input("Digite la aceleración: ")),float(input("Digite el tiempo recorrido por el objeto: ")))
        
        x =distancia(movimientoaux.velocidadInicial,movimientoaux.aceleracion, validaciontiempo(movimientoaux.tiempo))
        
        print("La distancia recorrida por el objeto es",round(x,2),"metros")
        seguir=int(input("""
          ¿Desea hacer otro calculo?
          1) Si
          Otro numero) No
        """))
        if seguir == 1:
          replit.clear()
      elif opcion == 2:
        movimientoaux = Movimiento(float(input("Digite la velocidad inicial: ")),float(input("Digite la aceleración: ")),float(input("Digite el tiempo recorrido por el objeto: ")))
        x = distancia(movimientoaux.velocidadInicial,movimientoaux.aceleracion, validaciontiempo(movimientoaux.tiempo))
        print("La distancia recorrida por el objeto es ",round(x,2),"metros")
        seguir=int(input("""
          ¿Desea hacer otro calculo?
          1) Si
          Otro numero) No
        """))
        if seguir == 1:
          replit.clear()
      while opcion < 1 or opcion > 2:
        
        replit.clear()
        print("Escogio una opción invalida")
        opcion = int(input("""¿Como actua el objeto al cuál le desea calcular la distancia?
      1) Partiendo desde el reposo
      2) Partiendo con una velocidad inicial
      
      """))
    print("Gracias por usar esta opción")    
  except ValueError:
    print("¡¡Digito un valor que no es númerico, repita el proceso!!")
    input("Oprima Enter para repetir el proceso")
    replit.clear()
    movimientoacelerado()