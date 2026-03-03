"""
Arquivo principal do projeto.

Responsável por iniciar o programa e controlar
o fluxo do menu principal.
"""

from interface import *

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


# Executa o programa apenas se este arquivo
# for executado diretamente
if __name__ == "__main__":
    main()