class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print("O contato já existe na agenda.")
        elif any(dados[1] == telefone for dados in self.contatos.values()):
            print("O telefone já está registrado para outro contato.")
        else:
            self.contatos[nome] = (nome, telefone)
            print("Contato adicionado com sucesso.")

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print("Contato removido com sucesso.")
        else:
            print("Contato não encontrado na agenda.")

    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            print("Nome:", nome)
            print("Telefone:", self.contatos[nome][1])
        else:
            print("Contato não encontrado na agenda.")

    def listar_contatos(self):
        if not self.contatos:
            print("A agenda está vazia.")
        else:
            print("Lista de contatos:")
            for nome, dados in self.contatos.items():
                print("Nome:", dados[0], "\tTelefone:", dados[1])

def menu():
    agenda = AgendaTelefonica()
    while True:
        print("\n===== MENU =====")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Pesquisar Contato")
        print("4. Listar Contatos")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            agenda.adicionar_contato(nome, telefone)
        elif opcao == '2':
            nome = input("Digite o nome do contato que deseja remover: ")
            agenda.remover_contato(nome)
        elif opcao == '3':
            nome = input("Digite o nome do contato que deseja pesquisar: ")
            agenda.pesquisar_contato(nome)
        elif opcao == '4':
            agenda.listar_contatos()
        elif opcao == '5':
            print("Obrigado por usar a agenda telefônica. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu()