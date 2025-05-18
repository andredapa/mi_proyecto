#Ejercicio realizado por Andrea Correa
#funciones básicas 2

#1 Múltiples de 2
def multiplica_2(m):
    return [i * 2 for i in range (m + 1)]

print(multiplica_2(5))

#2 Suma y resta
def suma_y_resta(n):
    suma = n[0] + n[1]
    resta = n[0] - n[1]
    print (suma)
    return resta
resultado= suma_y_resta([5,4])

print
 
#3 Sumatoria menos longitud

def sumatoria(n):
    return sum(n) - len(n)

resultado= sumatoria([1, 2, 3, 4])
print(resultado)

#4 Valores multiplicados por el segundo

def multiplos(n):
    print(len(n))
    if len(n) < 2:
        return []
    p= n[1]
    m = [x * p for x in n]
    return m

print(multiplos([1, 3, 5, 7]))  
print(multiplos([1]))        


#5 Valor multiplado y longitud
def multi_longi(v, l):
    lista = [l * v]*l
    return lista
print(multi_longi(5, 2))
print(multi_longi(7, 5))