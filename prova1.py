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
    
def calcular_subtotal(quantidade: int, preco_unitario: float) -> float:
  """
  Calcula o subtotal numérico de um item válido.

  :param quantidade: Quantidade de itens.
  :param preco_unitario: Preço unitário do produto.
  :return: Subtotal do item (quantidade * preço unitário).
  """
  return quantidade * preco_unitario

def calcular_desconto(subtotal: float, cupom: str) -> float:
  """
  Calcula o valor monetário do desconto com base no subtotal válido e cupom.

  Faixas de Desconto (base + 5% se cupom == "sim"):
  - Até R$ 50,00: 0% (com cupom: 5%)
  - R$ 50,01 a R$ 100,00: 5% (com cupom: 10%)
  - Acima de R$ 100,00: 10% (com cupom: 15%)

  :param subtotal: Soma dos subtotais dos itens válidos.
  :param cupom: Cupom padronizado em minúsculo ("sim" ou "nao").
  :return: Valor em reais do desconto a ser aplicado.
  """

  if cupom == "sim":
    if subtotal <= 50.0:
      taxa = 0.05
    elif subtotal <= 100.0:
      taxa = 0.10
    else:
      taxa = 0.15
  else:
    if subtotal <= 50.0:
      taxa = 0.00
    elif subtotal <= 100.0:
      taxa = 0.05
    else:
      taxa = 0.10

  return subtotal * taxa

def classificar_pedido(subtotal: float) -> str:
    """
    Retorna a classificação do pedido de acordo com o subtotal válido.

    - Subtotal == 0: "Pedido sem itens válidos"
    - Até R$ 50,00: "Pedido pequeno"
    - R$ 50,01 a R$ 100,00: "Pedido médio"
    - Acima de R$ 100,00: "Pedido grande"

    :param subtotal: Soma dos subtotais válidos (antes do desconto).
    :return: String contendo a classificação.
    """
    if subtotal <= 0:
        return "Pedido sem itens válidos"
    elif subtotal <= 50.0:
        return "Pedido pequeno"
    elif subtotal <= 100.0:
        return "Pedido médio"
    else:
        return "Pedido grande"

def exibir_resumo(cliente: str, itens_validos: list, itens_rejeitados: list,
                  linhas_validas: int, total_unidades: int, subtotal: float,
                  desconto: float, total: float, classificacao: str) -> None:
    """
    Imprime o relatório detalhado do pedido.

    :param cliente: Nome do cliente.
    :param itens_validos: Lista de dicionários dos itens aprovados.
    :param itens_rejeitados: Lista de dicionários dos itens rejeitados e seus motivos.
    :param linhas_validas: Quantidade de linhas válidas processadas.
    :param total_unidades: Soma total de itens/unidades válidas.
    :param subtotal: Subtotal monetário acumulado.
    :param desconto: Valor total do desconto aplicado em reais.
    :param total: Valor final a pagar (subtotal - desconto).
    :param classificacao: Categoria do pedido.
    """
    print("=" * 55)
    print("                RELATÓRIO DO PEDIDO                ")
    print("=" * 55)
    print(f"Cliente: {cliente}\n")

 print("--- ITENS PROCESSADOS ---")
    if itens_validos:
        for item in itens_validos:
            print(f"• {item['produto'].capitalize()}: {item['quantidade']}x R$ {item['preco_unitario']:.2f} "
                  f"= R$ {item['subtotal']:.2f}")
    else:
        print("Nenhum item válido encontrado.")

    if itens_rejeitados:
        print("\n--- ITENS REJEITADOS ---")
        for item in itens_rejeitados:
            motivos_str = " e ".join(item['motivos'])
            print(f"• Produto: '{item['produto_original']}' | Motivo(s): {motivos_str}")

    print("\n--- RESUMO E TOTALIZAÇÃO ---")
    print(f"Linhas Válidas:     {linhas_validas}")
    print(f"Total de Unidades:  {total_unidades}")
    print(f"Subtotal:           R$ {subtotal:.2f}")
    print(f"Desconto:           R$ {desconto:.2f}")
    print(f"Total Final:        R$ {total:.2f}")
    print(f"Classificação:      {classificacao}")
    print("=" * 55)
