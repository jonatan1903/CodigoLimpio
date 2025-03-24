import pytest
from src.model.sistemaUsuario import SistemaJugador
from src.model.jugador import Jugador

@pytest.fixture
def sistema():
    return SistemaJugador()

#  PRUEBAS NORMALES
def test_registro_exitoso(sistema):
    jugador = Jugador("usuario123", "contraseña123")
    resultado = sistema.registrar_jugador(jugador.nombre_usuario, jugador.contraseña)
    assert resultado == True  

def test_inicio_sesion_exitoso(sistema):
    sistema.registrar_jugador("Jugador2", "passwordSeguro")
    jugador = sistema.iniciar_sesion("Jugador2", "passwordSeguro")
    assert jugador is not None  

def test_inicio_sesion_usuario_no_registrado(sistema):
    jugador = sistema.iniciar_sesion("Desconocido", "claveCualquiera")
    assert jugador is None  

#  PRUEBAS EXTREMAS
def test_registro_muchos_jugadores(sistema):
    for i in range(1000):
        resultado = sistema.registrar_jugador(f"Jugador{i}", f"password{i}")
        assert resultado == True  

def test_intentos_fallidos_inicio_sesion(sistema):
    sistema.registrar_jugador("Usuario123", "claveSegura")
    for _ in range(10):
        jugador = sistema.iniciar_sesion("usuario123", "claveIncorrecta")
        assert jugador is None  

def test_registro_usuario_existente(sistema):
    sistema.registrar_jugador("Repetido", "password123")
    resultado = sistema.registrar_jugador("Repetido", "otraClave")
    assert resultado == False 

#  PRUEBAS DE ERROR
def test_registro_usuario_sin_nombre(sistema):
    resultado = sistema.registrar_jugador("", "password123")
    assert resultado == False 

def test_registro_usuario_sin_contraseña(sistema):
    resultado = sistema.registrar_jugador("UsuarioSinClave", "")
    assert resultado == False  

def test_registro_usuario_con_espacios(sistema):
    resultado = sistema.registrar_jugador("   ", "password123")
    assert resultado == False 
