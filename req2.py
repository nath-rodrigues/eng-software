# req2: vaga de funcionario

def gerar_vagas(total, ids_restritas):
    return {
        str(i): {"restrita": i in ids_restritas}
        for i in range(1, total + 1)
    }

VAGAS = gerar_vagas(total=6, ids_restritas={5, 6})

def tentarReservar(vaga_id):
    vaga = VAGAS.get(vaga_id)
 
    if vaga is None:
        print(f"Vaga {vaga_id} não existe.")
        return False
 
    if not vaga["restrita"]:
        print(f"Vaga {vaga_id} reservada normalmente.")
        return True
 
    confirmar = input(
        f"ALERTA: vaga {vaga_id} é de funcionários. Reservar mesmo assim? (s/n): "
    ).strip().lower()
    ok = confirmar == "s"
    print(f"Vaga {vaga_id} " + ("reservada com exceção." if ok else "reserva cancelada."))
    return ok