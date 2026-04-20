# rectangle_test.py
# Archivo de pruebas para rectangle.py
# Se prueban TODOS los casos: válidos, inválidos, intentos de romperlo.

from rectangle import calcular_area

def probar_caso(descripcion, base, altura, esperado):
    """
    Función auxiliar para probar un caso y mostrar si pasó o falló.
    """
    resultado = calcular_area(base, altura)
    if resultado == esperado:
        print(f"✅ PASÓ: {descripcion}")
    else:
        print(f"❌ FALLÓ: {descripcion} -> Esperado {esperado}, obtenido {resultado}")

def main():
    print("=== PRUEBAS DEL PROGRAMA RECTÁNGULO (VERSIÓN CORREGIDA) ===\n")
    
    # ===== CASOS VÁLIDOS (deben dar el área correcta) =====
    probar_caso("Enteros positivos", "5", "3", 15.0)
    probar_caso("Decimales", "2.5", "4.2", 10.5)
    probar_caso("Base decimal, altura entera", "7.3", "2", 14.6)
    probar_caso("Base entera, altura decimal", "8", "1.5", 12.0)
    probar_caso("Números grandes", "1000", "2000", 2_000_000.0)
    probar_caso("Muy pequeños positivos", "0.0001", "0.0002", 2e-08)
    
    # ===== CASOS INVÁLIDOS POR NÚMEROS NEGATIVOS O CERO =====
    probar_caso("Base negativa", "-5", "4", None)
    probar_caso("Altura negativa", "5", "-4", None)
    probar_caso("Ambos negativos", "-2", "-3", None)
    probar_caso("Base cero", "0", "5", None)
    probar_caso("Altura cero", "8", "0", None)
    probar_caso("Ambos cero", "0", "0", None)
    probar_caso("Base negativa con decimal", "-2.5", "3", None)
    
    # ===== CASOS INVÁLIDOS POR TEXTO O SÍMBOLOS =====
    probar_caso("Base con letras", "abc", "5", None)
    probar_caso("Altura con letras", "8", "xyz", None)
    probar_caso("Ambos con letras", "hola", "mundo", None)
    probar_caso("Base con símbolos", "@#$", "5", None)
    probar_caso("Altura con símbolos", "8", "!@#", None)
    
    # ===== CASOS INVÁLIDOS POR VACÍOS O ESPACIOS =====
    probar_caso("Valor vacío", "", "5", None)
    probar_caso("Solo espacios", "   ", "3", None)
    probar_caso("Base vacía, altura válida", "", "10", None)
    probar_caso("Altura vacía, base válida", "10", "", None)
    probar_caso("Ambos vacíos", "", "", None)
    probar_caso("Solo espacios en ambos", "   ", "   ", None)
    
    # ===== CASOS INVÁLIDOS POR FORMATOS RAROS =====
    probar_caso("Número con letras pegadas", "3a", "4", None)
    probar_caso("Doble signo", "--5", "4", None)
    probar_caso("Signo más", "+5", "4", 20.0)  # +5 es válido, es positivo
    probar_caso("Espacios internos", "5 0", "4", None)  # "5 0" no es número válido
    probar_caso("Coma en lugar de punto", "5,5", "4", None)  # Python usa punto decimal
    probar_caso("Número con texto", "5 perros", "4", None)
    
    print("\n=== FIN DE LAS PRUEBAS ===")
    print("\nNOTA: Solo los casos con números POSITIVOS (enteros o decimales) deberían pasar.")
    print("      Negativos, cero, letras, símbolos, vacíos y formatos raros son RECHAZADOS.")

if __name__ == "__main__":
    main()