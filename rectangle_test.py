# rectangle_test.py
# Script para probar rectangle.py manualmente
# Analiza CADA input por separado y dice exactamente qué está mal

from rectangle import calcular_area

def analizar_input(valor, nombre):
    """Analiza un input y devuelve (es_valido, mensaje, numero)"""
    
    # Caso 1: Vacío
    if valor == "":
        return False, f"{nombre} está VACÍA", None
    
    # Caso 2: Solo espacios
    if valor.strip() == "":
        return False, f"{nombre} solo tiene ESPACIOS", None
    
    # Caso 3: Intentar convertir a número
    try:
        num = float(valor)
        
        # Caso 4: Número negativo
        if num < 0:
            return False, f"{nombre} es NEGATIVO ({num})", None
        
        # Caso 5: Cero
        if num == 0:
            return False, f"{nombre} es CERO", None
        
        # Caso 6: Número positivo válido
        return True, f"{nombre} es válido ({num})", num
        
    except ValueError:
        # Caso 7: Revisar si es coma decimal
        if "," in valor:
            return False, f"{nombre} tiene COMA decimal (usa punto)", None
        
        # Caso 8: Revisar si tiene letras
        if any(c.isalpha() for c in valor):
            return False, f"{nombre} tiene LETRAS", None
        
        # Caso 9: Revisar si tiene símbolos
        if any(not c.isdigit() and c not in ['.', '-', '+'] for c in valor):
            return False, f"{nombre} tiene SÍMBOLOS", None
        
        # Caso 10: Otro error
        return False, f"{nombre} NO es un número válido", None

def main():
    print("=" * 70)
    print("PRUEBA MANUAL - RECTÁNGULO (ANÁLISIS DETALLADO)")
    print("=" * 70)
    
    # Pedir datos
    print("\n📝 Ingrese los datos de prueba:")
    base_input = input("   Base: ")
    altura_input = input("   Altura: ")
    
    
    # Analizar base
    base_valida, base_mensaje, base_num = analizar_input(base_input, "Base")
    print(f"\n🔍 {base_mensaje}")
    
    # Analizar altura
    altura_valida, altura_mensaje, altura_num = analizar_input(altura_input, "Altura")
    print(f"🔍 {altura_mensaje}")
    
    
    # Decidir resultado
    if base_valida and altura_valida:
        area = calcular_area(base_num, altura_num)
        print(f"\n✅ ÉXITO: Área = {area}")
    else:
        print("\n❌ ERROR: No se puede calcular el área")
        print("   La base y altura deben ser números POSITIVOS")
    

if __name__ == "__main__":
    main()