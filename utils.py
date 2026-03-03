"""
Módulo utilitário.

Contém funções auxiliares usadas em diferentes partes do projeto.
"""

def validar_positivo(valor: float, nome: str) -> None:
    
    """
    Verifica se um valor é maior que zero.

    Parâmetros:
    - valor: número a ser validado
    - nome: nome da variável (usado na mensagem de erro)

    Lança:
    - ValueError se o valor for menor ou igual a zero.
    """
    
    if valor<=0:
        raise ValueError(f"{nome} deve ser maior que zero.")