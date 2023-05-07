import replit
from area_triangulo import triangulo
from ordenarnumeros import ordenarnumero
from numeroeuler import euler
from interesimple import interes
from vectores import calculadora_vector
from mrua import movimientoacelerado
from titulo import tituloMenu




def opciones():
  x=0
  while x==0:
    
    def printer():
      tituloMenu()
      print("""
      Que procesa desea realizar?
      1) Area de un triangulo
      2) Ordenar Numeros
      3) Número Euler
      4) Interes Simple
      5) Vectores
      6) MRUA
      7) Salir del sistema
      """)
    printer()
    opcion = int(input("¿Qué proceso desea realizar?  "))
      
    if opcion == 1:
      replit.clear()
      
      triangulo()
      replit.clear()
      
    elif opcion == 2:

      replit.clear()
      
      ordenarnumero()
      replit.clear()
    
    elif opcion == 3:
      replit.clear()
      
      euler()
      replit.clear()
    
    elif opcion == 4:
      replit.clear()
      
      interes()
      replit.clear()
    elif opcion == 5:
      replit.clear()
      
      calculadora_vector()
      replit.clear()
    elif opcion == 6:
      replit.clear()
      
      movimientoacelerado()
      replit.clear()
    elif opcion == 7:
      x =1
    else: 
      input("Escoje una opción valida")
      replit.clear()
    
  print("Has salido!!!")
  
if __name__ == ('__main__'):
  opciones()