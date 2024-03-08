import random
def calcular_temperatura_promedio(datos_temperaturas):
    temperaturas_promedio = {}
    for ciudad_index, ciudad in enumerate(ciudades):
        total_temperaturas_ciudad = 0
        for semana_index, semana in enumerate(semanas):
            total_temperaturas_ciudad += sum(datos_temperaturas[semana_index][ciudad_index])
        promedio_ciudad = total_temperaturas_ciudad / (len(semanas) * len(dias_semana))
        temperaturas_promedio[ciudad] = promedio_ciudad
    return temperaturas_promedio
# Definir las ciudades, días de la semana y semanas
ciudades = ['Guayaquil', 'Ambato', 'Quito']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = ['Semana 1', 'Semana 2', 'Semana 3']
# Generar datos aleatorios de temperaturas diarias para cada ciudad, día y semana
datos_temperaturas = [[[random.randint(20, 35) for _ in range(len(dias_semana))] for _ in range(len(ciudades))] for _ in range(len(semanas))]
# Calcular el promedio de temperaturas para cada ciudad y mostrar los resultados
resultado = calcular_temperatura_promedio(datos_temperaturas)
for ciudad, promedio in resultado.items():
    print(f"Promedio de temperaturas para {ciudad}: {promedio:.2f}°C")