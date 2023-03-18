print("A) Una persona enferma, que pesa 70 kg, se encuentra en reposo y desea saber cuántas calorías consume su cuerpo durante todo el tiempo que realice una misma actividad.")
print("Las actividades que tiene permitido realizar son únicamente dormir o estar sentado en reposo. Los datos que tiene son que estando dormido consume 1.08 calorías por minuto")
print("y estando sentado en reposo consume 1.66 calorías por minuto. Determinar cuántas calorías perdería durante la semana.")
print(" ")

# Datos del problema
peso = 70  # kg
calorias_dormido = 1.08  # calorías por minuto
calorias_reposo = 1.66  # calorías por minuto

# Calcular calorías por hora
calorias_dormido_hora = calorias_dormido * 60  # calorías por hora
calorias_reposo_hora = calorias_reposo * 60  # calorías por hora

# Calcular calorías por día
calorias_dormido_dia = calorias_dormido_hora * 24  # calorías por día
calorias_reposo_dia = calorias_reposo_hora * 24  # calorías por día

# Calcular calorías por semana
calorias_dormido_semana = calorias_dormido_dia * 7  # calorías por semana
calorias_reposo_semana = calorias_reposo_dia * 7  # calorías por semana

# Calcular calorías perdidas por semana
calorias_perdidas_semana = (calorias_dormido_semana + calorias_reposo_semana) * peso

# Imprimir resultado
print("La persona perdería", calorias_perdidas_semana, "calorías durante la semana.")

print(" ")
print(" ")
print("B) Hacer un script que imprima el nombre de un artículo, clave, precio original y su precio")
print("con descuento. El descuento lo hace en base a la clave, si la clave es 01 el descuento")
print("es del 10% y si la clave es 02 el descuento es de 20% (solo existen dos claves).")
print(" ")

articulos = [
    {"nombre": "Camisa", "clave": "01", "precio": 50.0},
    {"nombre": "Pantalón", "clave": "02", "precio": 80.0},
    {"nombre": "Chaqueta", "clave": "01", "precio": 120.0},
    {"nombre": "Poleron", "clave": "02", "precio": 20.0},
    {"nombre": "Gorro", "clave": "01", "precio": 40.0}
]

for articulo in articulos:
    nombre_articulo = articulo["nombre"]
    clave = articulo["clave"]
    precio_original = articulo["precio"]
    
    if clave == "01":
        descuento = precio_original * 0.1
    elif clave == "02":
        descuento = precio_original * 0.2
    else:
        descuento = 0
    
    precio_descuento = precio_original - descuento
    
    print("Nombre del artículo:", nombre_articulo)
    print("Clave:", clave)
    print("Precio original:", precio_original)
    print("Precio con descuento:", precio_descuento)
    print()

print(" ")
print("C) Hacer un script que calcule el total a pagar por la compra de camisas. Si se compran tres camisas o más se aplica un descuento del 20")
print(" ")

precio_camisa = 50
cantidad_camisas = int(input("¿Cuántas camisas desea comprar? "))

subtotal = precio_camisa * cantidad_camisas

if cantidad_camisas >= 3:
    descuento = subtotal * 0.2
else:
    descuento = 0

total = subtotal - descuento

print("El total a pagar es:", total)

print(" ")
print(" ")
print("D) Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume.")
print(" ")

numero1 = int(input("Indique un numero : "))
numero2 = int(input("Indique otro numero : "))

if numero1 == numero2:
    multi = numero1 * numero2
    print(multi)
elif numero1 > numero2 :
    resta = numero1 - numero2
    print(resta)
else  :
    sum = numero1 + numero2
    print(sum)
    
print(" ")
print(" ")
print("E) Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos.")  
print(" ")

import json

cantidad = int(input("¿Cuántas personas evaluará? : "))

resultados = []
for i in range(cantidad):
    sexo = input("Indique su sexo (H o M): ")
    edad = int(input("Indique su edad: "))
    resultados.append({"sexo": sexo, "edad": edad})

with open("alumnos.json", "w") as file:
    json.dump(resultados, file)

# Inicializar variables
edad_hombres = 0
edad_mujeres = 0
edad_total = 0
num_hombres = 0
num_mujeres = 0

# Calcular edades promedio
for resultado in resultados:
    if resultado["sexo"] == "H":
        edad_hombres += resultado["edad"]
        num_hombres += 1
    else:
        edad_mujeres += resultado["edad"]
        num_mujeres += 1
    edad_total += resultado["edad"]

if num_hombres > 0:
    promedio_hombres = edad_hombres / num_hombres
else:
    promedio_hombres = 0

if num_mujeres > 0:
    promedio_mujeres = edad_mujeres / num_mujeres
else:
    promedio_mujeres = 0

if cantidad > 0:
    promedio_total = edad_total / cantidad
else:
    promedio_total = 0

print("Promedio de edades de hombres:", promedio_hombres)
print("Promedio de edades de mujeres:", promedio_mujeres)
print("Promedio de edades de todo el grupo:", promedio_total)

        


