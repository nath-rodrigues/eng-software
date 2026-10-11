"""Calculadora de frete - versão GREEN (a solução mais direta, com if/elif)."""


def calcular_frete(tipo, peso_kg):
    if peso_kg <= 0:
        raise ValueError("O peso deve ser maior que zero")

    if tipo == "pac":
        return 15.0 + 2.0 * peso_kg
    elif tipo == "sedex":
        return 25.0 + 4.0 * peso_kg
    elif tipo == "retirada":
        return 0.0
    else:
        raise ValueError(f"Tipo de entrega desconhecido: {tipo}")