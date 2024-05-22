# Comando para conseguir utilizar o comando: "time.sleep"
import time

# Lista onde as respostas serão armazenadas
curso  = []
disciplina = []
carga_horaria = []

# Início do código
print(f"Bem-vindo!")
time.sleep(1)

# Começando com códigos que necessitam de respostas
quant = int(input("Digite a quantidade de cursos que deseja inserir: "))
time.sleep(2)

# Sequência de códigos onde o responderemos no terminal e as informações serão guardadas enquanto o código estiver em funciomento
for i in range(quant):
    curs = input("Digite o curso: ")
    curso.append(curs)
    time.sleep(1)
    disc = input("Digite a descrição da matéria: ")
    disciplina.append(disc)
    time.sleep(1)
    cargah = int(input("Digite a carga horária: "))
    carga_horaria.append(cargah)
    time.sleep(1)

# Onde as respostas serão escritas para ficarem salvas
with open("dadosfinais.txt", "w") as f:
    for i in range(quant):
        f.write("\nCurso: " + curso[i] + "\n")
        f.write("Descricao: " + disciplina[i] + "\n")
        f.write("Carga Horaria: " + str(carga_horaria[i]) + "\n\n")

# Lerá, imprimirá e escreverá o que for inserido como resposta no terminal. Aparecerá no console
with open ("dadosfinais.txt", "r") as f:
    for line in f:
        print(line, end='')