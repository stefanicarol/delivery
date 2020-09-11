from restaurante import *

c = Cliente()
p = Pedido()

opcao = 0
while opcao!=5:
    if opcao == 1:
        c.nome = input("Digite seu nome: ")
        c.email = input("Digite seu email: ")
        c.telefone = input("Digite seu Telefone: ")
        c.endereco = input("Digite seu endereço: ")
        c.salvarCliente()
    elif opcao == 2:
        c.visualizarPratos()
    elif opcao == 3:
        p.prato=input("Qual prato deseja pedir? ")
        p.quantidade = input("Qual a quantidade de pratos? ")
        p.cliente = c
        p.fazerPedido(p.prato, p.quantidade, p.cliente)
    elif opcao == 4:
        c.visualizarPedidos()
    opcao = int(input("\nEscolha a opção desejada:"\
              "\n1. Cadastrar Cliente."\
              "\n2. Visualizar Pratos"\
              "\n3. Fazer Pedido"\
              "\n4. Visualizar Pedidos"\
              "\n5. Sair\n"))
