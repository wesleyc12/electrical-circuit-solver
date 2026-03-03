"""
Módulo responsável pelos cálculos elétricos.

Inclui:
- Lei de Ohm
- Associação de resistores (série e paralelo)
- Cálculo de potência elétrica
"""

from utils import validar_positivo

def calcular_tensao(r: float,i:float) -> float:
    return r*i
def calcular_corrente(v: float,r: float) -> float:
    validar_positivo(r,"Resistência")
    return v/r
def calcular_resistencia(v: float, i: float) -> float:
    validar_positivo(i,"Corrente")
    return v / i

def serie(resistores: list[float]) -> float:
    if not resistores:
        raise ValueError("Lista Vazia.")
    for r in resistores:
        validar_positivo(r,"Resistor")
    return sum(resistores) # Resistência equivalente com os resistores em série se dá pelo somatório dos resistores
def paralelo(resistores: list[float]) -> float:
    if not resistores:
        raise ValueError("Lista vazia.")
    for r in resistores:
        validar_positivo(r, "Resistor")
    soma_inverso = sum(1/r for r in resistores) # Resistência equivalente com os resistores em paralelo se dá pelo somatório do inverso dos resistores
    return 1 / soma_inverso if soma_inverso != 0 else 0

def potencia_vi(v: float, i: float) -> float:
    return v * i
def potencia_ri(r: float, i: float) -> float:
    return r * i**2
def potencia_vr(v: float, r: float) -> float:
    validar_positivo(r,"Resistência")
    return v**2 / r