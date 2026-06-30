# Calculadora_Rembolsos_test.py
# Pruebas unitarias para la Calculadora de Reembolsos
# Aplica TDD, análisis de valor límite y pruebas de robustez

import pytest
from Calculadora_Rembolsos import calcular_reembolso

# ============================================================
# CLASE 1: Reglas base (sin VIP)
# ============================================================

def test_normal_mas_72h():
    """>72h → 100%"""
    assert calcular_reembolso(100, 73, False) == 100.0
    assert calcular_reembolso(100, 96, False) == 100.0
    assert calcular_reembolso(100, 168, False) == 100.0

def test_normal_24_a_72h():
    """24-72h → 50%"""
    assert calcular_reembolso(100, 24, False) == 50.0
    assert calcular_reembolso(100, 48, False) == 50.0
    assert calcular_reembolso(100, 72, False) == 50.0

def test_normal_menos_24h():
    """<24h → 0%"""
    assert calcular_reembolso(100, 23, False) == 0.0
    assert calcular_reembolso(100, 12, False) == 0.0
    assert calcular_reembolso(100, 1, False) == 0.0
    assert calcular_reembolso(100, 0, False) == 0.0

# ============================================================
# CLASE 2: Regla VIP (Prioridad sobre regla de última hora)
# ============================================================

def test_vip_cancela_ultima_hora():
    """
    Escenario BDD: Cliente VIP cancela con 2 horas de antelación
    Debe recibir 50% (prioridad VIP sobre regla <24h que da 0%)
    """
    assert calcular_reembolso(500, 2, True) == 250.0  # 50% de 500
    assert calcular_reembolso(100, 2, True) == 50.0
    assert calcular_reembolso(100, 0, True) == 50.0

def test_vip_cancela_con_mucha_anticipacion():
    """VIP >72h → recibe 100% (no penalizado)"""
    assert calcular_reembolso(100, 96, True) == 100.0
    assert calcular_reembolso(100, 73, True) == 100.0

def test_vip_cancela_anticipacion_media():
    """VIP 24-72h → recibe 50%"""
    assert calcular_reembolso(100, 48, True) == 50.0
    assert calcular_reembolso(100, 24, True) == 50.0
    assert calcular_reembolso(100, 72, True) == 50.0

def test_vip_prioridad_sobre_ultima_hora():
    """Verifica que VIP tiene prioridad sobre regla de última hora"""
    # Regular con 2h recibe 0%
    assert calcular_reembolso(500, 2, False) == 0.0
    # VIP con 2h recibe 50% (prioridad VIP)
    assert calcular_reembolso(500, 2, True) == 250.0
    # VIP recibe más que regular en este escenario
    assert calcular_reembolso(500, 2, True) > calcular_reembolso(500, 2, False)

# ============================================================
# CLASE 3: Análisis de valores límite (Boundary Value Analysis)
# ============================================================

def test_limite_24_horas():
    """Prueba exactamente en la frontera de 24 horas"""
    # Regular: 24h → 50%, 23h → 0%
    assert calcular_reembolso(100, 24, False) == 50.0
    assert calcular_reembolso(100, 23, False) == 0.0
    
    # VIP: 24h → 50%, 23h → 50% (protegido)
    assert calcular_reembolso(100, 24, True) == 50.0
    assert calcular_reembolso(100, 23, True) == 50.0

def test_limite_72_horas():
    """Prueba exactamente en la frontera de 72 horas"""
    # Regular: 72h → 50%, 73h → 100%
    assert calcular_reembolso(100, 72, False) == 50.0
    assert calcular_reembolso(100, 73, False) == 100.0
    
    # VIP: 72h → 50%, 73h → 100%
    assert calcular_reembolso(100, 72, True) == 50.0
    assert calcular_reembolso(100, 73, True) == 100.0

def test_limite_cero_horas():
    """Frontera entre horas válidas y negativas"""
    assert calcular_reembolso(100, 0, False) == 0.0
    assert calcular_reembolso(100, 0, True) == 50.0
    assert calcular_reembolso(100, -0.1, False) == 0.0
    assert calcular_reembolso(100, -0.1, True) == 0.0

# ============================================================
# CLASE 4: Pruebas de Robustez (Validaciones de error)
# ============================================================

def test_monto_negativo_lanza_error():
    """Protección contra errores: monto negativo debe lanzar ValueError"""
    with pytest.raises(ValueError, match="El monto no puede ser negativo"):
        calcular_reembolso(-500, 48, False)
    
    with pytest.raises(ValueError, match="El monto no puede ser negativo"):
        calcular_reembolso(-500, 48, True)

def test_tipo_datos_invalidos_lanza_error():
    """Protección contra tipos de datos incorrectos"""
    with pytest.raises(TypeError, match="Monto debe ser numérico"):
        calcular_reembolso("1000", 48, False)
    
    with pytest.raises(TypeError, match="Horas debe ser numérico"):
        calcular_reembolso(1000, "48", False)
    
    with pytest.raises(TypeError, match="es_vip debe ser booleano"):
        calcular_reembolso(1000, 48, "True")

def test_monto_cero_valido():
    """Monto 0 es un caso válido (borde inferior)"""
    assert calcular_reembolso(0, 48, False) == 0.0
    assert calcular_reembolso(0, 2, True) == 0.0

# ============================================================
# CLASE 5: Escenarios reales de negocio
# ============================================================

def test_caso_real_vip_emergencia_2_horas():
    """Escenario BDD documentado: VIP cancela con 2 horas"""
    reserva = 500
    reembolso = calcular_reembolso(reserva, 2, True)
    assert reembolso == 250.0
    print(f"\n✅ Caso BDD: VIP con 2h → Reembolso: S/. {reembolso}")

def test_caso_real_vip_no_perdida():
    """VIP con 96h recibe 100%, igual que regular"""
    assert calcular_reembolso(1000, 96, True) == 1000.0
    assert calcular_reembolso(1000, 96, False) == 1000.0

def test_caso_real_horas_decimales():
    """Soporte para horas decimales (ej: 23.5 horas)"""
    assert calcular_reembolso(100, 24.5, False) == 50.0
    assert calcular_reembolso(100, 23.5, True) == 50.0

# ============================================================
# EJECUCIÓN
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("EJECUTANDO PRUEBAS - CALCULADORA DE REEMBOLSOS")
    print("=" * 60)
    pytest.main([__file__, "-v", "--tb=short"])