import os

LOGIN = "login.txt"

def verificaLogin():
    if os.path.exists(LOGIN):
        with open(LOGIN, "r") as f:
            usuario = f.read().strip()
            print(f"Login encontrado, usuário: {usuario}")
            return usuario;

print("nenhum login encontrado, por favor faça o login");
usuario = input("digite seu usuário: ").strip()
senha = input("digite sua senha: ").strip()

# escreve no arq que vai ser de verificacao
with open(LOGIN, "w") as f:
    f.write(usuario)

print(f"login feito com sucesso: {usuario}")
