import pandas as pd
from unidecode import unidecode


# Carregar dados
df = pd.read_csv('C:/Users/isabe/Downloads/interrupcoes-energia-eletrica-2022 (1).csv', encoding='ISO-8859-1', delimiter=';')

print(df.head())

# Função para remover acentos
def remove_accent(text):
    return unidecode(text)

# Aplicar a função a todas as colunas do DataFrame
df = df.applymap(lambda x: remove_accent(str(x)) if isinstance(x, str) else x)


# Salvar o arquivo CSV limpo
df.to_csv('C:/Users/isabe/Downloads/interrupcoes-energia-eletrica-2022-tratado.csv', index=False, header=False, encoding='utf-8', sep=';')

