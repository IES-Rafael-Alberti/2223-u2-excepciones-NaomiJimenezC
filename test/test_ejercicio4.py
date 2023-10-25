from src.ejercicio4 import *
import pytest

def test_comprobar_si_se_ingreso_un_numero_que_no_es():
    with pytest.raises(ValueError):
        comprobar_si_se_ingreso_un_numero("a")