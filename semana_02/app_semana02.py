import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Challenge Data Science Alura - Semana 02')

dados = pd.read_csv('https://raw.githubusercontent.com/duartejr/challenge_data_science_alura_voz/main/dados/dados_clientes_alura_voz.csv')
dados['genero'] = dados.genero.map({0:'Masculino', 1:'Feminino'})
colunas_binarias = ['churn', 'senior', 'parceiro', 'dependentes',
                    'servico_telefone', 'multiplas_linhas', 'seguranca_online',
                    'backup_online', 'protecao_dispositivo', 'suporte_tecnico',
                    'streaming_TV', 'streaming_filmes', 'fatura_online']
dados[colunas_binarias] = dados[colunas_binarias].replace({0:'Não', 1:'Sim'})

variaveis = st.sidebar.multiselect('Variáveis:', list(dados.columns[1:]), default='churn')
grafico = st.sidebar.radio('Tipo de gráfico', ['barras', 'boxplot'])

dados_plot = dados[variaveis]

if grafico == 'barras':
    fig = px.histogram(dados_plot, x=variaveis)
    st.plotly_chart(fig)

if grafico == 'boxplot':
    fig = px.box(dados_plot, x=variaveis[0], y=variaveis[1])
    st.plotly_chart(fig)