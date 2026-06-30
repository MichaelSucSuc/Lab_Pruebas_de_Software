# test_validador.py

import pytest
import validador

# ─── TC-01: Contraseña completamente válida ──────────────────────────
def test_tc01_contrasena_valida():
    # Arrange
    contrasena = "Segura#1"

    # Act
    resultado = validador.validar_contrasena(contrasena)

    # Assert
    assert resultado["valida"] is True
    assert resultado["errores"] == []

# ─── TC-02: Contraseña muy corta (<8 caracteres) ─────────────────────
def test_tc02_muy_corta():
    # Arrange
    contrasena = "Ab1!"

    # Act
    resultado = validador.validar_contrasena(contrasena)

    # Assert
    assert resultado["valida"] is False
    assert "8 caracteres" in resultado["errores"][0]

# ─── TC-03: Sin letra mayúscula ──────────────────────────────────────
def test_tc03_sin_mayuscula():
    # Arrange
    contrasena = "segura#1"

    # Act
    resultado = validador.validar_contrasena(contrasena)

    # Assert
    assert resultado["valida"] is False
    assert any("mayúscula" in e for e in resultado["errores"])

# ─── TC-04: Sin letra minúscula ──────────────────────────────────────
def test_tc04_sin_minuscula():
    # Arrange
    contrasena = "SEGURA#1"

    # Act
    resultado = validador.validar_contrasena(contrasena)

    # Assert
    assert resultado["valida"] is False
    assert any("minúscula" in e for e in resultado["errores"])

# ─── TC-05: Sin dígito numérico ──────────────────────────────────────
def test_tc05_sin_digito():
    # Arrange
    contrasena = "Segura##"

    # Act
    resultado = validador.validar_contrasena(contrasena)

    # Assert
    assert resultado["valida"] is False
    assert any("dígito" in e for e in resultado["errores"])

# ─── TC-06: Sin carácter especial ────────────────────────────────────
def test_tc06_sin_especial():
    # Arrange
    contrasena = "Segura12"

    # Act
    resultado = validador.validar_contrasena(contrasena)

    # Assert
    assert resultado["valida"] is False
    assert any("especial" in e for e in resultado["errores"])

# ─── TC-07: Contraseña vacía ─────────────────────────────────────────
def test_tc07_vacia():
    # Arrange
    contrasena = ""

    # Act
    resultado = validador.validar_contrasena(contrasena)

    # Assert
    assert resultado["valida"] is False
    assert len(resultado["errores"]) == 5

# ─── TC-08: aB1IcDe2 NO tiene carácter especial → debe ser FALSO ─────
def test_tc08_exacto_8_sin_especial():
    # Arrange
    contrasena = "aB1IcDe2"

    # Act
    resultado = validador.validar_contrasena(contrasena)

    # Assert
    assert resultado["valida"] is False  # <--- IMPORTANTE: False, no True
    assert any("especial" in e for e in resultado["errores"])

# ─── TC-09: SOLO contraseñas débiles (Solounamayuscula1! NO está aquí) ─
@pytest.mark.parametrize("contrasena", [
    "abc123",
    "SOLOMAYUSCULAS",
    "solominusculas1",
    "NoDigito!",
    "MayusMinus123",
    "aA1!",
    "corta",
])
def test_tc09_param_varias_debiles(contrasena):
    # Act
    resultado = validador.validar_contrasena(contrasena)

    # Assert
    assert resultado["valida"] is False, f"'{contrasena}' no debería ser válida"

# ─── Prueba: Solounamayuscula1! SÍ es válida ─────────────────────────
def test_contrasena_larga_valida():
    # Arrange
    contrasena = "Solounamayuscula1!"

    # Act
    resultado = validador.validar_contrasena(contrasena)

    # Assert
    assert resultado["valida"] is True
    assert resultado["errores"] == []