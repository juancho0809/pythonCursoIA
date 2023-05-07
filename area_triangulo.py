
import replit
from titulo import tituloTriangulo

def triangulo():
  try:
    opcion = 1
    while opcion == 1:
      tituloTriangulo()
      print("""
      Este programa calcula el área de un triángulo a partir de su base y su altura
      """)
      def atriangulo(base, altura):
        return (base * altura) / 2
      
      base = int(input("Digite la base: "))   
      while base < 1:
        print("Valor no valido, intentelo otra vez")
        base = int(input("Digite la base: "))
      altura = int(input("Digite la altura: "))
      while altura < 1:
        print("Valor no valido, intentelo otra vez")
        altura = int(input("Digite la base: "))
      
      print("El área del triangulo es ",atriangulo(base, altura))
      opcion = int(input(
        """¿Desea repetir el proceso?
        1) Si
        Otro numero) No
        """))
      if opcion == 1:
        replit.clear()
      
    print("Has salido de este proceso")
  except ValueError:
    print("¡¡Digito un valor que no es númerico, repita el proceso!!")
    input("Oprima Enter para repetir el proceso")
    replit.clear()
    triangulo()
    