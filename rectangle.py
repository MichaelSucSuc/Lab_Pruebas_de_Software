# rectangle.py
# Este programa solicita base y altura de un rectángulo y calcula su área.
# ROBUSTO: Rechaza números negativos, cero, letras, símbolos, vacíos, espacios, etc.

def calcular_area(base, altura):
    """
    Calcula el área de un rectángulo solo si ambos valores son números positivos.
    Retorna el área (float) si es válido, retorna None si hay algún error.
    """
    try:
        # Convertir a float (permite enteros y decimales)
        b = float(base)
        a = float(altura)
        
        # Validar que sean ESTRICTAMENTE POSITIVOS (mayores que cero)
        if b <= 0 or a <= 0:
            return None  # Número negativo o cero no es válido para un lado
        
        # Calcular área
        area = b * a
        return area
    
    except ValueError:
        # Si no se puede convertir a número (letras, símbolos, etc.)
        return None

def main():
    print("=== CÁLCULO DEL ÁREA DE UN RECTÁNGULO ===")
    print("(Solo se aceptan números POSITIVOS - mayores que cero)\n")
    
    # Solicitar base
    base_input = input("Ingrese la base del rectángulo: ").strip()
    # Solicitar altura
    altura_input = input("Ingrese la altura del rectángulo: ").strip()
    
    # Calcular área usando la función robusta
    area = calcular_area(base_input, altura_input)
    
    # Verificar si el cálculo fue exitoso
    if area is None:
        print("\n❌ ERROR: La base y altura deben ser números POSITIVOS (mayores que cero).")
        print("   No se aceptan: números negativos, cero, letras, símbolos o valores vacíos.")
    else:
        print(f"\n✅ RESULTADO:")
        print(f"   Base   = {base_input}")
        print(f"   Altura = {altura_input}")
        print(f"   Área   = {area}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()