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

from tabela import tabela

st.title("Declaração de Bens Conjugue" )
from conjugue import tabelaCo