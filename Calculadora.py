# CALCULADORA DE ELETRICIDADE


class CalculadoraEletricidade:

    # Construtor da classe
    def __init__(self):
        # Lista utilizada para armazenar o histórico
        self.historico = []

        # Dicionário contendo materiais e suas resistividades
        self.materiais = {
            "Cobre": 1.68e-8,
            "Alumínio": 2.82e-8,
            "Prata": 1.59e-8
        }

   
    # PRIMEIRA LEI DE OHM
   

    # Calcula a tensão:
    def calcular_tensao(self, resistencia, corrente):
        return resistencia * corrente

    # Calcula a corrente:
    def calcular_corrente(self, tensao, resistencia):
        if resistencia == 0:
            raise ZeroDivisionError("A resistência não pode ser zero.")

        return tensao / resistencia

    # Calcula a resistência:
    def calcular_resistencia(self, tensao, corrente):
        if corrente == 0:
            raise ZeroDivisionError("A corrente não pode ser zero.")

        return tensao / corrente

       
    # SEGUNDA LEI DE OHM
   

    # Calcula a resistência: R = ρ * L / A
   
    def segunda_lei_ohm(self, resistividade, comprimento, area=0.000001):

        if area == 0:
            raise ZeroDivisionError("A área não pode ser zero.")

        return resistividade * comprimento / area

   
    # POTÊNCIA ELÉTRICA
   

    # Calcula P = V * I
    def potencia_tensao_corrente(self, tensao, corrente):
        return tensao * corrente

    # Calcula P = R * I²
    def potencia_resistencia_corrente(self, resistencia, corrente):
        return resistencia * (corrente ** 2)

    # Calcula P = V² / R
    def potencia_tensao_resistencia(self, tensao, resistencia):

        if resistencia == 0:
            raise ZeroDivisionError("A resistência não pode ser zero.")

        return (tensao ** 2) / resistencia



# FUNÇÃO PARA LER NÚMEROS


def ler_numero(self):

    while True:
        try:
            valor = float(input(self))
            return valor

        except ValueError:
            print("\nEntrada inválida! Digite um valor numérico.\n")



# PRIMEIRA LEI DE OHM


def menu_primeira_lei(calculadora):

    while True:

        print("\n========================================")
        print("        PRIMEIRA LEI DE OHM")
        print("========================================")
        print("1 - Calcular tensão (V)")
        print("2 - Calcular corrente (I)")
        print("3 - Calcular resistência (R)")
        print("0 - Voltar ao menu principal")

        opcao = input("\nEscolha uma opção: ")

        try:

            if opcao == "1":

                resistencia = ler_numero(
                    "Digite a resistência (ohms): "
                )

                corrente = ler_numero(
                    "Digite a corrente (A): "
                )

                tensao = calculadora.calcular_tensao(
                    resistencia,
                    corrente
                )

                print(f"\nTensão calculada: {tensao} V")

                # Armazena a operação no histórico
                calculadora.historico.append(
                    f"Primeira Lei de Ohm - "
                    f"V = {tensao} V, "
                    f"R = {resistencia} Ω, "
                    f"I = {corrente} A"
                )

            elif opcao == "2":

                tensao = ler_numero(
                    "Digite a tensão (V): "
                )

                resistencia = ler_numero(
                    "Digite a resistência (ohms): "
                )

                corrente = calculadora.calcular_corrente(
                    tensao,
                    resistencia
                )

                print(f"\nCorrente calculada: {corrente} A")

                calculadora.historico.append(
                    f"Primeira Lei de Ohm - "
                    f"I = {corrente} A, "
                    f"V = {tensao} V, "
                    f"R = {resistencia} Ω"
                )

            elif opcao == "3":

                tensao = ler_numero(
                    "Digite a tensão (V): "
                )

                corrente = ler_numero(
                    "Digite a corrente (A): "
                )

                resistencia = calculadora.calcular_resistencia(
                    tensao,
                    corrente
                )

                print(f"\nResistência calculada: {resistencia} Ω")

                calculadora.historico.append(
                    f"Primeira Lei de Ohm - "
                    f"R = {resistencia} Ω, "
                    f"V = {tensao} V, "
                    f"I = {corrente} A"
                )

            elif opcao == "0":
                break

            else:
                print("\nOpção inválida!")

        except ZeroDivisionError as erro:
            print(f"\nErro: {erro}")



# SEGUNDA LEI DE OHM


def menu_segunda_lei(calculadora):

    while True:

        print("\n========================================")
        print("         SEGUNDA LEI DE OHM")
        print("========================================")

        print("\nMateriais disponíveis:")
        print("1 - Cobre")
        print("2 - Alumínio")
        print("3 - Prata")
        print("4 - Outro material")
        print("0 - Voltar ao menu principal")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
            break

        # Escolha do material
        if opcao == "1":
            material = "Cobre"
            resistividade = calculadora.materiais[material]

        elif opcao == "2":
            material = "Alumínio"
            resistividade = calculadora.materiais[material]

        elif opcao == "3":
            material = "Prata"
            resistividade = calculadora.materiais[material]

        elif opcao == "4":
            material = "Outro material"

            resistividade = ler_numero(
                "Digite a resistividade (ohm.m): "
            )

        else:
            print("\nMaterial inválido!")
            continue

        comprimento = ler_numero(
            "Digite o comprimento do condutor (m): "
        )

        area = ler_numero(
            "Digite a área da seção transversal (m²): "
        )

        try:

            resistencia = calculadora.segunda_lei_ohm(
                resistividade,
                comprimento,
                area
            )

            print(
                f"\nResistência do condutor: "
                f"{resistencia} Ω"
            )

            calculadora.historico.append(
                f"Segunda Lei de Ohm - "
                f"Material = {material}, "
                f"ρ = {resistividade} Ω.m, "
                f"L = {comprimento} m, "
                f"A = {area} m², "
                f"R = {resistencia} Ω"
            )

        except ZeroDivisionError as erro:
            print(f"\nErro: {erro}")



# POTÊNCIA ELÉTRICA


def menu_potencia(cal):

    while True:

        print("\n========================================")
        print("          POTÊNCIA ELÉTRICA")
        print("========================================")

        print("1 - Potência a partir de tensão e corrente")
        print("2 - Potência a partir de resistência e corrente")
        print("3 - Potência a partir de tensão e resistência")
        print("0 - Voltar ao menu principal")

        escolha = input("\nEscolha uma opção: ")

        try:

            if escolha == "1":

                tensao = ler_numero(
                    "Digite a tensão (V): "
                )

                corrente = ler_numero(
                    "Digite a corrente (A): "
                )

                potencia = cal.potencia_tensao_corrente(
                    tensao,
                    corrente
                )

                print(
                    f"\nPotência elétrica: {potencia} W"
                )

                cal.historico.append(
                    f"Potência Elétrica - "
                    f"V = {tensao} V, "
                    f"I = {corrente} A, "
                    f"P = {potencia} W"
                )

            elif escolha == "2":

                resistencia = ler_numero(
                    "Digite a resistência (ohms): "
                )

                corrente = ler_numero(
                    "Digite a corrente (A): "
                )

                potencia = calculadora.potencia_resistencia_corrente(
                    resistencia,
                    corrente
                )

                print(
                    f"\nPotência elétrica: {potencia} W"
                )

                calculadora.historico.append(
                    f"Potência Elétrica - "
                    f"R = {resistencia} Ω, "
                    f"I = {corrente} A, "
                    f"P = {potencia} W"
                )

            elif escolha == "3":

                tensao = ler_numero(
                    "Digite a tensão (V): "
                )

                resistencia = ler_numero(
                    "Digite a resistência (ohms): "
                )

                potencia = calculadora.potencia_tensao_resistencia(
                    tensao,
                    resistencia
                )

                print(
                    f"\nPotência elétrica: {potencia} W"
                )

                calculadora.historico.append(
                    f"Potência Elétrica - "
                    f"V = {tensao} V, "
                    f"R = {resistencia} Ω, "
                    f"P = {potencia} W"
                )

            elif escolha == "0":
                break

            else:
                print("\nOpção inválida!")

        except ZeroDivisionError as erro:
            print(f"\nErro: {erro}")



# HISTÓRICO


def mostrar_historico(calculadora):

    print("\n========================================")
    print("          HISTÓRICO DE CÁLCULOS")
    print("========================================")

    if len(calculadora.historico) == 0:

        print("\nNenhum cálculo foi realizado.")

    else:

        for i, calculo in enumerate(
            calculadora.historico,
            start=1
        ):

            print(f"\n{i}. {calculo}")


# ========================================
# MENU PRINCIPAL
# ========================================

def menu_principal():

    # Criação do objeto da classe
    calculadora = CalculadoraEletricidade()

    while True:

        print("\n")
        print("========================================")
        print("       CALCULADORA DE ELETRICIDADE")
        print("========================================")
        print()
        print("1 - Primeira Lei de Ohm")
        print("2 - Segunda Lei de Ohm")
        print("3 - Potência Elétrica")
        print("4 - Histórico de cálculos")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            menu_primeira_lei(calculadora)

        elif opcao == "2":

            menu_segunda_lei(calculadora)

        elif opcao == "3":

            menu_potencia(calculadora)

        elif opcao == "4":

            mostrar_historico(calculadora)

        elif opcao == "0":

            print("\nPrograma encerrado.")
            break

        else:

            print("\nOpção inválida! Digite uma opção disponível.")



# INÍCIO DO PROGRAMA
