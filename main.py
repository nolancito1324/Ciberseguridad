# codigo para generar contraseñas seguras
import random
caracteres = "+-/*!&$#?=@abcdefghijklmnpqrstuvwxyzABCDEFGHIJKLMNNPQRSTUVWXYZ1234567890"

longitud = int(input("escribe la longitud de la contraseña"))
password = ""
for i in range(longitud):
    password += random.choice(caracteres)

print("tu contraseña segura es: ", password)