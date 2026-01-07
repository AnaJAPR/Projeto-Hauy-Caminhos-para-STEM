import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Print (Output)
print("Hello World")
print("Este é meu primeiro programa")
print("############"*7)


# Variáveis (guardam valores na memória)
nome = "Ana"
idade = 20
altura = 1.73
estudante = True

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("É estudante?", estudante)
print("############"*7)


# Tipo de uma variável (em python, usamos type())
print(type(nome))       # string (texto)
print(type(idade))      # int (inteiro)
print(type(altura))     # float (decimal)
print(type(estudante))  # bool (booleano - true or false)
print("############"*7)


# Operações básicas
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)   # divisão - retorna a parte inteira e decimal, se houver
print(a // b)  # divisão inteira - retorna só a parte inteira
print(a % b)
print("############"*7)


# Operações de comparação
carrinho = 56
boneca = 120
bolsa = "56"

print(carrinho == bolsa)
print(carrinho != boneca)
print(carrinho > boneca)
print(carrinho < boneca)
print(carrinho >= int(bolsa)) # se não usar int() para converter o valor da bolsa para inteiro, não conseguimos comparar. Seria um texto comparando com um número.
print("############"*7)


# Usando variáveis em operações
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3
print("Média das notas:", media)
print("############"*7)


# Input (permite que o usuário digite informações)
nome_usuario = input("Digite seu nome: ")
print("Olá,", nome_usuario)
print("############"*7)


# Input + Conversão de tipo (input sempre retorna string, para fazer contas precisamos converter)
idade_usuario = input("DIgite sua idade: ")
idade_usuario = int(idade_usuario)

print("Daqui a 5 anos você terá ", idade_usuario + 5, "anos.")
print("############"*7)


# Pequeno programa usando tudo que aprendemos até aqui
nome = input("Qual é o seu nome? ")
horas_estudo = float(input("Quantas horas você estuda por semana? "))

print("Resumo:")
print("Nome:", nome)
print("Horas de estudo por semana:", horas_estudo)

horas_por_mes = horas_estudo * 4
print("Horas de estudo por mês:", horas_por_mes)
print("############"*7)


## INTRODUÇÃO A BIBLIOTECAS

# usando math
print("Raiz quadrada de 16:", math.sqrt(16))
print("Valor de pi:", math.pi)
print("############"*7)


# usando numpy
numeros = np.array([2, 4, 6, 8, 10])

print("Array de números:", numeros)
print("Média:", np.mean(numeros))
print("Maior valor:", np.max(numeros))
print("############"*7)


# usando pandas
dados = {
    "nome": ["Ana", "Beatriz", "Carla"],
    "idade": [16, 17, 16],
    "nota": [7.5, 8.0, 6.8]
}

df = pd.DataFrame(dados)

print("Tabela de dados:")
print(df)

print("Média das notas:")
print(df["nota"].mean())
print("############"*7)


# usando matplotlib
nomes = df["nome"]
notas = df["nota"]

plt.bar(nomes, notas)
plt.title("Notas das estudantes")
plt.xlabel("Nome")
plt.ylabel("Nota")
plt.show()


# usando seaborn
sns.barplot(x="nome", y="nota", data=df)
plt.title("Notas das estudantes (Seaborn)")
plt.show()