import re
import streamlit as st;
import pandas as pd;
import numpy as np;
from os import write


st.title("Declaração de Bens")

def aceitar_apenas_numeros(entrada):
    return ''.join(filter(str.isdigit, entrada))

with st.form(key="include_cliente"):
    input_name = st.text_input(label="insira seu nome: ")
    
    
    ## RESOLVER 
    
    input_rg = st.text_input(label="insira apenas os números do seu rg:")
    input_cpf = st.number_input(label="Insira os números do seu CPF: ", min_value=11, max_value= 11, step=1)
    input_cargo = st.text_input(label="Insira o seu cargo público: ")
    input_residencia = st.text_input(label="Insira a sua residencia: ")
    input_bairro = st.text_input(label="Insira o seu bairro: ")
    
    input_button_submit = st.form_submit_button("enviar")
    
if input_button_submit:
    st.write(f'Nome: {input_name}')
    st.write(f'Rg: {input_rg}')
    st.write(f'cpf: {input_cpf}')
    st.write(f'Cargo: {input_cargo}')
    st.write(f'Residencia: {input_residencia}')
    st.write(f'Bairro: {input_bairro}')
    
# TABELA
# Função para criar uma nova linha na tabela

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