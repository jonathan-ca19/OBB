#Herencia en Python
class persona:
    nombre   = str 
    apellido = str
    
    def __init__(self, nombre, apellido):
        self.nombre    = nombre
        self.apellido  = apellido
        
        def imprimir(self):
            print(self.nombre, self.apellido)
            
x = persona("Alexander", "flores")
x.imprimir()

#

class estudiante(persona):
    pass 

y = estudiante("Jeremy", "Cañizares")
y.imprimir()

#agregar atributos o herencia

class estudiante(persona):
    edad = int
    
    def __init__(self, nombre, apellido, edad):
        persona.__init__(self, nombre, apellido)
        self.edad = edad 
        
estudiante1 = estudiante("Carlos", "Dell", 30)
estudiante1.imprimir()

#agregar metodos a una herencia 

class Student1(persona):
    edad     = int
    semestre = str
    
    def __init__(self, nombre, apellido, edad, semestre):
        super().__init__(nombre, apellido)
        self.edad = edad
        self.semestre = semestre
        
    def bienvenido(self):
        print("Bienvenido "+self.apellido+" al "+self.semestre+ " ingresas a los "+ str(self.edad)+"años")
        
p5= Student1("Jonathan", "Cañar", 29, "Segundo")
p5.bienvenido()