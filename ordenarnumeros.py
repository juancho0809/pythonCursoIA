import replit
from titulo import tituloOrdenamiento

def ordenarnumero():
  try:
    opcion = 1
    while opcion == 1:
      tituloOrdenamiento()
      print("""
      Este programa ordena los numeros de manera ascendente e imprime el menor y el mayor de la lista, se usa el algoritmo de burbuja
      """)
      listanumero = [] 
      n = int(input("Cuantos numeros quiere poner en el arreglo: "))
      while n < 1:
          print("Valor no valido, intentelo otra vez")
          n = int(input("Cuantos numeros quiere poner en el arreglo: "))  
      for i in range(n):
        i = int(input(f"Digita el número de la posición {i+1}: "))
        listanumero.append(i)
        
      for i in range(n):
          # Últimos i elementos ya están ordenados
          for j in range(0, n-i-1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
              if listanumero[j] > listanumero[j+1]:
                listanumero[j], listanumero[j+1] = listanumero[j+1], listanumero[j]
        
        
      print(listanumero)
      print(f"El número menor es: {listanumero[0]}")
      print(f"El número mayor es: {listanumero[-1]}")
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
    ordenarnumero()
    
  