from services.excecoes import *
from services.banco import cadastrar_conta, listar_contas, pesquisar_conta, option_input, acessar_conta, sub_menu, limpar_tela
from data.dados import salvar, carregar


contas = carregar()
msg = "[1] Acessar conta\n[2] Cadastrar conta\n[3] Pesquisar conta\n[4] Listar Contas\n[0] Encerrar Programa\n"
options = [0, 1, 2, 3, 4]
limpar_tela(0.2)

while True:

    op = option_input(msg, options)

    if op == 0:
        limpar_tela(0.5)
        print("Saindo...")
        limpar_tela(0.5)
        break

    if op == 1:
        limpar_tela(0.5)
        acessar_conta(contas)

    if op == 2:
        limpar_tela(0.5)
        try:
            cadastrar_conta(contas)
            salvar(contas)
            sub_menu()
        except ContaJaCadastrada as e:
            print(f"Erro: {e}")
        limpar_tela(1)

    if op == 3:
        limpar_tela(0.5)
        pesquisar_conta(contas)
        sub_menu()
        limpar_tela(1)

    if op == 4:
        limpar_tela(0.5)
        listar_contas(contas)
        sub_menu()
        limpar_tela(1)
