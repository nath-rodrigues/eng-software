"""
PLANO

O que vou fazer: uma calculadora de frete, tipo de loja online. Eu passo o
tipo de entrega e o peso do pacote (em kg) e ela devolve quanto custa.

O que vou testar (3 jeitos de entrega):
  1. PAC: R$ 15 fixo + R$ 2 por kg
  2. SEDEX: R$ 25 fixo + R$ 4 por kg
  3. Retirada na loja: sempre de graça
  Também vou testar os erros: tipo de entrega que não existe e peso zero
  ou negativo.

Padrão que escolhi: Strategy.
Por quê: cada entrega calcula de um jeito, então no começo vai ficar um
monte de if/elif na mesma função. Se amanhã aparecer uma entrega nova,
eu teria que mexer nessa função de novo. Com o Strategy, cada jeito vira
uma classe separada e dá para criar uma nova sem encostar nas outras.

Como vou dividir o tempo (120 min):
  - Plano: 10 min
  - Red (testes falhando): 15 min
  - Green (fazer passar do jeito mais simples): 10 min
  - Refactor (aplicar o Strategy): 65 min
  - Autoavaliação: 10 min
  - Sobra para enviar: 10 min

Uso de IA: usei o Claude para uma coisa só, conferir se cada fase do
ciclo (red, green e refactor) estava certa, rodando a suíte em cada
commit. O resto eu fiz por conta própria. O link da conversa vai no Moodle.
"""

import pytest

from frete import calcular_frete


# ---------- variação 1: PAC ----------
def test_pac_calcula_valor_fixo_mais_valor_por_kg():
    # 15 + 2 * 3 = 21
    assert calcular_frete("pac", 3) == 21.0


# ---------- variação 2: SEDEX ----------
def test_sedex_calcula_valor_fixo_mais_valor_por_kg():
    # 25 + 4 * 3 = 37
    assert calcular_frete("sedex", 3) == 37.0


# ---------- variação 3: retirada na loja ----------
def test_retirada_na_loja_e_gratis():
    assert calcular_frete("retirada", 3) == 0.0


# ---------- casos de erro ----------
def test_tipo_desconhecido_gera_erro():
    with pytest.raises(ValueError):
        calcular_frete("drone", 3)


def test_peso_zero_gera_erro():
    with pytest.raises(ValueError):
        calcular_frete("pac", 0)


def test_peso_negativo_gera_erro():
    with pytest.raises(ValueError):
        calcular_frete("sedex", -1)