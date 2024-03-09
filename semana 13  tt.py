def calcular_temperatura_promedio(datos):
    temperaturas_promedio_ciudades = {}
    for ciudad, semanas in datos.items():
        suma_temperaturas = 0
        total_dias = 0
        for semana, temperaturas in semanas.items():
            suma_temperaturas += sum(temperaturas)
            total_dias += len(temperaturas)
        temperatura_promedio = suma_temperaturas / total_dias
        temperaturas_promedio_ciudades[ciudad] = temperatura_promedio
    return temperaturas_promedio_ciudades
# Ejemplo de datos: temperaturas de 2 ciudades durante 4 semanas
datos = {
    'Shushufindi': {
        'Semana 1': [25, 26, 27, 28, 29, 30, 31],
        'Semana 2': [24, 25, 26, 27, 28, 29, 30],
        'Semana 3': [23, 24, 25, 26, 27, 28, 29],
        'Semana 4': [22, 23, 24, 25, 26, 27, 28],
    },
    'Lago Agrio': {
        'Semana 1': [28, 29, 30, 31, 32, 33, 34],
        'Semana 2': [27, 28, 29, 30, 31, 32, 33],
        'Semana 3': [26, 27, 28, 29, 30, 31, 32],
        'Semana 4': [25, 26, 27, 28, 29, 30, 31],
    }
}
# Calcula la temperatura promedio de cada ciudad
temperaturas_promedio = calcular_temperatura_promedio(datos)
# Imprime los resultados
for ciudad, temperatura_promedio in temperaturas_promedio.items():
    print(f'Temperatura promedio en {ciudad}: {temperatura_promedio:.2f}°C')