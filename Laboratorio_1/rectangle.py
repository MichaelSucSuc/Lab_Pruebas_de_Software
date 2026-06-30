# rectangle.py
# Programa para calcular el área de un rectángulo
# VERSIÓN VULNERABLE - Sin validaciones, sin try-except
# Se rompe fácilmente con cualquier entrada incorrecta

def calcular_area(base, altura):
    """Calcula el área de un rectángulo"""
    return base * altura

def main():
    print("=" * 50)
    print("CÁLCULO DEL ÁREA DE UN RECTÁNGULO")
    print("=" * 50)
    
    # Pedir base - SIN VALIDACIONES
    base = float(input("\nIngrese la base del rectángulo: "))
    
    # Pedir altura - SIN VALIDACIONES
    altura = float(input("Ingrese la altura del rectángulo: "))
    
    # Calcular área
    area = calcular_area(base, altura)
    
    # Mostrar resultado
    print("\n" + "-" * 50)
    print("RESULTADO:")
    print("-" * 50)
    print(f"Base: {base}")
    print(f"Altura: {altura}")
    print(f"Área: {area}")
    print("=" * 50)

if __name__ == "__main__":
    main()