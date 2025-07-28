from services.excecoes import ContaNaoEncontradaError, SaldoInsuficienteError, ValorNegativoError, ContaJaCadastrada
from model.conta import ContaBancaria
from data.dados import salvar
import os
from time import sleep

def cadastrar_conta(contas):
    nome_conta = input("Informe o nome da conta bancária: ").upper().strip()
    senha_conta = input("Digite sua senha: ").strip()
    if any(nome_conta == conta.nome for conta in contas):
        raise ContaJaCadastrada(f"Conta: {nome_conta} já está cadastrada!")
    else:
        contas.append(ContaBancaria(nome_conta, senha_conta, 100.00))
        print(f"Conta cadastrada com sucesso!")

def listar_contas(contas):
    print("\n=== CONTAS ===\n")
    if contas:
        for conta in contas:
            conta.exibir_info()
    else:
        print("Este banco ainda não possui nenhuma conta cadastrada!")

def pesquisar_conta(contas):
    nome_conta = input("Informe o nome da conta que deseja pesquisar: ").upper().strip()
    procurar_conta = [conta for conta in contas if nome_conta == conta.nome]
    if procurar_conta:
        for conta in procurar_conta:
            print(f"\nConta encontrada:\n{conta}")
    else:
        print(f"Conta não encontrada ou não está cadastrada.")

def menu_conta():
    msg = "\n[1] Verificar Saldo da Conta\n[2] Depositar\n[3] Sacar\n[4] Transferir\n[0] Sair da conta\n"
    valid_options = [0, 1, 2, 3, 4]
    while True:
        try:
            valor = int(input(msg))    
            if valor in valid_options:
                return valor
            else:
                print(f"Opção inválida. Escolha entre: {valid_options}")
        except ValueError:
            print(f"Opção inválida. Escolha entre: {valid_options}")

def acessar_conta(contas):
    nome_conta = input("Login(Nome da Conta): ").upper().strip()
    senha_conta = input("Senha: ").strip()
    for conta in contas:
        if nome_conta == conta.nome and senha_conta == conta.senha:
            print(f"Conta acessada com sucesso!\n")
            while True:
                op = menu_conta()
                if op == 0: # Sair
                    limpar_tela(0.5)
                    print("Saindo...")
                    limpar_tela(0.5)
                    break    
                elif op == 1: # Verificar Saldo da Conta
                    print("=== Saldo da Conta ===\n")
                    print(f"Saldo: R$ {conta.saldo:.2f}")
                    sub_menu()
                    limpar_tela(0.5)
                elif op == 2: # Depositar
                    print("=== Depositar Dinheiro ===\n")
                    try:
                        valor_deposito = float(input("Digite o valor do depósito: R$ "))
                        conta.depositar(valor_deposito)
                        salvar(contas)
                        limpar_tela(1)
                        print(f"Depósito efetuado com sucesso!")
                    except ValueError:
                        print("Erro: Valor inválido! Digite somente números.")
                    except ValorNegativoError as e:
                        print(f"Erro: {e}")
                elif op == 3: # Sacar
                    print("=== Sacar Dinheiro ===\n")
                    try:
                        valor_saque = float(input("Digite o valor do saque: R$ "))
                        conta.sacar(valor_saque)
                        salvar(contas)
                        limpar_tela(1)
                        print(f"Saque efetuado com sucesso!")
                    except ValueError:
                        print("Erro: Valor inválido! Digite somente números.")
                    except ValorNegativoError as e:
                        print(f"Erro: {e}")
                    except SaldoInsuficienteError as e:
                        print(f"Erro: {e}")

                elif op == 4: # Transferir
                    print("=== Transferir Dinheiro ===\n")
                    try:
                        conta_destino = input("Digite o nome da conta pra qual deseja transferir: ").strip().upper()
                        valor = float(input("Digite o valor da transferência: R$ "))
                        limpar_tela(1)
                        for conta_recebedora in contas:
                            if conta_recebedora.nome == conta_destino:
                                conta.transferir(valor, conta_recebedora)
                                salvar(contas)
                                print(f"Transferência de R${valor:.2f} para {conta_recebedora.nome} efetuada com sucesso!")
                                break
                        else:
                            raise ContaNaoEncontradaError(f"{conta_destino} não encontrada ou não existe!")
                    except ValueError:
                        print("Erro: Valor inválido! Digite somente números.")
                    except ValorNegativoError as e:
                        print(f"Erro: {e}")
                    except SaldoInsuficienteError as e:
                        print(f"Erro: {e}")
                    except ContaNaoEncontradaError as e:
                        print(f"Erro: {e}")

            return
    else:
        limpar_tela(0.5)
        print("Conta ou senha inválida!") 

def sub_menu():
    msg = "\n[0] Voltar\n"
    valid_options = [0]
    while True:
        try:
            valor = int(input(msg))    
            if valor in valid_options:
                return valor
            else:
                print(f"Opção inválida. Escolha entre: {valid_options}")
        except ValueError:
            print(f"Opção inválida. Escolha entre: {valid_options}")
        

def option_input(msg, valid_options):
    while True:
        try:
            valor = int(input(msg))    
            if valor in valid_options:
                return valor
            else:
                print(f"Opção inválida. Escolha entre: {valid_options}")
        except ValueError:
            print(f"Opção inválida. Escolha entre: {valid_options}")

def limpar_tela(time):
    sleep(time)
    os.system('cls' if os.name == 'nt' else 'clear')
