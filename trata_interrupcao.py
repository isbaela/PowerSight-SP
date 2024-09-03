import pandas as pd
from unidecode import unidecode

# Carregar dados
df = pd.read_csv('C:/Users/isabe/Downloads/interrupcoes-energia-eletrica-2023 (1).csv', encoding='ISO-8859-1', delimiter=';')

# Exibir as primeiras linhas para verificação
print(df.head())

# Função para remover acentos
def remove_accent(text):
    return unidecode(text)

# Aplicar a função para remover acentos em todas as colunas do DataFrame
df = df.applymap(lambda x: remove_accent(str(x)) if isinstance(x, str) else x)

# Filtrar as linhas onde 'SigAgente' contém 'ELETROPAULO' 
df_filtered = df[df['SigAgente'].str.contains('ELETROPAULO', case=False, na=False)]

# Excluir a coluna 'NumCPFCNPJ'
df_filtered = df_filtered.drop(columns=['NumCPFCNPJ'], errors='ignore')

# Salvar o arquivo CSV limpo e filtrado
df_filtered.to_csv('C:/Users/isabe/Downloads/interrupcoes-energia-eletrica-2023-tratado.csv', index=False, header=False, encoding='utf-8', sep=';')
