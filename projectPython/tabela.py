import re
import streamlit as st;
import pandas as pd;
import numpy as np;
from os import write

def tabela():
    def nova_linha():
        nova_linha = pd.DataFrame({'Descrição do Patrimônio': [''], 'Valor': ['']})
        return nova_linha

if 'df' not in st.session_state:
    # cria um DataFrame inicial com uma linha vazia
    st.session_state.df = pd.DataFrame({'Descrição do Patrimônio': [''], 'Valor': ['']})

# Botão para adicionar uma nova linha
if st.button('Adicionar Nova Linha'):
    st.session_state.df = pd.concat([st.session_state.df, nova_linha()], ignore_index=True)

# Loop para permitir que o usuário escreva em cada célula da tabela
for index, row in st.session_state.df.iterrows():
    for col in st.session_state.df.columns:
        if col == 'Descrição do Patrimônio':
            st.session_state.df.at[index, col] = st.text_input(label=f"Insira um valor para a célula ({index}, {col}):", value=row[col])
        elif col == 'Valor':
            valor = st.text_input(label=f"Insira um valor para a célula ({index}, {col}):", value=row[col])
            if re.match("^[\d,]*$", valor):
                st.session_state.df.at[index, col] = valor
            else:
                st.warning("Por favor, insira apenas números na segunda coluna.")

# Exibir a tabela atualizada
st.write(st.session_state.df)