#Ejercicio realizado por Andrea Correa
#Ejercicios Listas, Tuplas y diccionarios (Core)
#1 Carga de Datos:

ventas = [
    {"fecha": "2004-01-01", "producto": "flores", "cantidad": "100", "precio":500.5},
    {"fecha": "2004-01-02", "producto": "maceteros", "cantidad": "50", "precio":650.5},
    {"fecha": "2004-01-03", "producto": "semillas", "cantidad": "80", "precio":350.5},
    {"fecha": "2004-01-04", "producto": "herramientas", "cantidad": "38", "precio":1255.5},
]

#2 Cálculo de Ingresos Totales:

ingresos_totale = 0.0
for venta in ventas:
    ingresos_totale += float(venta["cantidad"] )* venta["precio"]

print("Los ingresos totales son:", ingresos_totale)

#3 Análisis del Producto Más Vendido:


ventas_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    ingreso= venta["precio"]
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += float(cantidad) * ingreso
    else:
        ventas_por_producto[producto] = float(cantidad)  * ingreso
  
print(ventas_por_producto)   

mayor_producto = ""
mayor_cantidad = 0

for producto, cantidad in ventas_por_producto.items():
    if cantidad > mayor_cantidad:
        mayor_cantidad = cantidad
        mayor_producto = producto
print("Producto más vendido:", mayor_producto)
    
#Promedio de Precio por Producto:

precios_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = float(venta["cantidad"])
    total_precio = venta["precio"] * venta["cantidad"]
    
    
    if producto in precios_por_producto:
        precios_por_producto[producto][0] += total_precio
        precios_por_producto[producto][1] += cantidad
    else:
        precios_por_producto[producto] = [total_precio, cantidad]
    print(precios_por_producto)

# Calcular precio promedio
precios_promedio = {}

for producto, datos in precios_por_producto.items():
    suma_precios, total_cantidad = datos
    promedio = suma_precios / total_cantidad
    precios_promedio[producto] = promedio

print("el promedio de los precios es:" + str(precios_promedio))
