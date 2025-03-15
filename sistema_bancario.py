import textwrap
def menu():

    menu = """ \n
    ==========MENU DE OPÇÕES==========
    Bem vindo, digite uma opção: 
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair

    =>"""'' 
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato):
    if valor>0:
        saldo+=valor
        extrato+=f"Deposito:\tR$ {valor:.2f}\n"
        print("===Deposito realizado com sucesso.")
    else:
        print("Operação falhou! O valor é inválido.")

    return saldo, extrato    


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
        excedeu_saldo = valor > saldo 
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou. Você não tem saldo suficiente para essa transação. ")

        elif excedeu_limite:
            print("Operação falhou. O valor excedeu o limite para essa transação. ")

        elif excedeu_saques:
            print("Operação falhou. Você excedeu o limite de saques permitidos.")

        elif valor > 0: 
            saldo -= valor 
            extrato += f"Saque: R$ {valor:.2f} \n"
            numero_saque += 1
            print(f"Saque realizado com sucesso no valor de {valor}")

        else: 
            print("Operação falhou. O valor informado é inválido.")

        return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("="*10 +"EXTRATO" + "="*10)
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R${saldo :.2f}")
    print("="*40)


def criar_usuario(usuarios):
    cpf=input("Por favor, digite seu CPF(apenas números): ")
    usuario= filtrar_usuario(cpf,usuarios)

    if usuario:
        print("\n Já existe cadastro nesse CPF.")
        return
    
    nome = input("Digite seu nome completo: ")
    data_de_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite seu endereço (logadouro, número, bairro, cidade e sigla do Estado): ")

    usuarios.append({'nome': nome, 'data_de_nascimento': data_de_nascimento, 'cpf':cpf, 'endereco': endereco})

    print("Usuario criado com sucesso. Agradecemos a preferencia")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados= [usuario for usuario in usuarios if usuario ['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta,usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n Usuario não encontrado, criação de conta cancelada!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUE=3
    AGENCIA="0001"

    saldo = 0 
    limite= 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []



    while True: 
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                limite_saques=LIMITE_SAQUE
            )

        elif opcao == "e":
            exibir_extrato(saldo,extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas)+1
            conta=criar_conta(AGENCIA,numero_conta,usuarios)

            if conta:
                contas.append(conta)

        elif opcao =="lc":
            listar_contas(contas)

        elif opcao == "q": 
            print("Foi um prazer tê-lo conosco hoje. Volte sempre.")
            break 

        else: 
            print("Opção inválida, tente novamente.")



main()
