class Pessoa:
    nome = ''
    email = ''


class Cliente(Pessoa):
    telefone = ''
    endereco = ''

    def salvarCliente(self):
        arquivo = open('cliente.txt', 'a')
        arquivo.write('Nome: {}, E-mail: {}, Telefone: {}, Endereco: {} '
                      '\n'.format(self.nome, self.email, self.telefone, self.endereco))

    def visualizarClientes(self):
        c = open("cliente.txt", "r")
        for line in c:
            line
            print(line)
        c.close()

    def visualizarPratos(self):
        p = open("pratos.txt", "r")
        for line in p:
            line
            print(line)
        p.close()

    def __repr__(self):
        return 'Nome: {}, E-mail: {}, Telefone: {}, Endereco: {}'\
            .format(self.nome,
                    self.email,
                    self.telefone,
                    self.endereco)

class Prato:
    descricao = ''
    preco = ''
    tamanho = ''
    ingredientes = []

    def salvarPratos(self):
        arquivo = open('pratos.txt', 'a')
        arquivo.write('Descricao: {}, Preco: {}, Tamanho: {}. Ingredientes: {} '
                      '\n'.format(self.descricao, self.preco, self.tamanho, self.ingredientes))

    def visualizarPratosCadastrados(self):
        p = open("pratos.txt", "r")
        for line in p:
            line
            print(line)
        p.close()

    def __repr__(self):
        return 'Descricao: {}, Preco: {}, Tamanho: {}, Ingredientes: {}'\
            .format(self.descricao, self.preco, self.tamanho, self.ingredientes)

class Pedido:
    prato = ''
    quantidade = ''
    cliente = Cliente()

    def fazerPedido(self, prato, cliente):
        p = open("pratos.txt", "r")
        c = 0
        for line in p:
            if prato in line:
                c += 1
                prato = line.rsplit()
                quantidade = input("Qual a quantidade? ")
                arquivo = open('pedido.txt', 'a')
                arquivo.write('Pedido: {}, Quantidade: {}, Cliente: {}''\n'
                              .format(prato, quantidade, cliente))
        p.close()
        if c == 0:
            print("PRATO NÃO CADASTRADO!!")

    def visualizarPedidos(self):
        p = open("pedido.txt", "r")
        for line in p:
            line
            print(line)
        p.close()
    def __repr__(self):
        return 'Prato: {}, Quantidade: {}, Cliente: {}'.format(self.prato, self.quantidade, self.cliente)