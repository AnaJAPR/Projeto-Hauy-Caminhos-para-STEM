import pandas as pd

# Importando os dados
df = pd.read_csv("dados_estudantes.csv")

# Padronização
df["turno"] = df["turno"].str.lower().str.strip()

df["nota"] = pd.to_numeric(df["nota"], errors="coerce")

# Criando uma nova coluna baseada em uma condição
def classificar_desempenho(nota):
    if nota >= 7:
        return "bom"
    elif nota >= 5:
        return "regular"
    else:
        return "baixo"

df["desempenho"] = df["nota"].apply(classificar_desempenho)

# Selecionando apenas estudantes com nota válida
df = df.dropna(subset=["nota"])

# Lista para guardar estudantes com nota alta
destaques = {}

for _, linha in df.iterrows():
    if linha["nota"] >= 9:
        destaques[linha["id"]] = linha["nota"]


# Dicionário com média de notas por turno
media_por_turno = {}

for turno in df["turno"].unique():
    media = df[df["turno"] == turno]["nota"].mean()
    media_por_turno[turno] = media

# Exibindo resultados
print("Notas de destaque:", destaques)
print("Média por turno:", media_por_turno)

# Pequeno exemplo de uso do while
orcamento = 20
while orcamento > 0:
    orcamento -= 5  ## Isso é o mesmo que orcamento = orcamento - 5, ou seja, estamos subtraindo 5 da variável orcamento em cada loop.
    print("Gastei 5 reais.")


# Comandos que usamos para subir os códigos da aula para o GitHub por meio do Git Bash
# usa cd para entrar na pasta referente ao seu projeto no GitHub
# git status    -> deve aparecer os nomes dos arquivos adicionados ou alterados em vermelho
# git add .     -> Adiciona todos os arquivos listados em vermelho anteriormente
# git status    -> os nomes dos arquivos agoram aparecem em verde
# git commit -m "mensagem de commit"    -> salva as alterações com a mensagem que adiconar entre aspas
# git push      -> mandas as novas alterações para o repositório remoto, ou seja, deve aparecer no GitHub