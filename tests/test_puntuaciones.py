import pytest
from src.model.puntuaciones import Puntuaciones
from src.model.jugador import Jugador

#  PRUEBAS NORMALES
def test_mostrar_puntuaciones():
    puntuaciones = Puntuaciones()
    try:
        puntuaciones.mostrar_puntuaciones()  
    except Exception as e:
        pytest.fail(f"La función mostrar_puntuaciones() lanzó un error: {e}")

def test_actualizar_puntuacion():
    puntuaciones = Puntuaciones()
    jugador = Jugador("Neo", "matrix123")
    jugador.actualizar_puntaje(50)
    puntuaciones.actualizar_puntuacion(jugador)
    assert any(j["nombre_usuario"] == "Neo" and j["puntaje"] == 50 for j in puntuaciones.lista_puntuaciones)

def test_mostrar_puntuaciones_sin_jugadores():
    puntuaciones = Puntuaciones()
    try:
        puntuaciones.mostrar_puntuaciones()
    except Exception as e:
        pytest.fail(f"La función mostrar_puntuaciones() lanzó un error con lista vacía: {e}")

#  PRUEBAS EXTREMAS
def test_muchos_jugadores():
    puntuaciones = Puntuaciones()
    for i in range(10000):
        jugador = Jugador(f"Jugador{i}", "pass")
        jugador.actualizar_puntaje(i)
        puntuaciones.actualizar_puntuacion(jugador)
    try:
        puntuaciones.mostrar_puntuaciones()
    except Exception as e:
        pytest.fail(f"Error con muchos jugadores: {e}")

def test_puntuaciones_con_puntaje_nulo():
    puntuaciones = Puntuaciones()
    jugador1 = Jugador("Jugador1", "pass")
    jugador2 = Jugador("Jugador2", "pass")
    jugador1.puntaje = None
    jugador2.puntaje = 500
    puntuaciones.actualizar_puntuacion(jugador1)
    puntuaciones.actualizar_puntuacion(jugador2)
    assert any(j["nombre_usuario"] == "Jugador1" and j["puntaje"] is None for j in puntuaciones.lista_puntuaciones)

def test_empate_puntajes():
    puntuaciones = Puntuaciones()
    for i in range(5):
        jugador = Jugador(f"Jugador{i}", "pass")
        jugador.actualizar_puntaje(100)
        puntuaciones.actualizar_puntuacion(jugador)
    try:
        puntuaciones.mostrar_puntuaciones()
    except Exception as e:
        pytest.fail(f"Error en la tabla de puntuaciones con empate: {e}")

#  PRUEBAS DE ERROR
def test_actualizar_puntuacion_sin_jugador():
    puntuaciones = Puntuaciones()
    with pytest.raises(AttributeError):  
        puntuaciones.actualizar_puntuacion(None)

def test_actualizar_puntuacion_con_dato_invalido():
    puntuaciones = Puntuaciones()
    with pytest.raises(AttributeError):  
        puntuaciones.actualizar_puntuacion(12345)

def test_mostrar_puntuaciones_sin_datos():  
    puntuaciones = Puntuaciones()
    try:
        puntuaciones.mostrar_puntuaciones()  
    except Exception as e:
        pytest.fail(f"Error al mostrar puntuaciones sin datos: {e}")
