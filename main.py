#print("hola");
"""class persona:
    nombre = str 
    edad = int 
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad = edad
        
    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.'
if __name__== "__main__":
    persona1 = persona("David", 33)
    persona2 = persona("Elena", 35)
    
    print(persona1.saluda(persona2) )
    
class MiClase:
    nombre= "David"
    edad= int 
    
p1 = MiClase()
print(p1.nombre)

#Funcion __init__()

class persona2:
    nombre= "David"
    edad= int 
    genero=str 
    
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        
p2 = persona2("David", 29, "Masculino")

print(p2.nombre)
print(p2.edad)
print(p2.genero)

#Funcion __str___()

class persona3:
    nombre   = "David"
    edad     = int 
    genero   =str 
    estatura = int
    
    def __init__(self, nombre, edad, genero, estatura):
        self.nombre    = nombre
        self.edad      = edad        
        self.genero    = genero
        self.estatura  = estatura
        
    def __str__(self):
        return f'Hola me llamo'{self.nombre}, 'tengo '{self.edad}, 'mido '{self.estatura} 'cm'
    
p3 = persona3("Juan", 21, "Masculino", 189)

print(p3)

#Metodos dentro de objetos

class persona4:
    nombre    = str
    semestre  = str 
    
    def __init__(self, nombre, semestre):
        self.nombre   = nombre
        self.semestre = semestre
        
    def saludo(self):
        print("Bienvenido" +self.nombre+ "al"+ self.semestre)
        
p4 = persona4("Antonio", "Segundo")
p4.saludo()
 
 #cambiar atributos 
 
p4.nombre = "Jonathan"
p4.saludo()"""""

#del p4.semestre
#p4.saludo()

