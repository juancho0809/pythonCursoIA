import replit
import math
from titulo import tituloVectores

def calculadora_vector():
  try:
    class Vector:
        def __init__(self,x=0, y=0, z=0):
            
            self.x = x
            self.y = y
            self.z = z
        def __str__(self):
          return f'({self.x}i, {self.y}j, {self.z}k )'
    
        def __round__(self):
          return round()
    
      
        def suma(self, other):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
          
        def resta(self, other):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
          
        def producto_punto(self,other):
             return self.x * other.x + self.y * other.y + self.z * other.z
          
        def producto_cruz(self,other):
            return Vector(((self.y * other.z)-(other.y * self.z)),-((self.x * other.z)-(other.x * self.z)),((self.x * other.y)-(other.x * self.y)))
          
        def magnitud(self):
            cuadrado = lambda x: x ** 2
            x = cuadrado(self.x)+cuadrado(self.y)+cuadrado(self.z)
            return round(math.sqrt(x),2)       
            
        def unitario(self):
            aprox = lambda x: round(x,2)
            cuadrado = lambda x: x ** 2
            x = cuadrado(self.x)+cuadrado(self.y)+cuadrado(self.z)
            norma = round(math.sqrt(x),2)
            return Vector((aprox(self.x/norma)),(aprox(self.y/norma)),(aprox(self.z/norma)))
    
        def cosenos_vector(self):
            grados = lambda x: math.degrees(math.acos(x))
            aprox = lambda x: round(grados(x),2)
            cuadrado = lambda x: x ** 2
            x = cuadrado(self.x)+cuadrado(self.y)+cuadrado(self.z)
            norma = round(math.sqrt(x),2)
            return Vector((aprox(self.x/norma)),(aprox(self.y/norma)),(aprox(self.z/norma)))
            
    
    def menu():
      
      print("""
      Ahora que tenemos los vectores, que operación deseas implementar:
      1) Suma entre vectores
      2) Resta entre vectores
      3) Producto Punto entre vectores
      4) Producto Cruz entre vectores
      5) Sacar la magnitud del vector 1
      6) Sacar la magnitud del vector 2
      7) Sacar vector unitario del vector 1
      8) Sacar vector unitario del vector 2
      9) Sacar los cosenos del vector 1
      10) Sacar los cosenos del vector 2
      """)
    
    
    opcion = 1
    while opcion == 1:
      tituloVectores()
      input("""
      Este programa es una calculadora de 2 vectores R3, donde podrá sumar, restar, sacar producto punto, producto cruz entre esos dos vectores y magnitud, vector unitario y cosenos de cada vector 
      Oprima Enter para continuar
      """)
      print("""
      Vamos a darle valores a los vectores: 
      """)
      v1 = Vector(x=int(input("x vector 1: ")),y=int(input("y vector 1: ")), z=int(input("z vector 1: ")))
      
      v2 = Vector(x=int(input("x vector 2: ")),y=int(input("y vector 2: ")), z=int(input("z vector 2: ")))
      
      continuar = 1
      menu() #muestra opciones
      operacion = int(input("¿Que operacion desea realizar? "))
      while continuar == 1:
        while operacion < 1 or opcion > 10:
          print("Escoje una opción correcta ")
          replit.clear()
          tituloVectores()
          menu()
          print("sus valores del vector son: V1 =(",v1.x,v1.y,v1.z,") (",v2.x,v2.y,v2.z,")")
          operacion = int(input("¿Que operacion desea realizar? "))
          
        if operacion == 1:  
          v_sum = v1.suma(v2)
          print(f'La suma de {str(v1)}+{str(v2)}:{str(v_sum)}')
        elif operacion == 2:
          v_resta = v1.resta(v2)
          print(f'La resta de {str(v1)}-{str(v2)}:{str(v_resta)}')
        elif operacion == 3:  
          v_productopunto = v1.producto_punto(v2)
          print(f'El producto punto de {str(v1)}*{str(v2)}:{v_productopunto}')
        elif operacion == 4:
          v_productocruz = v1.producto_cruz(v2)
          print(f'La producto cruz de {str(v1)}-{str(v2)}:{str(v_productocruz)}')
        elif operacion == 5:
          v_magnitud = v1.magnitud()
          print(f'La magnitud de {str(v1)}:{v_magnitud}')
        elif operacion == 6:
          v2_magnitud = v2.magnitud()
          print(f'La magnitud de {str(v2)}:{v2_magnitud}')
        elif operacion == 7:
          v_unitario = v1.unitario()
          print(f'La magnitud de {str(v1)}:{v_unitario}')
        elif operacion == 8:
          v2_unitario = v2.unitario()
          print(f'La magnitud de {str(v2)}:{v2_unitario}')
        elif operacion == 9:
          v_cosenos = v1.cosenos_vector()
          print(f'Los cosenos de {str(v1)}:{v_cosenos}')
        elif operacion == 10:
          v2_cosenos = v2.cosenos_vector()
          print(f'Los cosenos de {str(v2)}:{v2_cosenos}')
        continuar = int(input("""
        ¿Desea hacer otro calculo con los vectores dados anteriormente?
        1) Si
        2) Cambiar los valores de los vectores
        3) Salir del sistema
        """))
        if continuar == 1:
          replit.clear()
          tituloVectores()
          menu()
          operacion = int(input("¿Que operacion desea realizar? "))
          
        elif continuar == 2:
          replit.clear()
          pass
        else:
          opcion = 2
    print("Has salido de la calculadora de vectores")      
  except ValueError:
    print("¡¡Digito un valor que no es númerico, repita el proceso!!")
    input("Oprima Enter para repetir el proceso")
    replit.clear()
    calculadora_vector()
  

  
  
  
  


  
