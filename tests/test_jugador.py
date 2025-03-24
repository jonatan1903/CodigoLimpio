import pytest
from src.model.jugador import Jugador

#  PRUEBAS NORMALES
def test_creacion_jugador():
    jugador = Jugador("usuario123", "contraseña123")
    assert jugador.nombre_usuario == "usuario123"
    assert jugador.contraseña == "contraseña123"
    assert jugador.puntaje == 0

def test_cambiar_contraseña():
    jugador = Jugador("usuario123", "contraseña123")
    resultado = jugador.cambiar_contraseña("nueva123")
    assert resultado == "ÉXITO"
    assert jugador.contraseña == "nueva123"

def test_actualizar_puntaje():
    jugador = Jugador("usuario123", "contraseña123")
    jugador.actualizar_puntaje(10)
    assert jugador.puntaje == 10

#  PRUEBAS EXTREMAS
def test_cambiar_contraseña_vacia():
    jugador = Jugador("usuario123", "contraseña123")
    resultado = jugador.cambiar_contraseña("")
    assert resultado == "ERROR"

def test_actualizar_puntaje_cero():
    jugador = Jugador("usuario123", "contraseña123")
    jugador.actualizar_puntaje(0)
    assert jugador.puntaje == 0 

def test_actualizar_puntaje_muy_alto():
    jugador = Jugador("usuario123", "contraseña123")
    jugador.actualizar_puntaje(9999999)
    assert jugador.puntaje == 9999999

#  PRUEBAS DE ERROR
def test_cambiar_contraseña_none():
    jugador = Jugador("usuario123", "contraseña123")
    resultado = jugador.cambiar_contraseña(None)
    assert resultado == "ERROR"  

def test_actualizar_puntaje_negativo():
    jugador = Jugador("usuario123", "contraseña123")
    jugador.actualizar_puntaje(-5)
    assert jugador.puntaje == -5 

def test_actualizar_puntaje_no_numerico():
    jugador = Jugador("usuario123", "contraseña123")
    with pytest.raises(TypeError):
        jugador.actualizar_puntaje("diez")  
