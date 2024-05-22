import os

#Função para carregar os dados do arquivo de texto
def carregardados():
    dic = {}
    if os.path.exists("dados.txt"):
        with open("dados.txt", "r") as file:
            for line in file:
                login, senha = line.strip().split(':')
                dic[login] = senha
    return dic

#Função para salvar os dados no arquivo de texto
def salvardados(dados):
    with open("dados.txt", "w") as file:
        for login, senha in dados.items():
            file.write(f"{login}:{senha}\n")

#Carregar os dados ao iniciar o programa
dic = carregardados()

while True:
    opcao = input("Bem vindo ao site!\n Digite 1 para Login\n Digite 2 para Cadastro\n Digite 3 para sair\n ")

    match opcao:
        case "1":
            print("Você está no login!")

            login = input("Digite seu login: ")
            senha = input("Digite sua senha: ")

            if login in dic:
                if senha == dic[login]:
                    print("O login é válido. Bem-vindo!")
                else:
                    print("Senha não é válida.")
            else:
                print("O login não existe.")

            break

        case "2":
            print("Você está no cadastro, seja bem-vindo!")

            login = input("Crie seu login: ")
            if login in dic:
                print("Login já existe. Tente outro.")
                continue

            senha = input("Crie sua senha: ")

            dic[login] = senha
            salvardados(dic)  
            
# Salvar os dados no arquivo após o cadastro
            
            print("Cadastro efetuado com sucesso!")
            print(dic)

        case "3":
            print("Você escolheu sair. Até logo!")
            break

        case _:
            print("Digite uma opção válida!")