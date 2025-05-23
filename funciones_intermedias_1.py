#Ejercicio realizado por Andrea Correa
#funciones Intermedias(Core)
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
#Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
matriz[1][0]= 6

print(matriz)
print()
#Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”

cantantes[0]["nombre"] = "Enrique Martin Morales"

print(cantantes)
print()
#En ciudades, cambia “Cancún” por “Monterrey”

ciudades["México"][2]= "Monterrey"
print(ciudades)
print()
#En las coordenadas, cambia el valor de “latitud” por 9.9355431

coordenadas[0]["latitud"]= 9.9355431

print(coordenadas)
print()
# Iterar a través de una lista de diccionarios

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario(lista):
    for personaje in lista:
        linea = ""
        for name, nacion in personaje.items():
            linea += name + " - "+ str(nacion) + ","
        print(linea.rstrip(", "))

iterarDiccionario(cantantes)
print()
#Obtener valores de una lista de diccionarios

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])
        

iterarDiccionario2("nombre",cantantes)
iterarDiccionario2("pais", cantantes)
print()
#Iterar a través de un diccionario con valores de lista

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    for palabra in diccionario:
            lista= diccionario[palabra]
            cantidad= len(lista)
            print(str(cantidad)+ " "+ palabra)
            for elemento in lista:
                 print(elemento)
            print()


imprimirInformacion(costa_rica)

