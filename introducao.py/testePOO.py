class MenuPrincipal:
    def __init__(self):
        self.opcoes = {
            1: Emola,
            2: self.elite_sempre_ligado,
            3: self.chamadas_movitel,
            4: self.liga_maning,
            5: self.internet,
            6: self.adois_familiar_netnoite,
            7: self.sms,
            8: self.shoo,
            9: self.ilimitado,
            10: self.diversao,
            11: self.my_movitel,
            12: self.language
        }

    def mostrar_menu(self):
        print("Bem vindo a Movitel")
        print("Menu Principal:")
        for key, _ in self.opcoes.items():
            print(f"{key}. {self.opcoes[key].__name__ if callable(self.opcoes[key]) else key}")

        try:
            opcao = int(input("Digite uma opção: "))
            if opcao in self.opcoes:
                self.opcoes[opcao]()  # Chama a opção escolhida
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    def elite_sempre_ligado(self):
        print("Opções Elite Sempre Ligado...")

    def chamadas_movitel(self):
        print("Opções Chamadas Movitel...")

    def liga_maning(self):
        print("Opções Liga Maning...")

    def internet(self):
        print("Opções de Internet...")

    def adois_familiar_netnoite(self):
        print("Opções Adois/Familiar/NetNoite...")

    def sms(self):
        print("Opções de SMS...")

    def shoo(self):
        print("Opções de Shoo...")

    def ilimitado(self):
        print("Opções de Ilimitado...")

    def diversao(self):
        print("Opções de Diversão...")

    def my_movitel(self):
        print("Opções My Movitel...")

    def language(self):
        print("Opções de Language...")


class Emola:
    def __init__(self):
        self.opcoes_emola = {
            1: self.transferir_movitel,
            2: self.transferir_mpesa_mkesh,
            3: self.transferir_banco,
            4: self.levantar,
            5: self.comprar_credito,
            6: self.voz_internet,
            7: self.xitique,
            8: self.credelec,
            9: self.pagamentos,
            10: self.minha_conta
        }
        self.mostrar_menu_emola()

    def mostrar_menu_emola(self):
        print("Menu e-Mola:")
        for key, value in self.opcoes_emola.items():
            print(f"{key}. {value.__name__.replace('_', ' ')}")

        try:
            opcao = int(input("Digite uma opção: "))
            if opcao in self.opcoes_emola:
                self.opcoes_emola[opcao]()  # Chama a opção escolhida
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    def transferir_movitel(self):
        numero = input("Digite o numero: ")
        valor = input("Digite o valor: ")
        pin = input("Digite o pin: ")
        print(f"Deseja transferir {valor} MT para o número {numero}")
        print("1. Confirmar\n2. Cancelar")
        op = int(input("Digite a opcao: "))
        if op == 1:
            print(f"Confirmado, transferiste {valor} para o número {numero}. Obrigado.")
        elif op == 2:
            print("Cancelado")
        else:
            print("Opção inválida")

    def transferir_mpesa_mkesh(self):
        print("1. M-pesa\n2. M-kesh")
        opcao = int(input("Digite a opção: "))
        numero = input("Digite o número: ")
        valor = input("Digite o valor: ")
        pin = input("Digite o pin: ")
        print(f"Deseja transferir {valor} MT para o número {numero}")
        print("1. Confirmar\n2. Cancelar")
        op = int(input("Digite a opção: "))
        if op == 1:
            print(f"Confirmado, transferiste {valor} para o número {numero}. Obrigado.")
        elif op == 2:
            print("Cancelado")
        else:
            print("Opção inválida")

    def transferir_banco(self):
        print("Escolha o banco:")
        print(
            "1. BCI\n2. Absa\n3. BIM\n4. Access\n5. MOZA\n6. Standard\n7. FNB\n8. NED\n9. Favorito\n10. SIMO-Conta Móvel")
        banco_op = int(input("Digite a opção: "))
        nib = input("Digite o NIB: ")
        valor = input("Digite o valor: ")
        pin = input("Digite o pin: ")
        print(f"Deseja transferir {valor} MT para a conta NIB {nib}")
        print("1. Confirmar\n2. Cancelar")
        op = int(input("Digite a opção: "))
        if op == 1:
            print(f"Confirmado, transferiste {valor} para o NIB {nib}. Obrigado.")
        elif op == 2:
            print("Cancelado")
        else:
            print("Opção inválida")

    def levantar(self):
        print("Função de levantamento")

    def comprar_credito(self):
        print("Função de compra de crédito")

    def voz_internet(self):
        print("Função de Voz & Internet")

    def xitique(self):
        print("Função de Xitique")

    def credelec(self):
        print("Função de CREDELEC")

    def pagamentos(self):
        print("Função de Pagamentos")

    def minha_conta(self):
        print("Função de Minha Conta")

class Elite_sempre_ligado:
    def __init__(self):
        self.opcoes_elite_sempre_ligado = {
            1: self.Chamadas_todas_redes,
            2: self.Chamadas_Movitel,
            3: self.Chamadas_todas_redes2,
            4: self.Chamadas_Movitel2,
            5: self.Dados_SMS_todasRedes,
            6: self.MinutosInternacionais_DadosRoaming,
            0: self.Voltar,
        }
        self.Mostrar_menu_elite_sempre_ligado()


# Inicializando o Menu Principal
if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.mostrar_menu()
