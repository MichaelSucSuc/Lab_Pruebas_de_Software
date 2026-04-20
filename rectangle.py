# rectangle.py
# Programa que calcula el área de un rectángulo - VERSIÓN ULTRAROBUSTA

import re
import sys

# Constantes para límites de truncamiento
MAX_VALID_VALUE = 1e12      # 1,000,000,000,000 (un billón)
MIN_VALID_VALUE = 1e-12     # 0.000000000001 (un billonésimo)
MAX_AREA = 1e24             # Área máxima permitida (1e24)


def sanitizar_entrada(valor_str):
    """
    Limpia y valida la entrada del usuario.
    
    Args:
        valor_str: String ingresado por el usuario
    
    Returns:
        float limpio y validado
    
    Raises:
        ValueError: Si la entrada es inválida (vacía, solo espacios, letras, etc.)
    """
    # Caso 1: Entrada vacía o None
    if valor_str is None:
        raise ValueError("No se ingresó ningún valor")
    
    # Caso 2: Eliminar espacios al inicio y final, pero NO espacios internos
    valor_limpio = valor_str.strip()
    
    # Caso 3: String vacío después de limpiar
    if len(valor_limpio) == 0:
        raise ValueError("Entrada vacía. Debe ingresar un número.")
    
    # Caso 4: Detectar espacios internos (ej: "12 34")
    if ' ' in valor_limpio:
        raise ValueError("El número no debe contener espacios internos.")
    
    # Caso 5: Detectar múltiples puntos decimales
    if valor_limpio.count('.') > 1:
        raise ValueError("Formato inválido: múltiples puntos decimales.")
    
    # Caso 6: Detectar símbolos no permitidos (letras, símbolos especiales)
    # Permitidos: dígitos, un punto decimal, y un signo menos al inicio
    patron_valido = r'^-?\d+\.?\d*$|^-?\d*\.?\d+$'
    if not re.match(patron_valido, valor_limpio):
        # Detección específica de letras
        if re.search(r'[a-zA-Z]', valor_limpio):
            raise ValueError("No se permiten letras. Ingrese solo números.")
        # Detección de símbolos especiales
        if re.search(r'[!@#$%^&*()_+=\[\]{};:"\\|,<>/?]', valor_limpio):
            raise ValueError("No se permiten símbolos especiales. Ingrese solo números.")
        raise ValueError("Formato de número inválido.")
    
    # Caso 7: Convertir a float
    try:
        numero = float(valor_limpio)
    except ValueError:
        raise ValueError("No se pudo convertir el valor a número.")
    
    return numero


def truncar_valor(valor, nombre):
    """
    Trunca un valor si excede los límites permitidos.
    
    Args:
        valor: Número a verificar
        nombre: Nombre del campo ("base" o "altura") para mensajes
    
    Returns:
        Número truncado dentro de los límites permitidos
    """
    valor_original = valor
    truncado = False
    
    # Truncar si es demasiado grande positivo
    if valor > MAX_VALID_VALUE:
        valor = MAX_VALID_VALUE
        truncado = True
    # Truncar si es demasiado pequeño positivo (cercano a cero)
    elif 0 < valor < MIN_VALID_VALUE:
        valor = MIN_VALID_VALUE
        truncado = True
    # Truncar si es demasiado grande negativo (muy negativo)
    elif valor < -MAX_VALID_VALUE:
        valor = -MAX_VALID_VALUE
        truncado = True
    # Truncar si es demasiado pequeño negativo (cercano a cero desde negativos)
    elif -MIN_VALID_VALUE < valor < 0:
        valor = -MIN_VALID_VALUE
        truncado = True
    
    if truncado:
        print(f"[ADVERTENCIA] El valor de {nombre} ({valor_original}) ha sido truncado a {valor}")
    
    return valor


def validar_positivo(valor, nombre):
    """
    Valida que el valor sea positivo.
    
    Args:
        valor: Número a validar
        nombre: Nombre del campo ("base" o "altura")
    
    Raises:
        ValueError: Si el valor es cero o negativo
    """
    if valor <= 0:
        if valor == 0:
            raise ValueError(f"La {nombre} no puede ser cero. Debe ser mayor que 0.")
        else:
            raise ValueError(f"La {nombre} no puede ser negativa. Ingresó: {valor}")


def calcular_area(base, altura):
    """
    Calcula el área de un rectángulo con truncamiento de valores extremos.
    
    Args:
        base: La longitud de la base (número positivo, entero o float)
        altura: La longitud de la altura (número positivo, entero o float)
    
    Returns:
        El área calculada (base * altura)
    """
    # Validar que sean números
    if not isinstance(base, (int, float)):
        raise TypeError("La base debe ser un número")
    if not isinstance(altura, (int, float)):
        raise TypeError("La altura debe ser un número")
    
    # Validar que sean positivos
    validar_positivo(base, "base")
    validar_positivo(altura, "altura")
    
    # Truncar valores extremos
    base = truncar_valor(base, "base")
    altura = truncar_valor(altura, "altura")
    
    # Calcular área
    area = base * altura
    
    # Truncar área si excede el límite máximo
    if area > MAX_AREA:
        area = MAX_AREA
        print(f"[ADVERTENCIA] El área calculada ({base * altura}) ha sido truncada a {MAX_AREA}")
    
    return area


def solicitar_medida(nombre_medida):
    """
    Solicita una medida (base o altura) al usuario con validación robusta.
    
    Args:
        nombre_medida: "base" o "altura"
    
    Returns:
        float válido ingresado por el usuario
    """
    intentos = 0
    max_intentos = 3
    
    while intentos < max_intentos:
        try:
            entrada = input(f"Ingrese la {nombre_medida} del rectángulo: ")
            numero = sanitizar_entrada(entrada)
            # Nota: la validación de positivo se hará en calcular_area
            return numero
            
        except ValueError as e:
            intentos += 1
            print(f"  [ERROR] {e}")
            if intentos < max_intentos:
                print(f"  Le quedan {max_intentos - intentos} intento(s).")
            else:
                print(f"  [ERROR FATAL] Demasiados intentos fallidos. Saliendo del programa.")
                sys.exit(1)
    
    return None  # No debería llegar aquí


def main():
    """
    Función principal que solicita datos al usuario y muestra el resultado.
    """
    print("\n" + "=" * 60)
    print("   CALCULADORA DE ÁREA DE RECTÁNGULO (Versión Ultra Robusta)")
    print("=" * 60)
    print("\n[INFO] Límite máximo aceptado: 1,000,000,000,000 (1e12)")
    print("[INFO] Límite mínimo aceptado: 0.000000000001 (1e-12)")
    print("[INFO] Valores fuera de estos límites serán truncados.\n")
    
    # Solicitar base y altura con validación
    base = solicitar_medida("base")
    altura = solicitar_medida("altura")
    
    # Calcular el área
    try:
        area = calcular_area(base, altura)
        
        # Mostrar el resultado
        print("\n" + "-" * 60)
        print("RESULTADO:")
        print(f"  Base:   {base}")
        print(f"  Altura: {altura}")
        print(f"  Área:   {area}")
        print("-" * 60)
        
    except ValueError as e:
        print(f"\n[ERROR] {e}")
        print("El programa terminará.")
        sys.exit(1)


if __name__ == "__main__":
    main()