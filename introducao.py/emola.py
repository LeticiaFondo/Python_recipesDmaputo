print("Bem vindo a Movitel")
print("Emola\n"
      "1. e-Mola\n"
      "2. Elite Sempre Ligado\n"
      "3. Chamadas Movitel\n"
      "4. Liga Maning\n"
      "5. Internet\n"
      "6. Adois/Familiar/NetNoite\n"
      "7. SMS\n"
      "8. Shoo!\n"
      "9. Ilimitado\n"
      "10. Diversao\n"
      "11. My Movitel\n"
      "12. Language\n")

try:
    num = int(input("Digite uma opção: "))

    match num:
        case 1:
            print("1. Transferir para 86/87\n"
                  "2. Transferir para Mpesa/Mkesh\n"
                  "3. Transferir para o banco\n"
                  "4. Levantar\n"
                  "5. Comprar crédito\n"
                  "6. Voz&Internet\n"
                  "7. Xitique\n"
                  "8. CREDELEC\n"
                  "9. Pagamentos\n"
                  "10. Minha conta")

            num2 = int(input("Digite uma opcao: "))
            match num2:
                case 1:
                    numero = input("Digite o numero: ")
                    valor = input("Digite o valor: ")
                    pin = input("Digite o pin: ")
                    print(f"Deseja transferir {valor} MT para o numero {numero}\n"
                          "Para confirmar digite 1 e para cancelar digite 2:\n"
                          "1. Confirmar\n"
                          "2. Cancelar")
                    op = int(input("Digite a opcao: "))
                    if op == 1:
                        print(f"Confirmado, transferiste {valor} para o numero {numero}. Obrigado.")
                    elif op == 2:
                        print("Cancelado")
                    else:
                        print("Opcao invalida")

                case 2:
                    print("1. M-pesa\n"
                          "2. M-kesh")
                    op = int(input("Digite a opcao: "))

                    if op == 1:
                        numero = input("Digite o numero: ")
                        valor = input("Digite o valor: ")
                        pin = input("Digite o pin: ")

                        print(f"Deseja transferir {valor} MT para o numero {numero}\n"
                              "Digite 1 para confirmar e 2 para cancelar:\n"
                              "1. Confirmar\n"
                              "2. Cancelar")
                        op = int(input("Digite a opcao: "))
                        if op == 1:
                            print(f"Confirmado, transferiste {valor} para o numero {numero}. Obrigado.")
                        elif op == 2:
                            print("Cancelado")
                        else:
                            print("Opcao invalida")

                    elif op == 2:
                        numero = input("Digite o numero: ")
                        valor = input("Digite o valor: ")
                        pin = input("Digite o pin: ")

                        print(f"Deseja transferir {valor} MT para {numero}?")
                        op = int(input("Digite 1 para confirmar e 2 para cancelar: "))
                        if op == 1:
                            print(f"Confirmado, transferiste {valor} para {numero}.")
                        elif op == 2:
                            print("Cancelado")
                        else:
                            print("Opcao invalida")

                case 3:
                    print("1. BCI\n"
                          "2. Absa\n"
                          "3. BIM\n"
                          "4. Access\n"
                          "5. MOZA\n"
                          "6. Standart\n"
                          "7. FNB\n"
                          "8. NED\n"
                          "9. Favorito\n"
                          "10. SIMO-Conta Movel\n"
                          "#. Voltar")

                    num = int(input("Digite a opcao: "))
                    match num:
                        case 1:
                            nib = input("Digite o NIB: ")
                            valor = input("Digite o valor: ")
                            pin = input("Digite o pin: ")
                            print(
                                f"Deseja transferir {valor} MT para {nib}, para confirmar digite 1 e para cancelar digite 2:")
                            op = int(input("Digite a opcao: "))
                            if op == 1:
                                print(f"Confirmado, transferiste {valor} MT para a conta com o NIB {nib}.")
                            elif op == 2:
                                print("Cancelado")
                            else:
                                print("Opcao invalida")

                        case 2:
                            nib = input("Digite o NIB: ")
                            valor = input("Digite o valor: ")
                            pin = input("Digite o pin: ")
                            print(
                                f"Deseja transferir {valor} MT para {nib}, para confirmar digite 1 e para cancelar digite 2:")
                            op = int(input("Digite a opcao: "))
                            if op == 1:
                                print(f"Confirmado, transferiste {valor} MT para a conta com o NIB {nib}.")
                            elif op == 2:
                                print("Cancelado")
                            else:
                                print("Opcao invalida")

        case 2:
            print("1. Chamadas todas redes+*\n"
                  "2. Chamadas Movitel+*\n"
                  "3. Chamadas todas redes+*+**\n"
                  "4. Chamadas Movitel+*+**\n"
                  "0. Voltar\n"
                  "*=Dados+SMS todas as redes\n"
                  "**=Minutos internacionais+Dados Roaming")

        case 3:
            print("1. Horas\n"
                  "2. Bom dia\n"
                  "3. Diario\n"
                  "4. Semanal\n"
                  "5. Mensal\n"
                  "6. Infinito (sem validade)\n"
                  "7. Cancelar auto-renovacao\n"
                  "0. Voltar")

        case 4:
            print("1. Horas\n"
                  "2. Bom dia\n"
                  "3. Diario\n"
                  "4. Semanal\n"
                  "5. Mensal\n"
                  "6. Infinito\n"
                  "7. Cancelar auto-renovacao\n"
                  "0. Voltar")

        case 5:
            print("1. Elite dados\n"
                  "2. WFIYT\n"
                  "3. WFT\n"
                  "4. Whatsapp + Facebook\n"
                  "5. Whatsapp + YouTube\n"
                  "6. Whatsapp\n"
                  "7. Facebook\n"
                  "8. Instagram\n"
                  "9. YouTube\n"
                  "10. TikTok\n"
                  "11. Servico de dados\n"
                  "0. Voltar")

        case 6:
            print("1. Adois\n"
                  "2. Familiar\n"
                  "3. NetNoite (0-5h59)\n"
                  "0. Voltar")

        case 7:
            print("1. Diario\n"
                  "2. Semanal\n"
                  "3. Mensal\n"
                  "4. Cancelar auto-renovacao\n"
                  "0. Voltar")

        case 8:
            print("Coming soon")

        case 9:
            print("1. Infinito chamadas MOV +*\n"
                  "2. Ilimitado chamadas todas redes+*\n"
                  "0. voltar\n"
                  "*+=Dados+SMS todas redes ilimitado")

        case 10:
            print("1. Jogos\n"
                  "2. Utilitario\n"
                  "3. Conteudo\n"
                  "4. Entretenimento\n"
                  "5. Promocoes *155#\n"
                  "6. Emola *898#\n"
                  "7. Verifica teus servicos\n"
                  "8. Language")

        case _:  # Caso padrão
            print("Error")

except ValueError:
    print("Entrada inválida. Por favor, digite um número.")
