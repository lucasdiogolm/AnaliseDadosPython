#!/usr/bin/env python
# coding: utf-8

# Imporar a base de dados
import pandas as pd

tabela = pd.read_csv("telecom_users.csv") 

# Vizualizar a base de dados (Entender as informações que tenho disponíveis, descobrir as falhas da base de dados)
tabela  = tabela.drop("Unnamed: 0", axis=1)
display(tabela)

# Tratamento de dados (resolver as falhas da base de dados)
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# Tratar as informações vazias
tabela = tabela.dropna(how="all", axis=1)

# Linhas com alguma (any) informação vazia
tabela = tabela.dropna(how="any", axis=0)

print(tabela.info())


# Análise inicial dos dados
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# Descobrir os motivos do cancelamento
#!pip install plotly
# Importando biblioteca para gráficos 
import plotly.express as px
#Criando um gráfico pra cada coluna (IDClientes, Genero, Aposentado...)
for coluna in tabela.columns:
    # Etapa 1: Cria o gráfico: bar, line, histogram...
    grafico = px.histogram(tabela,x=coluna, color="Churn")

    # Etapa 2: exibe o gráfico
    grafico.show()
