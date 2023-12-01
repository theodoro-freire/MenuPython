# # Lista para armazenar cadastros
# cadastros = []

# # Explicação sobre nossa equipe e solução.
# def exibir_equipe_e_solucao():
#     print("Equipe: [Nomes dos membros da equipe]")
#     print("Solução: [Descrição da solução]")
#     input("Pressione Enter para voltar ao menu principal.")

# # Menu secundário de cadastro
# def cadastrar_atualizar_excluir_ver():
#     while True:
#         print("\nMenu de Cadastro:")
#         print("1. Cadastrar")
#         print("2. Atualizar")
#         print("3. Excluir")
#         print("4. Ver Cadastro")
#         print("0. Voltar ao menu principal")

#         opcao = input("Escolha uma opção: ")

#         if opcao == "1":
#             cadastrar()
#         elif opcao == "2":
#             atualizar()
#         elif opcao == "3":
#             excluir()
#         elif opcao == "4":
#             ver_cadastro()
#         elif opcao == "0":
#             break
#         else:
#             print("Opção inválida. Tente novamente.")

# def cadastrar():
#     print("\nCadastro de Novo Usuário:")
#     nome = input("Digite seu nome: ")
#     idade = input("Digite sua idade: ")
#     email = input("Digite seu email: ")
#     senha = input("Digite sua senha: ")

#     # Adiciona as informações à lista de cadastros
#     cadastros.append({"nome": nome, "idade": idade, "email": email, "senha": senha})

#     print("Cadastro realizado com sucesso!")

# def atualizar():
#     print("\nAtualização de Cadastro:")
#     email_atualizar = input("Digite o email do cadastro a ser atualizado: ")

#     # Procura o cadastro na lista e atualiza as informações
#     for cadastro in cadastros:
#         if cadastro["email"] == email_atualizar:
#             cadastro["idade"] = input("Digite a nova idade: ")
#             cadastro["senha"] = input("Digite a nova senha: ")
#             print("Cadastro atualizado com sucesso!")

# def excluir():
#     print("\nExclusão de Cadastro:")
#     email_excluir = input("Digite o email do cadastro a ser excluído: ")

#     # Remove o cadastro da lista
#     for cadastro in cadastros:
#         if cadastro["email"] == email_excluir:
#             cadastros.remove(cadastro)
#             print("Cadastro excluído com sucesso!")

# def ver_cadastro():
#     print("\nConsulta de Cadastro:")
#     email_consulta = input("Digite o email do cadastro a ser consultado: ")

#     # Exibe as informações do cadastro
#     for cadastro in cadastros:
#         if cadastro["email"] == email_consulta:
#             print(f"Nome: {cadastro['nome']}, Idade: {cadastro['idade']}, Email: {cadastro['email']}")
#             break
#     else:
#         print("Cadastro não encontrado.")

# def verificar_solucao():
#     print("\nVerificação de Valores:")
#     batimentos = int(input("Digite os batimentos por minuto: "))
#     saturacao = int(input("Digite a saturação: "))
#     freq_respiratoria = int(input("Digite a frequência respiratória: "))
#     pressao = int(input("Digite a pressão: "))

#     if batimentos > 100:
#         print("Batimentos altos! Risco de taquicardia. Procure um médico.")
#     elif batimentos < 50:
#         print("Batimentos baixos! Risco de bradicardia. Procure um médico.")

#     if saturacao < 90:
#         print("Saturação baixa! Possível falta de oxigênio. Procure um médico.")

#     if freq_respiratoria < 12:
#         print("Frequência respiratória baixa! Risco de bradipneia. Procure um médico.")
#     elif freq_respiratoria > 20:
#         print("Frequência respiratória alta! Risco de taquipneia. Procure um médico.")

#     if pressao > 140:
#         print("Pressão alta! Procure um médico.")
#     elif pressao < 90:
#         print("Pressão baixa! Procure um médico.")

#     if 50 <= batimentos <= 100 and saturacao >= 90 and 12 <= freq_respiratoria <= 20 and 90 <= pressao <= 140:
#         print("Tudo está bem!")

# def menu_principal():
#     while True:
#         print("\nMenu Principal:")
#         print("1. Informações sobre a equipe e solução")
#         print("2. Cadastro")
#         print("3. Verificar Solução")
#         print("0. Sair")

#         opcao = input("Escolha uma opção: ")

#         if opcao == "1":
#             exibir_equipe_e_solucao()
#         elif opcao == "2":
#             cadastrar_atualizar_excluir_ver()
#         elif opcao == "3":
#             verificar_solucao()
#         elif opcao == "0":
#             print("Obrigado por usar o sistema. Até logo!")
#             break
#         else:
#             print("Opção inválida. Tente novamente.")

# if __name__ == "__main__":
#     menu_principal()


# Lista para armazenar cadastros
cadastros = []

# Explicação sobre nossa equipe e solução.
def exibir_equipe_e_solucao():
    print("\nEquipe: [Nomes dos membros da equipe]")
    print("\nSolução: [Descrição da solução]")
    input("\nPressione Enter para voltar ao menu principal.")

# Menu secundário de cadastro
def cadastrar_atualizar_excluir_ver(cadastros, nome, idade, email, senha):
    while True:
        print("\nMenu de Cadastro:")
        print("1. Cadastrar")
        print("2. Atualizar")
        print("3. Excluir")
        print("4. Ver Cadastro")
        print("0. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("\nDigite seu nome: ")
            idade = input("\nDigite sua idade: ")
            email = input("\nDigite seu email: ")
            senha = input("\nDigite sua senha: ")
            cadastrar(cadastros, nome, idade, email, senha)
        elif opcao == "2":
            atualizar(cadastros)
        elif opcao == "3":
            excluir(cadastros)
        elif opcao == "4":
            ver_cadastro(cadastros)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def cadastrar(cadastros, nome, idade, email, senha):
    # Adiciona as informações à lista de cadastros
    cadastros.append({"nome": nome, "idade": idade, "email": email, "senha": senha})
    print("Cadastro realizado com sucesso!")

def atualizar(cadastros):
    print("\nAtualização de Cadastro:")
    email_atualizar = input("\nDigite o email do cadastro a ser atualizado (ou digite 0 para sair): ")

    if email_atualizar == "0":
        return

    # Procura o cadastro na lista e atualiza as informações
    for cadastro in cadastros:
        if cadastro["email"] == email_atualizar:
            cadastro["idade"] = input("Digite a nova idade: ")
            cadastro["senha"] = input("Digite a nova senha: ")
            print("Cadastro atualizado com sucesso!")
            return  # Adiciona um return para sair da função após a atualização

    # Se o email não for encontrado
    print("Cadastro não encontrado.")

def excluir(cadastros):
    print("\nExclusão de Cadastro:")
    email_excluir = input("Digite o email do cadastro a ser excluído (ou digite 0 para sair): ")

    if email_excluir == "0":
        return

    # Remove o cadastro da lista
    for cadastro in cadastros:
        if cadastro["email"] == email_excluir:
            cadastros.remove(cadastro)
            print("Cadastro excluído com sucesso!")
            return  # Adiciona um return para sair da função após a exclusão

    # Se o email não for encontrado
    print("Cadastro não encontrado.")

def ver_cadastro(cadastros):
    print("\nConsulta de Cadastro:")
    email_consulta = input("Digite o email do cadastro a ser consultado (ou digite 0 para sair): ")

    if email_consulta == "0":
        return

    # Exibe as informações do cadastro
    for cadastro in cadastros:
        if cadastro["email"] == email_consulta:
            print(f"Nome: {cadastro['nome']}, Idade: {cadastro['idade']}, Email: {cadastro['email']}")
            return  # Adiciona um return para sair da função após a consulta

    # Se o email não for encontrado
    print("\nCadastro não encontrado.")

def verificar_dados(batimentos, saturacao, freq_respiratoria, pressao):
    print("\nResultado:")

    if batimentos > 100:
        print("\nBatimentos altos! Risco de taquicardia.")
    elif batimentos < 50:
        print("\nBatimentos baixos! Risco de bradicardia.")

    if saturacao < 90:
        print("\nSaturação baixa! Possível falta de oxigênio.")

    if freq_respiratoria < 12:
        print("\nFrequência respiratória baixa! Risco de bradipneia.")
    elif freq_respiratoria > 20:
        print("\nFrequência respiratória alta! Risco de taquipneia.")

    if pressao > 140:
        print("\nPressão alta!")
    elif pressao < 90:
        print("\nPressão baixa!")

    if 50 <= batimentos <= 100 and saturacao >= 90 and 12 <= freq_respiratoria <= 20 and 90 <= pressao <= 140:
        print("\nTudo está bem!")

def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Informações sobre a equipe e solução")
        print("2. Cadastro")
        print("3. Verificar Dados")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_equipe_e_solucao()
        elif opcao == "2":
            nome = input("\nDigite seu nome: ")
            idade = input("\nDigite sua idade: ")
            email = input("\nDigite seu email: ")
            senha = input("\nDigite sua senha: ")
            cadastrar(cadastros, nome, idade, email, senha)
            cadastrar_atualizar_excluir_ver(cadastros, nome, idade, email, senha)
        elif opcao == "3":
            batimentos = int(input("\nDigite os batimentos por minuto: "))
            saturacao = int(input("\nDigite a saturação: "))
            freq_respiratoria = int(input("\nDigite a frequência respiratória: "))
            pressao = int(input("\nDigite a pressão: "))
            verificar_dados(batimentos, saturacao, freq_respiratoria, pressao)
        elif opcao == "0":
            print("\nObrigado por usar o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
