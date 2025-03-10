import pytest
from src.model.sistemaUsuario import SistemaJugador
from src.model.jugador import Jugador

@pytest.fixture
def sistema():

    return SistemaJugador()


#Pruebas Normales

def test_registro_exitoso(sistema):
    jugador = Jugador("usuario123", "contraseña123")
    with pytest.raises(AttributeError):
        sistema.registrar_jugador(jugador)

def test_inicio_sesion_exitoso(sistema):
    jugador = Jugador("Jugador2", "passwordSeguro")
    sistema.registrar_jugador(jugador)
    with pytest.raises(TypeError):
        sistema.iniciar_sesion("Jugador2", "passwordSeguro")

def test_inicio_sesion_usuario_no_registrado(sistema):
    with pytest.raises(TypeError):
        sistema.iniciar_sesion("Desconocido", "claveCualquiera")


# Pruebas extremas


def test_registro_muchos_jugadores(sistema):
    with pytest.raises(AttributeError):
        for i in range(1000):
            jugador = Jugador(f"Jugador{i}", f"password{i}")
            sistema.registrar_jugador(jugador)

def test_intentos_fallidos_inicio_sesion(sistema):
    jugador = Jugador("Usuario123", "claveSegura")
    sistema.registrar_jugador(jugador)
    with pytest.raises(TypeError):
        for _ in range(10):
            sistema.iniciar_sesion("usuario123", "claveIncorrecta")

def test_registro_usuario_existente(sistema):
    jugador1 = Jugador("Repetido", "password123")
    jugador2 = Jugador("Repetido", "otraClave")
    sistema.registrar_jugador(jugador1)
    with pytest.raises(TypeError):  
        sistema.registrar_jugador(jugador2)


#Pruebas Error

def test_registro_usuario_sin_nombre(sistema):
    with pytest.raises(ValueError, match="El nombre de usuario no puede estar vacío"):
        jugador = Jugador("", "password123")
        sistema.registrar_jugador(jugador)

def test_registro_usuario_sin_contraseña(sistema):
    with pytest.raises(ValueError, match="La contraseña no puede estar vacía"):
        jugador = Jugador("UsuarioSinClave", "")
        sistema.registrar_jugador(jugador)

def test_registro_usuario_con_espacios(sistema):
    with pytest.raises(ValueError, match="El nombre de usuario no puede contener solo espacios"):
        jugador = Jugador("   ", "password123")
        sistema.registrar_jugador(jugador)
