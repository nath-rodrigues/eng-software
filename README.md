# Protótipo — Estacionamento UTFPR

Protótipo em linha de comando que simula duas necessidades do app de
vagas de estacionamento.

**Requisitos cobertos:**
1. Login que não é pedido repetidas vezes (sessão salva em arquivo).
2. Alerta ao tentar reservar vaga destinada a funcionários.

**Como executar:**
```
python main.py
```

Na primeira execução, o login é solicitado; nas seguintes, a sessão
salva é reconhecida automaticamente. Ao tentar reservar a vaga B1
(restrita), o sistema pede confirmação extra antes de concluir.

## Autoavaliação

Não consegui implementar todos os critérios pedidos
O requisito mais difícil foi o da vaga restrita pois precisei decidir o que fazer depois da confirmação
Resolvi separando essa lógica numa função própria que retorna se a reserva foi feita ou não