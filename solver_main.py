def calcular_tensao(r,i):
    return r*i
def calcular_corrente(v,r):
    return v/r
def calcular_resistencia(v, i):
    return v / i

def serie(resistores):
    return sum(resistores)
def paralelo(resistores):
    soma_inverso = sum(1/r for r in resistores)
    return 1 / soma_inverso if soma_inverso != 0 else 0

def potencia_vi(v, i):
    return v * i
def potencia_ri(r, i):
    return r * i**2
def potencia_vr(v, r):
    return v**2 / r

def menu():
    print("\n===================================")
    print("SOLUCIONADOR DE CIRCUITOS ELÉTRICOS")
    print("===================================")
    print("1 - Lei de Ohm")
    print("2 - Resistores em Série")
    print("3 - Resistores em Paralelo")
    print("4 - Potência Elétrica")
    print("5 - Sair")

def lei_de_ohm():
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
                        print("Tensão =", round(v, 2), "V")
                        break
                    except ValueError:
                        print("Erro: digite apenas números válidos!")

            case 2:
                while True:
                    try:
                        v = float(input("Digite a tensão (V): "))
                        r = float(input("Digite a resistência (Ω): "))
                        i = calcular_corrente(v,r)
                        print("Corrente =", round(i, 2), "A")
                        break
                    except ValueError:
                        print("Erro: digite apenas números válidos!")

            case 3:
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
                break

            case _:
                print("Opção inválida. Digite um número de 1 a 4.")

def resistor_serie():
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
                        print("Potência =", round(p, 2), "W")
                        break
                    except ValueError:
                        print("Erro: digite apenas números válidos!")

            case 2:
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

def main():
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