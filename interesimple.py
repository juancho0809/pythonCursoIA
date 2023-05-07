import replit
from titulo import intereSimple

def interes():
  try:
    def interes_iterativo(inicial, interes, tiempo):
      i =1
      for i in range(tiempo):
        final = inicial * (1+(interes/100)*(i+1))
        intereses = final - inicial
        
        print("- El capital final será de: ",round(final,1),", donde los intereses son de ",round(intereses,1), " en el mes ",i+1)
    
    def interes_recursivo(inicial,interes,tiempo):
      if tiempo == 0:
        pass
      else:   
        final = inicial * (1+(interes/100)*tiempo)
        intereses = final - inicial
        print("- El capital final será de: ",round(final,1),", donde los intereses son de ",round(intereses,1), " en el mes ",tiempo)
        return interes_recursivo(inicial,interes,tiempo-1)
    opcion = 1
    while opcion == 1:
      intereSimple()
      print(input("""
      Bienvenido al programa para calcular el interés simple de un año (por meses), por favor introduce los siguientes valores
      Oprima Enter para continuar
      """))
      
      inicial = int(input("Digite el capital inicial: "))
      while inicial < 1:
        print("Valor no valido, intentelo otra vez")
        inicial = int(input("Digite el capital inicial: "))
      interes = int(input("Digita el interés mensual, (solo el digito) "))
      while interes < 1:
        print("Valor no valido, intentelo otra vez")
        interes = int(input("Digite el capital inicial: "))
      tiempo = int(input("Introduce la cantidad de meses: "))
      while tiempo < 1:
        print("Valor no valido, intentelo otra vez")
        tiempo = int(input("Digite el capital inicial: "))
      print("""
      -----------------------------------
                    ITERATIVA
      -----------------------------------
      """)
      interes_iterativo(inicial,interes,tiempo)
      print("""
      -----------------------------------
                    RECURSIVA
      -----------------------------------
      """)
      interes_recursivo(inicial,interes,tiempo)
      opcion = int(input(
      """¿Desea repetir el proceso?
      1) Si
      Otro numero) No
      """))
      if opcion == 1:
        replit.clear()
      
    print("Has salido de este proceso")
  except:
    print("¡¡Digito un valor que no es númerico, repita el proceso!!")
    input("Oprima Enter para repetir el proceso")
    replit.clear()
    interes()
  