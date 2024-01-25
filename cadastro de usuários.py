usuarios = {}


def cadastrar_usuario():
    nome = input("Digite seu nome:")
    senha = input("Digite sua senha:")
    usuarios[nome] = senha
    print("Usuario cadastrado")


def realizar_login():
     nome = input("Digite seu nome:")
     senha = input("Digite sua senha:")

     if nome in usuarios and usuarios[nome] == senha:
          print("Login Bem sucessido! Bem vindo" + nome + "!")
     else:
          print("Credenciais Invalidas . tente novamente.")

def main():
     while True:
          print("\n1 - cadastrar usuario")
          print("2 - realizar login")
          print("3 - sair")

          escolha = input("Escolha uma das opções:")

          if escolha == "1":
               cadastrar_usuario()
          elif escolha == "2":
               realizar_login()
          elif escolha == "3":
                print("Saindo do programa")
                break
          else:
               print("Opcao invalida, tente novamente")


if __name__ == "__main__":
     main()
               