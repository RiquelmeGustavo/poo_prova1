# ==============================================================================
# UFPE - POO - 1ª Avaliação Prática - Sistema de Pedidos de uma Lanchonete
# Integrantes do Grupo:
# José Carlos Joaquim
# Riquelme Gustavo de Arruda Silva
# Wilas Kauã
# ==============================================================================
#
# ------------------------------------------------------------------------------
# DADOS INICIAIS (Exemplo fornecido na avaliação)
# ------------------------------------------------------------------------------
cardapio = {
    "hamburguer": 25.0,
    "sanduiche": 18.0,
    "batata": 12.0,
    "suco": 8.0,
    "agua": 5.0
}

pedido = [
    {"produto": "HAMBURGUER", "quantidade": 2},
    {"produto": "batata", "quantidade": 1},
    {"produto": "Suco", "quantidade": 3},
    {"produto": "pizza", "quantidade": 1},
    {"produto": "agua", "quantidade": 0}
]

nome = "Felipe"
cupom = "SIM"


# ------------------------------------------------------------------------------
# FUNÇÕES OBRIGATÓRIAS
# ------------------------------------------------------------------------------

def validar_item(produto: str, quantidade: int, cardapio: dict) -> bool:
    """
    Verifica se um item do pedido é válido.

    Um item só é válido quando o produto existe no cardápio e a quantidade
    é estritamente maior que zero.

    :param produto: Nome do produto padronizado em minúsculo.
    :param quantidade: Quantidade solicitada do produto.
    :param cardapio: Dicionário contendo os produtos e preços.
    :return: True se válido, False caso contrário.
    """
    produto_existe = produto in cardapio
    quantidade_valida = quantidade > 0
    return produto_existe and quantidade_valida

