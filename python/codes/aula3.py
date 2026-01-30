import pandas as pd

# Importando os dados
df = pd.read_csv("datasets/dados_estudantes.csv")

# Visão inicial
print(df.head())
print("\n")  ## salta uma linha no terminal ou "imprime uma linha vazia"
df.info()
print("\n")

# Padronizando texto
df["turno"] = df["turno"].str.lower().str.strip()  # lower deixa todas as letras minúsculas e strip remove espaços e quebra de linhas "desnecessárias"
df["escola"] = df["escola"].str.lower().str.strip()

# Convertendo colunas numéricas
df["idade"] = pd.to_numeric(df["idade"], errors="coerce")  # o argumento coerce é usada para converter dados inválidos em NaN a fim de evitar levantar erros
df["nota"] = pd.to_numeric(df["nota"], errors="coerce")

# Removendo linhas com valores faltantes essenciais
df_limpo = df.dropna(subset=["idade", "nota"])  # a linha só não é excluída quando há valor válido tanto na coluna "idade" quanto na coluna "nota"

# Agrupando dados (groupby no 1º caso está agrupando a coluna "notas" de acordo com os valores que existem na coluna "turno" e com mean() tira a média)
media_por_turno = df_limpo.groupby("turno")["nota"].mean()
media_por_idade = df_limpo.groupby("idade")["nota"].mean()

melhor_turno = media_por_turno.idxmax()
melhor_idade = media_por_idade.idxmax()

# Resultado final
print(f"Turno com maior média de notas: {melhor_turno}")
print(f"Idade com maior média de notas: {melhor_idade}")
print("\n")
print(media_por_turno)
print("\n")
print(media_por_idade)