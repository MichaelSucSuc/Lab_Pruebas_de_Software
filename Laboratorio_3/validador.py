# validador.py

def validar_contrasena(contrasena: str) -> dict:
    """
    Evalúa la fortaleza de una contraseña según:
    - Longitud >= 8
    - Al menos una mayúscula
    - Al menos una minúscula
    - Al menos un dígito
    - Al menos un carácter especial: ! @ # $ % ^ & *
    """
    errores = []

    if len(contrasena) < 8:
        errores.append("La contraseña debe tener al menos 8 caracteres.")

    if not any(c.isupper() for c in contrasena):
        errores.append("La contraseña debe contener al menos una letra mayúscula.")

    if not any(c.islower() for c in contrasena):
        errores.append("La contraseña debe contener al menos una letra minúscula.")

    if not any(c.isdigit() for c in contrasena):
        errores.append("La contraseña debe contener al menos un dígito numérico.")

    especiales = "!@#$%^&*"
    if not any(c in especiales for c in contrasena):
        errores.append("La contraseña debe contener al menos un carácter especial (!@#$%^&*).")

    return {
        "valida": len(errores) == 0,
        "errores": errores
    }