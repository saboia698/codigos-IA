import json

def criar_estoque(nome_arquivo="estoque.json"):
    """Cria um arquivo JSON inicial com um estoque vazio."""
    estoque = {}
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(estoque, arquivo)

def adicionar_produto(nome_arquivo, produto, quantidade):
    """Adiciona um produto ao estoque ou atualiza a quantidade."""
    with open(nome_arquivo, 'r') as arquivo:
        estoque = json.load(arquivo)
    estoque[produto] = quantidade
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(estoque, arquivo)

def realizar_venda(nome_arquivo, produto, quantidade_vendida):
    """Realiza uma venda, atualizando o estoque."""
    with open(nome_arquivo, 'r') as arquivo:
        estoque = json.load(arquivo)
    if produto in estoque:
        estoque[produto] -= quantidade_vendida
        if estoque[produto] < 0:
            print(f"Quantidade insuficiente de {produto} em estoque.")
            return False
        else:
            with open(nome_arquivo, 'w') as arquivo:
                json.dump(estoque, arquivo)
            return True
    else:
        print(f"Produto {produto} não encontrado no estoque.")
        return False

# Exemplo de uso:
criar_estoque()
adicionar_produto("estoque.json", "Maçã", 10)
adicionar_produto("estoque.json", "Banana", 5)
realizar_venda("estoque.json", "Maçã", 3)