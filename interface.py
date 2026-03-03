"""
Módulo de interface com o usuário.

Responsável por:
- Exibir menus
- Receber entradas
- Mostrar resultados
- Tratar erros de entrada

"""

from calculos import *

def menu() -> None:
    print("\n===================================")
    print("SOLUCIONADOR DE CIRCUITOS ELÉTRICOS")
    print("===================================")
    print("1 - Lei de Ohm")
    print("2 - Resistores em Série")
    print("3 - Resistores em Paralelo")
    print("4 - Potência Elétrica")
    print("5 - Sair")

def lei_de_ohm() -> None:
    
    """
    Submenu para cálculos relacionados à Lei de Ohm.
    Permite calcular tensão, corrente ou resistência.
    
    """

    while True:
        print("\n===== LEI DE OHM =====")
        print("1 - Calcular Tensão (V)")
        print("2 - Calcular Corrente (i)")
        print("3 - Calcular Resistência (R)")
        print("4 - Voltar")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Erro: você deve digitar um número inteiro de 1 a 4!")
            continue

        match opcao:
            case 1:
                while True:
                    try:
                        r = float(input("Digite a resistência (Ω): "))
                        i = float(input("Digite a corrente (A): "))
                        v = calcular_tensao(r,i)
                        print(f"Tensão = {v:.2f} V")
                        break
                    except ValueError:
                        print("Erro: digite apenas números válidos!")

            case 2:
                while True:
                    try:
                        v = float(input("Digite a tensão (V): "))
                        r = float(input("Digite a resistência (Ω): "))
                        i = calcular_corrente(v,r)
                        print(f"Corrente = {i:.2f} A")
                        break
                    except ValueError:
                        print("Erro: digite apenas números válidos!")

            case 3:
                while True:
                    try:
                        v = float(input("Digite a tensão (V): "))
                        i = float(input("Digite a corrente (A): "))
                        r = calcular_resistencia(v, i)
                        print(f"Resistência = {r:.2f} Ω")
                        break
                    except ValueError:
                        print("Erro: digite apenas números válidos!")

            case 4:
                break

            case _:
                print("Opção inválida. Digite um número de 1 a 4.")

def resistor_serie() -> None:
    
    """
    Submenu para o cálculo relacionado à Resistência equivalente.
    Neste caso, com os resistores em série.
    
    """
    
    print("\n===== RESISTORES EM SÉRIE =====")
    print("Digite os valores dos resistores. Para terminar, digite 0.")
    
    resistores = []
    while True:
        try:
            r = float(input("Resistor (Ω): "))
            if r == 0:
                break
            resistores.append(r)
        except ValueError:
            print("Erro: digite apenas números válidos!")
    
    try:
        resistencia_equivalente = serie(resistores)
        print(f"Resistência equivalente = {resistencia_equivalente:.2f} Ω")
    except ValueError as erro:
        print(f"Erro: {erro}")

def resistor_paralelo()-> None:
    
    """
    Submenu para o cálculo relacionado à Resistência equivalente.
    Neste caso, com os resistores em paralelo.
    
    """
    
    print("\n===== RESISTORES EM PARALELO =====")
    print("Digite os valores dos resistores. Para terminar, digite 0.")
    
    resistores = []
    while True:
        try:
            r = float(input("Resistor (Ω): "))
            if r == 0:
                break
            resistores.append(r)
        except ValueError:
            print("Erro: digite apenas números válidos!")
    try:
        resistencia_equivalente = paralelo(resistores)
        print(f"Resistência equivalente = {resistencia_equivalente:.2f} Ω")
    except ValueError as erro:
        print(f"Erro: {erro}")

def potencia() -> None:
    
    """
    Submenu para cálculos relacionados à Potência.
    Podemos calcular usando as variáveis Tensão, Corrente e Resistência.
    
    """
    
    while True:
        print("\n===== POTÊNCIA ELÉTRICA =====")
        print("1 - Calcular P a partir de V e i")
        print("2 - Calcular P a partir de R e i")
        print("3 - Calcular P a partir de V e R")
        print("4 - Voltar")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Erro: digite um número inteiro de 1 a 4!")
            continue

        match opcao:
            case 1:
                while True:
                    try:
                        v = float(input("Tensão (V): "))
                        i = float(input("Corrente (A): "))
                        p = potencia_vi(v, i)
                        print(f"Potência = {p:.2f} W")
                        break
                    except ValueError:
                        print("Erro: digite apenas números válidos!")

            case 2:
                while True:
                    try:
                        r = float(input("Resistência (Ω): "))
                        i = float(input("Corrente (A): "))
                        p = potencia_ri(r, i)
                        print(f"Potência = {p:.2f} W")
                        break
                    except ValueError:
                        print("Erro: digite apenas números válidos!")

            case 3:
                while True:
                    try:
                        v = float(input("Tensão (V): "))
                        r = float(input("Resistência (Ω): "))
                        p = potencia_vr(v, r)
                        print(f"Potência = {p:.2f} W")
                        break
                    except ValueError:
                        print("Erro: digite apenas números válidos!")

            case 4:
                break

            case _:
                print("Opção inválida. Digite um número de 1 a 4.")