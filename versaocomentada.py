# ================================
# SOLUCIONADOR DE CIRCUITOS ELÉTRICOS
# Aplicação de conceitos de Lei de Ohm,
# associação de resistores e potência elétrica.
#
# O código utiliza:
# - Type hints (tipagem estática opcional)
# - Validações com exceptions
# - Estrutura de menu interativo
# - Match/Case (Python 3.10+)
# ================================


# ================================
# FUNÇÃO DE VALIDAÇÃO
# ================================

def validar_positivo(valor: float, nome: str) -> None:
    """
    Garante que um valor seja maior que zero.
    
    :param valor: Número a ser validado
    :param nome: Nome da variável (para mensagem de erro)
    :raises ValueError: Se o valor for menor ou igual a zero
    """
    if valor <= 0:
        raise ValueError(f"{nome} deve ser maior que zero.")


# ================================
# LEI DE OHM
# ================================

def calcular_tensao(r: float, i: float) -> float:
    """Calcula a tensão usando V = R * i"""
    return r * i


def calcular_corrente(v: float, r: float) -> float:
    """Calcula a corrente usando i = V / R"""
    validar_positivo(r, "Resistência")
    return v / r


def calcular_resistencia(v: float, i: float) -> float:
    """Calcula a resistência usando R = V / i"""
    validar_positivo(i, "Corrente")
    return v / i


# ================================
# ASSOCIAÇÃO DE RESISTORES
# ================================

def serie(resistores: list[float]) -> float:
    """
    Calcula resistência equivalente em série.
    Req = R1 + R2 + R3 + ...
    """
    if not resistores:
        raise ValueError("Lista Vazia.")

    for r in resistores:
        validar_positivo(r, "Resistor")

    return sum(resistores)


def paralelo(resistores: list[float]) -> float:
    """
    Calcula resistência equivalente em paralelo.
    1/Req = 1/R1 + 1/R2 + ...
    """
    if not resistores:
        raise ValueError("Lista vazia.")

    for r in resistores:
        validar_positivo(r, "Resistor")

    soma_inverso = sum(1 / r for r in resistores)

    return 1 / soma_inverso if soma_inverso != 0 else 0


# ================================
# POTÊNCIA ELÉTRICA
# ================================

def potencia_vi(v: float, i: float) -> float:
    """Calcula potência usando P = V * i"""
    return v * i


def potencia_ri(r: float, i: float) -> float:
    """Calcula potência usando P = R * i²"""
    return r * i**2


def potencia_vr(v: float, r: float) -> float:
    """Calcula potência usando P = V² / R"""
    validar_positivo(r, "Resistência")
    return v**2 / r


# ================================
# MENU PRINCIPAL
# ================================

def menu() -> None:
    """Exibe o menu principal"""
    print("\n===================================")
    print("SOLUCIONADOR DE CIRCUITOS ELÉTRICOS")
    print("===================================")
    print("1 - Lei de Ohm")
    print("2 - Resistores em Série")
    print("3 - Resistores em Paralelo")
    print("4 - Potência Elétrica")
    print("5 - Sair")


# ================================
# SUBMENU LEI DE OHM
# ================================

def lei_de_ohm() -> None:
    """Menu interativo para cálculos da Lei de Ohm"""
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
                # Cálculo de tensão
                while True:
                    try:
                        r = float(input("Digite a resistência (Ω): "))
                        i = float(input("Digite a corrente (A): "))
                        v = calcular_tensao(r, i)
                        print(f"Tensão = {v:.2f} V")
                        break
                    except ValueError:
                        print("Erro: digite apenas números válidos!")

            case 2:
                # Cálculo de corrente
                while True:
                    try:
                        v = float(input("Digite a tensão (V): "))
                        r = float(input("Digite a resistência (Ω): "))
                        i = calcular_corrente(v, r)
                        print(f"Corrente = {i:.2f} A")
                        break
                    except ValueError:
                        print("Erro: digite apenas números válidos!")

            case 3:
                # Cálculo de resistência
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


# ================================
# SUBMENU RESISTORES EM SÉRIE
# ================================

def resistor_serie() -> None:
    """Entrada interativa para resistores em série"""
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


# ================================
# SUBMENU RESISTORES EM PARALELO
# ================================

def resistor_paralelo() -> None:
    """Entrada interativa para resistores em paralelo"""
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


# ================================
# SUBMENU POTÊNCIA
# ================================

def potencia() -> None:
    """Menu interativo para cálculos de potência elétrica"""
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


# ================================
# FUNÇÃO PRINCIPAL
# ================================

def main() -> None:
    """Loop principal da aplicação"""
    while True:
        menu()

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Erro: você deve digitar um número inteiro!")
            continue

        match opcao:
            case 1:
                lei_de_ohm()
            case 2:
                resistor_serie()
            case 3:
                resistor_paralelo()
            case 4:
                potencia()
            case 5:
                print("Saindo...")
                break
            case _:
                print("Opção inválida.")


# Executa o programa
main()
