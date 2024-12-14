import json

# Arquivo JSON para armazenar o estoque
ESTOQUE_ARQUIVO = 'estoque.json'

# Função para carregar o estoque do arquivo JSON
def carregar_estoque():
    try:
        with open(ESTOQUE_ARQUIVO, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}  # Retorna um estoque vazio se o arquivo não existir

# Função para salvar o estoque no arquivo JSON
def salvar_estoque(estoque):
    with open(ESTOQUE_ARQUIVO, 'w') as arquivo:
        json.dump(estoque, arquivo, indent=4)

# Função para adicionar um produto ao estoque
def adicionar_produto(nome, quantidade):
    estoque = carregar_estoque()
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade
    salvar_estoque(estoque)
    print(f"Produto '{nome}' adicionado com sucesso. Estoque atualizado: {estoque[nome]}")

# Função para registrar uma venda e atualizar o estoque
def registrar_venda(nome, quantidade):
    estoque = carregar_estoque()
    if nome in estoque and estoque[nome] >= quantidade:
        estoque[nome] -= quantidade
        salvar_estoque(estoque)
        print(f"Venda registrada. Estoque atualizado do produto '{nome}': {estoque[nome]}")
    else:
        print(f"Erro: Estoque insuficiente para o produto '{nome}' ou produto não encontrado.")

# Função para visualizar o estoque atual
def visualizar_estoque():
    estoque = carregar_estoque()
    if estoque:
        print("Estoque atual:")
        for produto, quantidade in estoque.items():
            print(f"- {produto}: {quantidade}")
    else:
        print("Estoque vazio.")

# Exemplo de uso
if __name__ == "__main__":
    while True:
        print("\nControle de Estoque")
        print("1. Adicionar produto")
        print("2. Registrar venda")
        print("3. Visualizar estoque")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            adicionar_produto(nome, quantidade)
        elif escolha == '2':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            registrar_venda(nome, quantidade)
        elif escolha == '3':
            visualizar_estoque()
        elif escolha == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
