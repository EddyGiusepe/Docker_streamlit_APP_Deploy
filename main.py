'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''

# Importando as nossas bibliotecas
import streamlit as st
import pandas as pd
import pickle


# Nosso Dataset
df = pd.read_csv("./data/itens.csv")

media_area = float(df['tamanho'].mean())
area_max = float(df['tamanho'].max())
area_min = float(df['tamanho'].min())


media_ano = float(df['ano'].mean())
ano_max = float(df['ano'].max())
ano_min = float(df['ano'].min())


# Loading de nosso modelo de ML
with open("./models/model_rf.pkl", "rb") as arquivo:
    modelo_rf = pickle.load(arquivo)


# Começando a construção da nossa APP
st.title("APP de Machine Learning")

st.subheader("Escolha as suas opções para realizar uma predição")

area = st.slider("Área do imóvel", min_value=area_min, max_value=area_max, value=media_area)

garagem_options = [1, 2, 3]
garagem = st.radio("Quantidade de Garagens", options=garagem_options)

bairro = st.text_input("Informar o seu Bairro")

ano = st.slider("Ano que foi construído o imóvel", min_value=ano_min, max_value=ano_max, value=media_ano)


st.sidebar.title("Escreva as suas informações")
name_user = st.sidebar.text_input("Digite seu nome")

dados = {
    'tamanho': [area],
    'ano': [ano],
    'garagem': [garagem]
        }

click = st.button('Fazer a previsão')
if click:
    y_pred = float(modelo_rf.predict(pd.DataFrame(dados))[0])
    y_pred = round(y_pred, 2)
    st.write(f"Olá {name_user} do bairro {bairro}, com as informações passadas o valor da casa é de ${y_pred}")
    