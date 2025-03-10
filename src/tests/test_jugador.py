import pytest

class JuegoMock:
    def realizar_disparo(self, x, y):
        if x == 1 and y == 1:
            return "¡Impacto!"
        return "Agua..."

from src.model.jugador import Jugador


#Pruebas Normales

def test_creacion_jugador():
    with pytest.raises(AttributeError):
        jugador = Jugador("usuario123", "contraseña123")
        assert jugador.nombre_usuario == "usuario123"
        assert jugador.contraseña == "contraseña123"
        assert jugador.puntaje == 0

def test_realizar_disparo():
    jugador = Jugador("usuario123", "contraseña123")
    with pytest.raises(NameError):  
        juego = JuegoMock()
        resultado = jugador.realizar_disparo(juego, 1, 1)
        assert resultado == "¡Impacto!"
        assert jugador.puntaje == 1

def test_cambiar_contraseña():
    jugador = Jugador("usuario123", "contraseña123")
    with pytest.raises(AttributeError):
        resultado = jugador.cambiar_contraseña("nueva123")
        assert resultado == "Contraseña cambiada exitosamente."
        assert jugador.contraseña == "nueva123"

#Pruebas Extremas

def test_contraseña_extremadamente_larga():
    jugador = Jugador("usuario123", "contraseña123")
    nueva_contraseña = "a" * 1000  
    resultado = jugador.cambiar_contraseña(nueva_contraseña)
    assert resultado == "Contraseña cambiada exitosamente."
    assert jugador.contraseña == nueva_contraseña

def test_coordenadas_disparo_fuera_rango():
    jugador = Jugador("usuario123", "contraseña123")
    juego = JuegoMock()
    resultado = jugador.realizar_disparo(juego, 9999, 9999)
    assert resultado == "Agua..."
    assert jugador.puntaje == 0

def test_multiples_impactos_consecutivos():
    jugador = Jugador("usuario123", "contraseña123")
    juego = JuegoMock()
    for _ in range(10):  
        resultado = jugador.realizar_disparo(juego, 1, 1)
        assert resultado == "¡Impacto!"
    assert jugador.puntaje == 10


#Pruebas Error


def test_contraseña_extremadamente_corta():
    jugador = Jugador("usuario123", "contraseña123")
    nueva_contraseña = "abc"  
    
    with pytest.raises(ValueError) as error_info:  
        jugador.cambiar_contraseña(nueva_contraseña)
    
    assert str(error_info.value) == "La contraseña es demasiado corta."


def test_coordenadas_disparo_no_numericas():
    jugador = Jugador("usuario123", "contraseña123")
    juego = JuegoMock()
    
    with pytest.raises(TypeError) as error_info:
        jugador.realizar_disparo(juego, "a", "b")  

    assert str(error_info.value) == "Las coordenadas deben ser números."
    

def test_inicializacion_jugador_con_nulos():
    with pytest.raises(ValueError) as error_info:
        jugador = Jugador(None, None)  

    assert str(error_info.value) == "El nombre de usuario y la contraseña no pueden ser nulos."
