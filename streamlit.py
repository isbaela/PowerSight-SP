import streamlit as st
import pandas as pd
import sqlalchemy
import plotly.express as px

# Configurar a conexão com o PostgreSQL
engine = sqlalchemy.create_engine('postgresql://postgres:****@localhost:5432/db_fiap')

# Escreva a consulta SQL para buscar os dados que deseja
query = """
SELECT * FROM tb_interrupcao;
"""

# Carregar os dados em um DataFrame do Pandas
df = pd.read_sql_query(query, engine)

# Adicionar uma coluna com o ano
df['ano'] = pd.to_datetime(df['dt_fim']).dt.year
df['tp_falha'] = df['tp_falha'].str.lower().str.strip()  # Normalizar texto

# Gráfico de Barras: Porcentagem de Falhas por Motivo e Ano

# Contar o número de falhas por motivo e ano
falhas_count = df.groupby(['ano', 'tp_falha']).size().reset_index(name='count')

# Calcular a porcentagem
total_falhas_ano = df.groupby('ano').size().reset_index(name='total_count')
df_merged = pd.merge(falhas_count, total_falhas_ano, on='ano')
df_merged['percentage'] = (df_merged['count'] / df_merged['total_count']) * 100

# Criar o gráfico de barras com Plotly
fig_percentage = px.bar(df_merged, x='ano', y='percentage', color='tp_falha',
                        title='Porcentagem de Falhas por Motivo e Ano',
                        labels={'percentage': 'Porcentagem', 'ano': 'Ano'},
                        text='percentage')



# Gráfico de Linha: Evolução Temporal das Falhas de Meio Ambiente

# Filtrar para motivos relacionados a "meio ambiente"
df_meio_ambiente = df[df['tp_falha'].str.contains('meio ambiente', case=False, na=False)]

# Contar o número de falhas relacionadas ao meio ambiente por ano
falhas_meio_ambiente = df_meio_ambiente.groupby('ano').size().reset_index(name='count')

# Criar o gráfico de linha com Plotly
fig_line = px.line(falhas_meio_ambiente, x='ano', y='count',
                   title='Evolução Temporal das Falhas Relacionadas ao Meio Ambiente',
                   labels={'count': 'Quantidade de Falhas', 'ano': 'Ano'})



# Adicionar um título principal
st.title("Dashboard de Análise de Falhas")

# Adicionar um cabeçalho para a seção de gráficos
st.header("Visualização dos Dados")

# Adicionar uma descrição
st.text("Este dashboard exibe a porcentagem de falhas por motivo e ano, "
        "bem como a evolução temporal das falhas relacionadas ao meio ambiente.")


# Colocar gráficos lado a lado
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig_percentage)

with col2:
    st.plotly_chart(fig_line)

# streamlit run mvp1.py
