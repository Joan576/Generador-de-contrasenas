""""
--Generador de Contraseñas Seguras--

--Descripción: Un programa que genere contraseñas aleatorias seguras con la opción de personalización 
longitud, uso de mayúsculas, números, símbolos, etc.).

--Características:
Generación de contraseñas seguras con diferentes parámetros (longitud, caracteres especiales, etc.).
Guardado de contraseñas en una base de datos.
Cifrado de contraseñas.
Funcionalidades adicionales como la gestión de contraseñas (agregar, eliminar, ver).
"""

import secrets, string

from database import guardar_contraseña

#Funcion para generar contraseñas de manera aleatoria
def generar_contraseña (longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(secrets.choice(caracteres) for i in range(int(longitud)))
    return contraseña

# main.py

def main():
    #Bucle donde se le pide al usario la longitud de la contraseña
    while True:
        try:
            longitud = int(input ("¿Cuantos caracteres quieres que tenga la contraseña?: "))
            break
        except ValueError:
            print("Ingrese solo valores numericos.")


    while True:

        clave = input("Introduce 'H' para generar la contraseña: ")
        if clave.lower() == 'h':
            nueva_contraseña = generar_contraseña(longitud)
            print("La contraseña generada es:", nueva_contraseña)
            # Guardar la contraseña en la base de datos
            guardar_contraseña(nueva_contraseña)
            break
        else:
            print("Valor invalido, siga las intrucciones dadas.")


if __name__ == "__main__":
    main()




