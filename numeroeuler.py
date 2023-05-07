import replit
from titulo import tituloEuler

def euler():
  try:
    def euler_recursiva(n):
        if n == 0:
            return 0
        else:
            return n / factorial(n) + euler_recursiva(n-1) #recursiva
    
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1) 
        
    def euler_iterativa(x):
        sumatoria = 0
        factorial = 1
        for i in range(1,x+1):
            factorial = i * factorial
            sumatoria = i/factorial + sumatoria
        return sumatoria 
      
    opcion = 1
    while opcion == 1:
      tituloEuler()
      print("""
      Este programa muestra el numero euler (e), donde entre más números digite, tendra una aproximación mayor a euler
      """)
      print("MANERA RECURSIVA")
      n = int(input("Ingrese el cuantos numeros quiere para aproximarse a euler: "))
      while n < 1:
        print("Valor no valido, intentelo otra vez")
        n = int(input("Ingrese el cuantos numeros quiere para aproximarse a euler: "))
      decimales = int(input("Ingrese la cantidad de decimales que desea: "))
      while decimales < 1:
        print("Valor no valido, intentelo otra vez")
        decimales = int(input("Ingrese la cantidad de decimales que desea: "))
      print("el número euler aproximado es: " , round(euler_recursiva(n),decimales))
      
      print("MANERA ITERATIVA")
      x = int(input("Ingrese el cuantos numeros quiere para aproximarse a euler: "))
      decimales = int(input("Ingrese la cantidad de decimales que desea: "))
      
      print("el número euler aproximado es: " , round(euler_iterativa(x),decimales))
      
      #En resumen, el resultado sera el mismo, la diferencia es su forma de procesar la información pero, al final de cuantas, tendran la misma aproximación
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
    euler()
  