def validar_positivo(valor: float, nome: str) -> None:
    if valor<=0:
        raise ValueError(f"{nome} deve ser maior que zero.")

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
    return sum(resistores)
def paralelo(resistores: list[float]) -> float:
    if not resistores:
        raise ValueError("Lista vazia.")
    for r in resistores:
        validar_positivo(r, "Resistor")
    soma_inverso = sum(1/r for r in resistores)
    return 1 / soma_inverso if soma_inverso != 0 else 0

def potencia_vi(v: float, i: float) -> float:
    return v * i
def potencia_ri(r: float, i: float) -> float:
    return r * i**2
def potencia_vr(v: float, r: float) -> float:
    validar_positivo(r,"Resistência")
    return v**2 / r

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

def main() -> None:
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
main()