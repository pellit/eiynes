import math as m
import turtle


class Circle:
    PI = m.pi
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        # area = self.PI * (self.radius ** 2)
        return round(self.PI * (self.radius ** 2),2)
    
    def perimetro(self):
        return round(2 * self.PI * self.radius,2)
    
    def draw(self):
        t = turtle.Turtle()
        t.circle(r)
        turtle.done()
        
    def circle_draw_pattern(self):
        row = int(input("Enter the number of rows: "))
        col= int(input("Enter the number of columns: "))
        for i in range(0,row):
            for j in range(0,col):
                if((j == 0 or j == col-1) and (i!=0 and i!=row-1)) :
                    print('*',end='')   #end='' so that print statement should not change the line.
                elif( ((i==0 or i==row-1) and (j>0 and j<col-1))):
                    print('*',end='')
                else:
                    print(end=' ')  #to print the space.
            print()  #to change the line after iteration of inner loop.
            
        
while True:      

    r = int(input("Ingrese el radio: "))
    r = float(r)

    try:
        if r < 0:
            raise ValueError
        else :
            circle_instance = Circle(r)
            print(circle_instance.area())
            print(circle_instance.perimetro())
            # circle_instance.draw()
            # circle_instance.circle_draw_pattern()
            escala = input("Desea escalar el circulo n veces su radio (s/n)?: ")
            if escala == 's':
                n = input("Ingrese factor de escala n: ")
                rNew = r * float(n)
                print(str(r) + " * " + str(n) + " = " + str(rNew))
                circle_instance = Circle(rNew)
                print(circle_instance.area())
                print(circle_instance.perimetro())
                # circle_instance.draw()
                # circle_instance.circle_draw_pattern()
                opcion = input("Desea ingresar un nuevo valor de radio (s/n)?: ")
                if opcion == 's':
                    continue
                else:
                    break
            else:
                break
        
        
        
    except ValueError:
            print("El radio debe ser mayor que cero")
    

       


