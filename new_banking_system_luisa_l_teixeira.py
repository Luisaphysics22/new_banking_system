def menu():
    menu = print("""

       ========= BANCO LUISA DO BRASIL =========
        [0] Depositar
        [1] Sacar
        [2] Extrato
        [3] Cadastrar Cliente
        [4] Nova Conta Corrente
        [5] Listar Conta Corrente
        [6] Sair
        =========================================
     """)
    return input("=> ")

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito realizado de R$ {valor:.2f} com sucesso!\n")
    else:
        print(f"Operação não realizada! O valor informado é inválido. Por favor, tente novamente.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite_valor, numero_saques, LIMITE_SAQUES):
    saldo_insuficiente = saldo < valor
    excedeu_limite = valor > limite_valor
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if saldo_insuficiente:
        print("Operação não realizada, pois não há saldo suficiente.\n")
            
    elif excedeu_limite:
        print(f"Operação não realizada, pois o  valor de R$ {valor:.2f} ultrapassa o limite de R$ {limite_valor:.2f}.\n")

    elif excedeu_saques:
        print("Operação não realizada, pois excedeu o número de saques diários. Por favor, tente novamente amanhã.\n")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso, por favor retire o seu dinheiro!\n")

    else:
        print(f"Operação não realizada! O valor informado é inválido. Por favor, tente novamente.")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("================ EXTRATO ==============\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R${saldo:.2f}\n")
    print("========================================\n")

def cadastrar_cliente(clientes):
    cpf = input("Digite seu CPF(somente os números): ")
    cliente = filtrar_cliente(cpf,clientes)

    if cliente:
        print("Já existe cliente cadastrado com esse CPF. Por favor, tente novamente.")
        return
    
    nome = input("Digite seu nome completo: ")
    data_nasc = input("Digite sua data de nascimento: ")
    endereco = input("Informe seu endereço completo(logradouro, nro - bairro - cidade / sigla do estado):")

    clientes.append({"nome": nome, "data_nascimento": data_nasc, "cpf": cpf, "endereco": endereco})

    print("Cliente cadastrado com sucesso! \n")

def filtrar_cliente(cpf, clientes):
    clientes_cadastrados = [clientes for clientes in clientes if clientes["cpf"] == cpf]
    return clientes_cadastrados[0] if clientes_cadastrados else None

def nova_conta_corrente(agencia, numero_conta, clientes):
    cpf = input("Digite seu CPF(somente os números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Conta corrente criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}
    
    print("Usuário não encontrado, por favor cadastre um usuário primeiro.")

def listar_contas(contas):
    for conta in contas:
       print( f"""
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['cliente']['nome']}
        """)

def main ():
    saldo = 0
    limite_valor = 500
    extrato = ""
    numero_saques = 0
    clientes = []
    contas = []
  
    # const 
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()
        
        if opcao == "0":
                valor = float(input("Informe o valor que deseja depositar: "))
                
                saldo, extrato = depositar(saldo , valor, extrato)
        
        elif opcao == "1":
            valor = float(input("Informe o valor que deseja sacar: "))

            saldo, extrato, numero_saques = sacar(saldo=saldo, valor= valor, extrato=extrato, limite_valor=limite_valor, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)  

        elif opcao == "2":
           exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "3":
            cadastrar_cliente(clientes)
        
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = nova_conta_corrente(AGENCIA, numero_conta, clientes)

            if conta: 
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)
        elif opcao == "6":
            print("Obrigada por ser nosso(a) cliente. Tenha um bom dia!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()

