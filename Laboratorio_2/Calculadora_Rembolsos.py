# Calculadora_Rembolsos.py
# Calculadora de Reembolsos para cancelación de reservas de hotel
# Aplica reglas de negocio con prioridad para clientes VIP

def calcular_reembolso(monto, horas, es_vip):
    """
    Calcula el reembolso según reglas de negocio del hotel.
    
    Reglas:
    - horas < 0 → 0% para todos (cancelación después del check-in)
    - > 72 horas: 100% reembolso
    - 24 a 72 horas: 50% reembolso  
    - < 24 horas: 0% reembolso
    - VIP: MÁXIMO entre (regla normal) y 50% (nunca recibe menos)
    
    Validaciones:
    - monto debe ser numérico (int o float) y >= 0
    - horas debe ser numérico (int o float)
    - es_vip debe ser booleano
    """
    
    # ============================================================
    # VALIDACIONES DE TIPO (Robustez)
    # ============================================================
    
    if not isinstance(monto, (int, float)):
        raise TypeError(f"Monto debe ser numérico (int o float), recibido: {type(monto).__name__}")
    
    if not isinstance(horas, (int, float)):
        raise TypeError(f"Horas debe ser numérico (int o float), recibido: {type(horas).__name__}")
    
    if not isinstance(es_vip, bool):
        raise TypeError(f"es_vip debe ser booleano (True/False), recibido: {type(es_vip).__name__}")
    
    # ============================================================
    # VALIDACIONES DE DOMINIO
    # ============================================================
    
    if monto < 0:
        raise ValueError("El monto no puede ser negativo")
    
    # ============================================================
    # LÓGICA DE NEGOCIO
    # ============================================================
    
    # Cancelación después del evento = sin reembolso
    if horas < 0:
        return 0.0
    
    # Calcular porcentaje según plazo (regla base)
    if horas > 72:
        porcentaje_base = 1.0
    elif horas >= 24:
        porcentaje_base = 0.5
    else:
        porcentaje_base = 0.0
    
    # Regla VIP: toma el mejor beneficio (prioridad sobre regla de última hora)
    if es_vip:
        porcentaje_final = max(porcentaje_base, 0.5)
    else:
        porcentaje_final = porcentaje_base
    
    return float(monto * porcentaje_final)