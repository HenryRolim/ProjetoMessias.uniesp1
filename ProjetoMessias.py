# Código de um sistema de cadastro simples
import time

with open("login.txt", "r") as file:
  


print("Olá, vamos iniciar seu cadastro!")
time.sleep(1)
print("Por favor, digite o login que deseja salvar.")
time.sleep(1)
with open("login.txt", "w") as file:
  login = input(f"Login: ")
  file.write(login)

time.sleep(2)
print("Muito bem!")
time.sleep(1)
print("Agora insira uma senha.")
time.sleep(1)
with open("senha.txt", "w") as file:
  senha = input(f"Senha: ") 
  file.write(senha)

time.sleep(2)
print("Cadastro feito com sucesso!")
time.sleep(2)
print("Agora, tentemos acessar sua conta.")
time.sleep
with open("login.txt", "r") as file:
  print("Digite seu login: ")
