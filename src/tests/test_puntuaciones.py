import pytest

from src.model.puntuaciones import Puntuaciones

#Prueba Normal

def test_mostrar_puntuaciones_no_implementado():
    puntuaciones = Puntuaciones()
    resultado = puntuaciones.mostrar_puntuaciones()
    assert resultado is not None, "Parece que la función no está implementada o no devuelve nada."


def test_actualizar_puntuacion_sin_jugador():
    puntuaciones = Puntuaciones()
    with pytest.raises(AttributeError):
        puntuaciones.actualizar_puntuacion(None)  


def test_mostrar_puntuaciones_sin_jugadores():
    puntuaciones = Puntuaciones()
    resultado = puntuaciones.mostrar_puntuaciones()
    assert resultado != "", "El programa debería decir que no hay puntuaciones en lugar de quedarse en blanco."


#Prueba Extrema

class JugadorMock:
    def __init__(self, nombre, puntaje):
        self.nombre_usuario = nombre
        self.puntaje = puntaje

def test_mostrar_puntuaciones_muchos_jugadores():
    puntuaciones = Puntuaciones()
    jugadores = [JugadorMock(f"Jugador{i}", i) for i in range(10000)]
    for jugador in jugadores:
        puntuaciones.actualizar_puntuacion(jugador)
    resultado = puntuaciones.mostrar_puntuaciones()
    assert resultado, "El programa no debería crashear con muchos jugadores."

def test_mostrar_puntuaciones_jugadores_sin_puntaje():
    puntuaciones = Puntuaciones()
    jugadores = [JugadorMock("Jugador1", None), JugadorMock("Jugador2", 500), JugadorMock("Jugador3", 0)]
    for jugador in jugadores:
        puntuaciones.actualizar_puntuacion(jugador)
    resultado = puntuaciones.mostrar_puntuaciones()
    assert "Jugador1" in resultado, "Los jugadores sin puntaje deberían aparecer en la tabla."

def test_mostrar_puntuaciones_empate():
    puntuaciones = Puntuaciones()
    jugadores = [JugadorMock(f"Jugador{i}", 100) for i in range(5)]
    for jugador in jugadores:
        puntuaciones.actualizar_puntuacion(jugador)
    resultado = puntuaciones.mostrar_puntuaciones()
    assert "Jugador0" in resultado and "Jugador4" in resultado, "Los jugadores deberían aparecer en la tabla."


#Prueba Error

def test_actualizar_puntuacion_sin_jugador():
    puntuaciones = Puntuaciones()
    with pytest.raises(AttributeError):
        puntuaciones.actualizar_puntuacion(None)

def test_mostrar_puntuaciones_sin_datos():
    puntuaciones = Puntuaciones()
    resultado = puntuaciones.mostrar_puntuaciones()
    assert resultado is not None, "La tabla debería manejar correctamente cuando no hay jugadores."

def test_actualizar_puntuacion_con_dato_invalido():
    puntuaciones = Puntuaciones()
    with pytest.raises(AttributeError):
        puntuaciones.actualizar_puntuacion(12345)