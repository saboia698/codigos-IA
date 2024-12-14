import json
import os

# Nome do arquivo JSON para armazenar o estoque
ARQUIVO_ESTOQUE = "estoque.json"

def carregar_estoque():
    if os.path.exists(ARQUIVO_ESTOQUE):
        with open(ARQUIVO_ESTOQUE, 'r') as arquivo:
            return json.load(arquivo)
    return {}

def salvar_estoque(estoque):
    with open(ARQUIVO_ESTOQUE, 'w') as arquivo:
        json.dump(estoque, arquivo, indent=4)

def adicionar_item(estoque, nome, quantidade):
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade
    salvar_estoque(estoque)
    print(f"Item '{nome}' adicionado ao estoque. Quantidade atual: {estoque[nome]}")

def registrar_venda(estoque, nome, quantidade):
    if nome in estoque:
        if estoque[nome] >= quantidade:
            estoque[nome] -= quantidade
            salvar_estoque(estoque)
            print(f"Venda registrada. Novo estoque de '{nome}': {estoque[nome]}")
        else:
            print(f"Erro: Estoque insuficiente. Quantidade disponível de '{nome}': {estoque[nome]}")
    else:
        print(f"Erro: Item '{nome}' não encontrado no estoque.")

def exibir_estoque(estoque):
    print("\nEstoque atual:")
    for item, quantidade in estoque.items():
        print(f"{item}: {quantidade}")

def menu():
    estoque = carregar_estoque()
    while True:
        print("\n=== CONTROLE DE ESTOQUE ===")
        print("1. Adicionar item ao estoque")
        print("2. Registrar venda")
        print("3. Exibir estoque")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome do item: ")
            quantidade = int(input("Quantidade: "))
            adicionar_item(estoque, nome, quantidade)
        elif opcao == '2':
            nome = input("Nome do item vendido: ")
            quantidade = int(input("Quantidade vendida: "))
            registrar_venda(estoque, nome, quantidade)
        elif opcao == '3':
            exibir_estoque(estoque)
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()