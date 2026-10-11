"""Calculadora de frete - versão REFATORADA.

Padrão de projeto aplicado: STRATEGY

Participantes (nomeados conforme o domínio):
  - Strategy          -> EstrategiaDeFrete  (interface: calcular(peso_kg))
  - ConcreteStrategy  -> FretePac, FreteSedex, RetiradaNaLoja
  - Context           -> CalculadoraDeFrete (recebe uma estratégia e usa ela)

O comportamento visto de fora não mudou: calcular_frete(tipo, peso_kg)
continua existindo com a mesma assinatura, então os testes não mudaram.
"""

from abc import ABC, abstractmethod


# ---------- Strategy ----------
class EstrategiaDeFrete(ABC):
    @abstractmethod
    def calcular(self, peso_kg):
        """Devolve o valor do frete para o peso informado."""


# ---------- ConcreteStrategies ----------
class FretePac(EstrategiaDeFrete):
    def calcular(self, peso_kg):
        return 15.0 + 2.0 * peso_kg


class FreteSedex(EstrategiaDeFrete):
    def calcular(self, peso_kg):
        return 25.0 + 4.0 * peso_kg


class RetiradaNaLoja(EstrategiaDeFrete):
    def calcular(self, peso_kg):
        return 0.0


# ---------- Context ----------
class CalculadoraDeFrete:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def calcular(self, peso_kg):
        if peso_kg <= 0:
            raise ValueError("O peso deve ser maior que zero")
        return self.estrategia.calcular(peso_kg)


# Para criar um tipo novo de entrega basta criar uma classe nova reigstrar aqui, sem mexer nas outras.
ESTRATEGIAS = {
    "pac": FretePac,
    "sedex": FreteSedex,
    "retirada": RetiradaNaLoja,
}


def calcular_frete(tipo, peso_kg):
    """Porta de entrada: escolhe a estratégia pelo tipo e calcula."""
    if tipo not in ESTRATEGIAS:
        raise ValueError(f"Tipo de entrega desconhecido: {tipo}")
    return CalculadoraDeFrete(ESTRATEGIAS[tipo]()).calcular(peso_kg)


# =====================================================================
# AUTOAVALIAÇÃO
#
# Critérios do enunciado:
#  1. Testes em arquivo separado, um por variação: atingi. O
#     test_frete.py cobre PAC, SEDEX e retirada, e ainda botei três
#     testes de erro (tipo que não existe, peso zero e peso negativo).
#  2. Três commits com a fase na mensagem: atingi. Fiz red, green e
#     refactor, nessa ordem.
#  3. Red só com os testes: atingi. Rodei o pytest antes de commitar e
#     vi o erro "No module named 'frete'", porque o frete.py ainda não
#     existia. Só criei ele no commit green.
#  4. Padrão nomeado em comentário: atingi. Usei o Strategy e expliquei
#     no começo deste arquivo quem é quem (EstrategiaDeFrete, FretePac,
#     FreteSedex, RetiradaNaLoja e CalculadoraDeFrete).
#  5. Suíte passando depois do refactor, com a saída registrada: atingi.
#     Os 6 testes passaram e salvei a saída no resultado_testes.txt.
#  Cumpri o prazo sem precisar reduzir para duas variações.
#
# Como foi para mim:
#  No começo rodei o arquivo de testes pelo botão de play do VS Code, e
#  só deu o erro de importação, sem mostrar teste nenhum. Aí entendi que
#  o certo era rodar com "python -m pytest" dentro da pasta, e foi assim
#  que passei a ver cada teste passando ou falhando. Também tomei cuidado
#  de usar "git add" só nos arquivos da atividade, porque o repositório
#  tem trabalhos de outras matérias e eu não queria misturar nos commits.
#
# O que mudou do verde para o refatorado:
#  No verde era uma função só, com um if/elif para cada tipo de entrega.
#  Funcionava, mas toda entrega nova ia obrigar a mexer nela. Agora cada
#  entrega é uma classe separada, a CalculadoraDeFrete usa a que recebe,
#  e um dicionário liga o texto ("pac", "sedex"...) à classe certa. O
#  comportamento é o mesmo e os testes não precisaram mudar.
#
# O que deu mais trabalho:
#  Entender o Strategy na prática, principalmente por que ele deixa o
#  código maior para um problema tão pequeno. Também foi chato decidir
#  onde ficava cada validação (peso e tipo) sem quebrar os testes.
#
# Uso de IA (Claude):
#  Utilizei o Claude exclusivamente como um "revisor de fluxo" para garantir 
#  que eu estava aplicando o ciclo TDD (Red, Green, Refactor) corretamente. 
#  A cada etapa, eu rodava o pytest localmente na minha máquina e pedia para a 
#  IA validar se a saída do terminal correspondia ao esperado para aquela fase 
#  (ex: confirmar se o erro de "module not found" na fase 'Red' era o indicativo 
#  correto para seguir em frente e fazer o commit).
# =====================================================================