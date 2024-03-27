# Escritura de Archivo de Texto
with open("my_notes.txt", "w") as file:
    # Escribe al menos tres líneas de notas personales en el archivo
    file.write("Nota 1: Mi nombre es Edinson.\n")
    file.write("Nota 2: Me gusta ver peliculas.\n")
    file.write("Nota 3: Espero poder graduarme en esta especialidad.\n")
# Lectura de Archivo de Texto
with open("my_notes.txt", "r") as file:
    # Lee el contenido del archivo línea por línea utilizando el método adecuado
    for line in file.readlines():
        # Muestra en la consola cada línea leída
        print(line.strip())  # strip() elimina los caracteres de nueva línea (\n)
# Cierre de Archivos
# El archivo se cierra automáticamente al salir del bloque "with", no es necesario cerrarlo explícitamente
