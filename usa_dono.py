from restaurante import Prato

opcao = 0
p = Prato()

while opcao!=3:

    if opcao == 1:
        p.descricao = input("Digite a descrição do prato: ")
        p.preco = input("Digite o preço do prato R$: ")
        p.ingredientes = input("Digite os ingredientes: ")
        p.tamanho = input("Digite o tamanho do prato: ")
        p.salvarPratos()

    elif opcao == 2:
        p.visualizarPratosCadastrados()

    opcao = int(input("\nEscolha a opção desejada:"\
              "\n1. Cadastrar Pratos."\
              "\n2. Visualizar Pratos"\
              "\n3. Sair\n"))
