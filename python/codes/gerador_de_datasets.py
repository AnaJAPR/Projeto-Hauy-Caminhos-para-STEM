import pandas as pd
import numpy as np

## GERANDO DATASETS PARA PEQUENA TAREFA DA SEMANA 3

np.random.seed(42)

def gerar_dataset_educacao(nome):
    df = pd.DataFrame({
        "id": range(1, 201),
        "idade": np.random.randint(14, 20, 200),
        "horas_estudo": np.random.randint(0, 15, 200),
        "nota": np.random.uniform(0, 10, 200).round(1),
        "faltas": np.random.randint(0, 20, 200),
        "tempo_transporte": np.random.randint(5, 120, 200),
        "grupo": np.random.choice(["A", "B", "C"], 200)
    })

    # Inserindo problemas de dados
    df.loc[5, "nota"] = None
    df.loc[20, "grupo"] = " a "
    df.loc[50, "horas_estudo"] = None

    df.to_csv(f"datasets/{nome}.csv", index=False)

def gerar_dataset_habitos(nome):

    np.random.seed(123)

    df = pd.DataFrame({
        "id": range(1, 201),
        "horas_celular": np.random.randint(1, 12, 200),
        "horas_sono": np.random.randint(4, 10, 200),
        "tempo_redes": np.random.randint(0, 6, 200),
        "tempo_estudo": np.random.randint(0, 8, 200),
        "nivel_concentracao": np.random.randint(1, 6, 200),
        "passos_dia": np.random.randint(1000, 15000, 200)
    })

    # Inserindo problemas de dados
    df.loc[12, "horas_sono"] = None
    df.loc[35, "tempo_redes"] = None
    df.loc[78, "nivel_concentracao"] = None

    df.to_csv(f"datasets/{nome}.csv", index=False)

def gerar_dataset_saude(nome):

    np.random.seed(20)

    df = pd.DataFrame({
        "id": range(1, 201),
        "horas_sono": np.random.randint(4, 10, 200),
        "tempo_tela": np.random.randint(1, 12, 200),
        "min_atividade_fisica": np.random.randint(0, 120, 200),
        "nivel_estresse": np.random.randint(1, 6, 200),
        "copos_agua": np.random.randint(1, 10, 200),
        "alimentacao": np.random.choice(["Boa", "Regular", " Ruim "], 200),
        "sexo": np.random.choice(["F", "M"], 200)
    })

    # Inserindo problemas de dados
    df.loc[15, "horas_sono"] = None
    df.loc[60, "alimentacao"] = "boa "
    df.loc[120, "nivel_estresse"] = None

    df.to_csv(f"datasets/{nome}.csv", index=False)

def gerar_dataset_tecnologia(nome):
    np.random.seed(30)

    df = pd.DataFrame({
        "id": range(1, 201),
        "horas_celular": np.random.randint(1, 14, 200),
        "tempo_redes": np.random.randint(0, 8, 200),
        "tempo_estudo": np.random.randint(0, 10, 200),
        "horas_sono": np.random.randint(4, 9, 200),
        "nivel_concentracao": np.random.randint(1, 6, 200),
        "principal_uso": np.random.choice(
            ["Estudo", "Redes Sociais", "Jogos", " Entretenimento "], 200
        ),
        "periodo": np.random.choice(["Semana", "Final de Semana"], 200)
    })

    # Inserindo problemas de dados
    df.loc[22, "horas_sono"] = None
    df.loc[49, "principal_uso"] = "estudo "
    df.loc[101, "tempo_redes"] = None

    df.to_csv(f"datasets/{nome}.csv", index=False)

def gerar_dataset_educacao_rotina(nome):
    np.random.seed(10)

    df = pd.DataFrame({
        "id": range(1, 201),
        "idade": np.random.randint(14, 19, 200),
        "horas_estudo": np.random.randint(0, 15, 200),
        "nota": np.random.uniform(0, 10, 200).round(1),
        "faltas": np.random.randint(0, 20, 200),
        "turno": np.random.choice(["Manhã", "Tarde", " Noite "], 200),
        "escola": np.random.choice(["Publica", "Pública", "publica "], 200)
    })

    # Inserindo problemas de dados
    df.loc[8, "nota"] = None
    df.loc[34, "horas_estudo"] = None
    df.loc[77, "turno"] = " manhã "

    df.to_csv(f"datasets/{nome}.csv", index=False)

gerar_dataset_educacao("dataset_nicolas")
gerar_dataset_habitos("dataset_kleber")
gerar_dataset_educacao_rotina("dataset_lazaro")
gerar_dataset_saude("dataset_sofia")
gerar_dataset_tecnologia("dataset_lavinia_melo")
gerar_dataset_educacao("dataset_lavinia_damasceno")
gerar_dataset_educacao_rotina("dataset_laura")
gerar_dataset_saude("dataset_samuel")
gerar_dataset_tecnologia("dataset_guilherme")
gerar_dataset_habitos("dataset_extra")
