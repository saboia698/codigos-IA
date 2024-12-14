import json
import os
from datetime import datetime

class ControleEstoque:
    def __init__(self, arquivo_estoque='estoque.json'):
        self.arquivo_estoque = arquivo_estoque
        self.carregar_estoque()

    def carregar_estoque(self):
        """Carrega o estoque do arquivo JSON ou cria um novo se não existir"""
        if os.path.exists(self.arquivo_estoque):
            with open(self.arquivo_estoque, 'r', encoding='utf-8') as file:
                self.estoque = json.load(file)
        else:
            self.estoque = []

    def salvar_estoque(self):
        """Salva o estoque atualizado no arquivo JSON"""
        with open(self.arquivo_estoque, 'w', encoding='utf-8') as file:
            json.dump(self.estoque, file, indent=4, ensure_ascii=False)

    def adicionar_produto(self, nome, quantidade, preco):
        """Adiciona um novo produto ao estoque"""
        # Verifica se o produto já existe
        for produto in self.estoque:
            if produto['nome'] == nome:
                print(f"Produto {nome} já existe. Use atualizar_quantidade para modificar.")
                return False

        novo_produto = {
            'nome': nome,
            'quantidade': quantidade,
            'preco': preco,
            'data_criacao': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        self.estoque.append(novo_produto)
        self.salvar_estoque()
        print(f"Produto {nome} adicionado com sucesso!")
        return True

    def atualizar_quantidade(self, nome, quantidade):
        """Atualiza a quantidade de um produto no estoque"""
        for produto in self.estoque:
            if produto['nome'] == nome:
                produto['quantidade'] += quantidade
                self.salvar_estoque()
                print(f"Quantidade de {nome} atualizada para {produto['quantidade']}")
                return True
        
        print(f"Produto {nome} não encontrado")
        return False

    def registrar_venda(self, nome, quantidade_vendida):
        """Registra uma venda e atualiza o estoque"""
        for produto in self.estoque:
            if produto['nome'] == nome:
                if produto['quantidade'] >= quantidade_vendida:
                    produto['quantidade'] -= quantidade_vendida
                    self.salvar_estoque()
                    print(f"Venda de {quantidade_vendida} {nome} registrada com sucesso!")
                    return True
                else:
                    print(f"Estoque insuficiente de {nome}")
                    return False
        
        print(f"Produto {nome} não encontrado")
        return False

    def listar_estoque(self):
        """Lista todos os produtos em estoque"""
        print("\n--- Estoque Atual ---")
        for produto in self.estoque:
            print(f"Produto: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print("--------------------")

def main():
    controle = ControleEstoque()

    while True:
        print("\n--- Sistema de Controle de Estoque ---")
        print("1. Adicionar Produto")
        print("2. Atualizar Quantidade")
        print("3. Registrar Venda")
        print("4. Listar Estoque")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade inicial: "))
            preco = float(input("Preço do produto: "))
            controle.adicionar_produto(nome, quantidade, preco)

        elif opcao == '2':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade a adicionar: "))
            controle.atualizar_quantidade(nome, quantidade)

        elif opcao == '3':
            nome = input("Nome do produto vendido: ")
            quantidade = int(input("Quantidade vendida: "))
            controle.registrar_venda(nome, quantidade)

        elif opcao == '4':
            controle.listar_estoque()

        elif opcao == '5':
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
