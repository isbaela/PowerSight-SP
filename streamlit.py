import streamlit as st
import pandas as pd
import sqlalchemy


# Configurar a conexão com o PostgreSQL
engine = sqlalchemy.create_engine('postgresql://postgres:****@localhost:5432/db_fiap')

print("1")

# Escreva a consulta SQL para buscar os dados que deseja
query = """
SELECT * FROM tb_hst_interrupcao limit 10;
"""

print("2")

# Carregar os dados em um DataFrame do Pandas
df = pd.read_sql_query(query, engine)


# Exibir o DataFrame no Streamlit
st.write("Dados Carregados do Banco de Dados:")
st.write(df)

# Criar um gráfico de exemplo com Plotly
import plotly.express as px

fig = px.line(df, x='ideconjuntounidadeconsumidora', y='datgeracaoconjuntodados', title='Gráfico de Exemplo')
st.plotly_chart(fig)    
