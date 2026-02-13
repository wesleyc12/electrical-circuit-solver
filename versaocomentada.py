# ==========================================
# SOLUCIONADOR DE CIRCUITOS ELÉTRICOS
# ==========================================
# Programa para calcular:
# - Tensão, corrente e resistência (Lei de Ohm)
# - Resistores em série e paralelo
# - Potência elétrica
# ==========================================

# -----------------------------
# FUNÇÕES AUXILIARES
# -----------------------------

def calcular_tensao(r, i):
    """
    Calcula a tensão usando a Lei de Ohm: V = R * I

    Parâmetros:
    r (float): resistência em ohms
    i (float): corrente em amperes

    Retorna:
    float: tensão em volts
    """
    return r * i

def calcular_corrente(v, r):
    """
    Calcula a corrente usando a Lei de Ohm: I = V / R
    """
    return v / r

def calcular_resistencia(v, i):
    """
    Calcula a resistência usando a Lei de Ohm: R = V / I
    """
    return v / i

def serie(resistores):
    """
    Calcula a resistência equivalente de resistores em série.

    Parâmetros:
    resistores (list): lista de valores de resistores em ohms

    Retorna:
    float: resistência equivalente em ohms
    """
    return sum(resistores)

def paralelo(resistores):
    """
    Calcula a resistência equivalente de resistores em paralelo.

    Parâmetros:
    resistores (list): lista de valores de resistores em ohms

    Retorna:
    float: resistência equivalente em ohms
    """
    soma_inverso = sum(1 / r for r in resistores)
    return 1 / soma_inverso if soma_inverso != 0 else 0

def potencia_vi(v, i):
    """Calcula potência usando P = V * I"""
    return v * i

def potencia_ri(r, i):
    """Calcula potência usando P = R * I^2"""
    return r * i**2

def potencia_vr(v, r):
    """Calcula potência usando P = V^2 / R"""
    return v**2 / r

# -----------------------------
# FUNÇÃO DE MENU PRINCIPAL
# -----------------------------

def menu():
    """Exibe o menu principal do solucionador de circuitos"""
    print("\n===================================")
    print("SOLUCIONADOR DE CIRCUITOS ELÉTRICOS")
    print("===================================")
    print("1 - Lei de Ohm")
    print("2 - Resistores em Série")
    print("3 - Resistores em Paralelo")
    print("4 - Potência Elétrica")
    print("5 - Sair")

# -----------------------------
# FUNÇÕES DE CÁLCULO
# -----------------------------

def lei_de_ohm():
    """Menu para cálculos da Lei de Ohm"""
    while True:
        print("\n===== LEI DE OHM =====")
        print("1 - Calcular Tensão (V)")
        print("2 - Calcular Corrente (i)")
        print("3 - Calcular Resistência (R)")
        print("4 - Voltar")
        
        # Valida a opção do usuário
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
                        print("Tensão =", round(v, 2), "V")
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
                        print("Corrente =", round(i, 2), "A")
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
                        print("Resistência =", round(r, 2), "Ω")
                        break
                    except ValueError:
                        print("Erro: digite apenas números válidos!")

            case 4:
                # Volta para o menu principal
                break

            case _:
                print("Opção inválida. Digite um número de 1 a 4.")

def resistor_serie():
    """Calcula resistência equivalente de resistores em série"""
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
    
    resistencia_equivalente = serie(resistores)
    print("Resistência equivalente =", round(resistencia_equivalente, 2), "Ω")
    
def resistor_paralelo():
    """Calcula resistência equivalente de resistores em paralelo"""
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
    
    resistencia_equivalente = paralelo(resistores)
    print("Resistência equivalente =", round(resistencia_equivalente, 2), "Ω")

def potencia():
    """Menu para cálculos de potência elétrica"""
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
                # P = V * I
                while True:
                    try:
                        v = float(input("Tensão (V): "))
                        i = float(input("Corrente (A): "))
                        p = potencia_vi(v, i)
                        print("Potência =", round(p, 2), "W")
                        break
                    except ValueError:
                        print("Erro: digite apenas números válidos!")

            case 2:
                # P = R * I^2
                while True:
                    try:
                        r = float(input("Resistência (Ω): "))
                        i = float(input("Corrente (A): "))
                        p = potencia_ri(r, i)
                        print("Potência =", round(p, 2), "W")
                        break
                    except ValueError:
                        print("Erro: digite apenas números válidos!")

            case 3:
                # P = V^2 / R
                while True:
                    try:
                        v = float(input("Tensão (V): "))
                        r = float(input("Resistência (Ω): "))
                        p = potencia_vr(v, r)
                        print("Potência =", round(p, 2), "W")
                        break
                    except ValueError:
                        print("Erro: digite apenas números válidos!")

            case 4:
                break

            case _:
                print("Opção inválida. Digite um número de 1 a 4.")

# -----------------------------
# FUNÇÃO PRINCIPAL
# -----------------------------
def main():
    """Executa o loop principal do programa"""
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
