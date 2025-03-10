from src.model.campo import Campo

import pytest

#Pruebas Normales

def test_creacion_campo_dimensiones():
    campo = Campo(5, 5)
    assert len(campo.celdas) == 5
    assert len(campo.celdas[0]) == 5

def test_celdas_inicializadas():
   
    campo = Campo(5, 5)
    assert campo.celdas is not None

def test_campo_no_vacio():
    
    campo = Campo(5, 5)
    elementos = sum(1 for fila in campo.celdas for celda in fila if celda is not None)
    assert elementos > 0


#Pruebas Extremas

def test_campo_tamano_minimo():
    with pytest.raises(ValueError, match="El tamaño minimo del campo es 2 X 2"):
        Campo(1, 1)

def test_campo_tamano_maximo():
    with pytest.raises(ValueError, match="El tamaño minimo del campo es 20 X 20"):
        Campo(21, 21)

def test_campo_mas_naves_que_espacios():
    with pytest.raises(ValueError, match="No se pueden colocar más naves que casillas disponibles."):
        Campo(3, 3, 10)  

#Pruebas Error


def test_campo_valores_negativos():
    with pytest.raises(ValueError, match="No se permiten valores negativos para el ancho, alto o número de naves."):
        Campo(-5, 5, 3)

def test_campo_dimensiones_no_numericas():
    with pytest.raises(TypeError, match="El ancho, el alto y el número de naves deben ser enteros."):
        Campo("a", 5, 3) 

def test_campo_sin_naves():
    with pytest.raises(ValueError, match="Debe haber al menos una nave en el campo de juego."):
        Campo(5, 5, 0)