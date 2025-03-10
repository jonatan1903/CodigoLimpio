import pytest

from src.model.campo import Campo
from src.model.celda import Celda

#Pruebas normales 

def test_disparo_repetido_en_misma_celda():
    campo = Campo(5, 5, 3)
    campo.celdas[2][2] = Celda(tiene_nave=True)
    campo.VerificarImpacto(2, 2)
    assert campo.VerificarImpacto(2, 2)

def test_disparo_en_celda_sin_nave():
    campo = Campo(5, 5, 3)  
    resultado = campo.VerificarImpacto(2, 2)  
    assert resultado == False

def test_disparo_en_celda_con_nave():
    campo = Campo(5, 5, 3)
    campo.celdas[1][1] = None  
    with pytest.raises(AttributeError):
        campo.VerificarImpacto(1, 1)

#Pruebas extremas 

def test_disparo_en_borde_superior_grande():
    campo = Campo(10, 10, 5)
    with pytest.raises(AttributeError):
        campo.VerificarImpacto(0, 5)

def test_disparo_en_borde_inferior_pequeno():
    campo = Campo(3, 3, 2)
    with pytest.raises(AttributeError):
        campo.VerificarImpacto(2, 1)

def test_disparo_en_campo_grande():
    campo = Campo(50, 50, 20)
    with pytest.raises(AttributeError):
        campo.VerificarImpacto(25, 25)

#Pruebas Error 

def test_disparo_en_celda_fuera_de_margen():
    campo = Campo(5, 5, 3)
    with pytest.raises(ValueError, match="Disparo fuera de los limites"):
        campo.VerificarImpacto(5, 5)


def test_disparo_en_misma_celda():
    campo = Campo(5, 5, 3)
    campo.celdas[2][2] = Celda(tiene_nave=True)
    campo.VerificarImpacto(2, 2)  
    with pytest.raises(ValueError, match="Esta celda ya ha sido impactada"):
        campo.VerificarImpacto(2, 2)  

def test_disparo_con_valores_no_enteros():
    campo = Campo(5, 5, 3)
    with pytest.raises(TypeError, match="Las coordenadas deben ser enteros"):
        campo.VerificarImpacto("dos", 3) 