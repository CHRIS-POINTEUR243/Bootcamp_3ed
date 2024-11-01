# -*- coding: utf-8 -*-
"""Projeto_bootcamp.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/BusinessAnalyticsHub/Bootcamp_3ed/blob/main/Projeto_bootcamp.ipynb
"""

from google.colab import files
uploaded = files.upload()

from google.colab import drive
drive.mount('/content/drive')

!pip install openpyxl

import pandas as pd

encantado = pd.read_excel('encantado.xlsx')
santa_tereza = pd.read_excel('santa_tereza.xlsx')
mucum = pd.read_excel('mucum.xlsx')

print("Dados Encantado")
print(encantado.head())

print("\nDados Santa Tereza")
print(santa_tereza.head())

print("\nDados Muçum")
print(mucum.head())

santa_tereza = pd.read_excel('santa_tereza.xlsx', parse_dates=['Data/Hora'])
mucum = pd.read_excel('mucum.xlsx', parse_dates=['Data/Hora'])
encantado = pd.read_excel('encantado.xlsx', parse_dates=['Data/Hora'])

# Valores faltantes
na_counts = santa_tereza.isna().sum()
print('Santa Tereza:\n', na_counts)

na_counts = mucum.isna().sum()
print('Muçum:\n', na_counts)

na_counts = encantado.isna().sum()
print('Encantado:\n', na_counts)

# Análise de Sazonalidade e Tendência - Santa Tereza
plt.figure(figsize=(12, 6))
sns.lineplot(data=santa_tereza, x='Data/Hora', y='Nivel', label='Nível do Rio')
plt.title('Nível na Estação Santa Tereza ao Longo do Tempo')
plt.xlabel('Data/Hora')
plt.ylabel('Nível do Rio')
plt.legend()
plt.grid()
plt.show()

# Análise Exploratória
plt.figure(figsize=(10, 6)) #histograma da variável "Nivel"
sns.histplot(santa_tereza['Nivel'], bins=30, kde=True, color='blue') #Kernel Density Estimate

plt.title('Distribuição do Nível do Rio')
plt.xlabel('Nível do Rio (cm)')
plt.ylabel('Frequência')
plt.grid(axis='y')
plt.tight_layout()

plt.show()

# Descritivas
variaveis_relevantes = ['Chuva', 'Nivel', 'Bateria', 'Temp']
tabela_descritiva = santa_tereza[variaveis_relevantes].describe()
print(tabela_descritiva)

# Boxplot
plt.figure(figsize=(12, 6))
sns.boxplot(data=santa_tereza[['Nivel', 'Chuva']])
plt.title('Boxplot das Variáveis de Santa Tereza')
plt.ylabel('Valores')
plt.xticks(rotation=45)
plt.show()

def count_outliers(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return series[(series < lower_bound) | (series > upper_bound)].count()

# Contar outliers para cada variável de interesse
outlier_counts = {col: count_outliers(santa_tereza[col]) for col in ['Nivel', 'Chuva']}
print("Número de Outliers em cada variável de Santa Tereza:")
for var, count in outlier_counts.items():
    print(f"{var}: {count} outliers")

# Análise de Sazonalidade e Tendência - Muçum
plt.figure(figsize=(12, 6))
sns.lineplot(data=mucum, x='Data/Hora', y='Nivel', label='Nível do Rio')
plt.title('Nível na Estação Muçum ao Longo do Tempo')
plt.xlabel('Data/Hora')
plt.ylabel('Nível do Rio')
plt.legend()
plt.grid()
plt.show()

# Análise Exploratória
plt.figure(figsize=(10, 6)) #histograma da variável "Nivel"
sns.histplot(mucum['Nivel'], bins=30, kde=True, color='blue') #Kernel Density Estimate

plt.title('Distribuição do Nível do Rio')
plt.xlabel('Nível do Rio (cm)')
plt.ylabel('Frequência')
plt.grid(axis='y')
plt.tight_layout()

plt.show()

# Descritivas
variaveis_relevantes = ['Chuva', 'Nivel', 'Vazao', 'Bateria', 'Temp']
tabela_descritiva = mucum[variaveis_relevantes].describe()
print(tabela_descritiva)

# Boxplot
plt.figure(figsize=(12, 6))
sns.boxplot(data=mucum[['Nivel', 'Chuva','Vazao']])
plt.title('Boxplot das Variáveis de Muçum')
plt.ylabel('Valores')
plt.xticks(rotation=45)
plt.show()

# Análise de Sazonalidade e Tendência - Encantado
plt.figure(figsize=(12, 6))
sns.lineplot(data=encantado, x='Data/Hora', y='Nivel', label='Nível do Rio')
plt.title('Nível do Rio Encantado ao Longo do Tempo')
plt.xlabel('Data/Hora')
plt.ylabel('Nível do Rio')
plt.legend()
plt.grid()
plt.show()

# Análise Exploratória
plt.figure(figsize=(10, 6)) #histograma da variável "Nivel"
sns.histplot(encantado['Nivel'], bins=30, kde=True, color='blue') #Kernel Density Estimate

plt.title('Distribuição do Nível do Rio')
plt.xlabel('Nível do Rio (cm)')
plt.ylabel('Frequência')
plt.grid(axis='y')
plt.tight_layout()

plt.show()

# Descritivas
variaveis_relevantes = ['Chuva', 'Nivel', 'Vazao', 'Bateria', 'Temp']
tabela_descritiva = encantado[variaveis_relevantes].describe()
print(tabela_descritiva)

# Boxplot
plt.figure(figsize=(12, 6))
sns.boxplot(data=encantado[['Nivel', 'Chuva', 'Vazao']])
plt.title('Boxplot das Variáveis de Encantado')
plt.ylabel('Valores')
plt.xticks(rotation=45)
plt.show()

# Excluir a variável 'vazão' para Santa Tereza (não tem nada preenchido)
santa_tereza.drop(columns=['Vazao'], inplace=True, errors='ignore')

# Mesclar Dados das Estações
df = pd.merge(pd.merge(santa_tereza, mucum, on='Data/Hora', suffixes=('_santa', '_mucum')), encantado, on='Data/Hora')
df.rename(columns={'chuva': 'chuva_encantado', 'nivel': 'nivel_encantado'}, inplace=True)
df.rename(columns={'Vazao_x': 'Vazao_Mucum'}, inplace=True)
df

#número de NaN
na_counts = df.isna().sum()
print(na_counts)

# Valores Faltantes (1 ALTERNATIVA)
df.fillna(method='ffill', inplace=True)
df.fillna(method='bfill', inplace=True)

# Análise Descritiva
print("Resumo Estatístico das Variáveis:")
print(df.describe())

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Boxplots
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[['Chuva_santa', 'Chuva_mucum', 'Chuva', 'Nivel_santa', 'Nivel_mucum', 'Nivel']])
plt.title("Boxplot das Variáveis")
plt.show()

# Análise de Correlação
correlation_matrix = df[['Chuva_santa', 'Chuva_mucum', 'Chuva', 'Nivel_santa', 'Nivel_mucum', 'Nivel']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Matriz de Correlação")
plt.show()

print(df.columns)

# Converter a coluna 'Data/Hora' para datetime
df['Data/Hora'] = pd.to_datetime(df['Data/Hora'], errors='coerce')

# Feature Engineering: Defasagem e Médias Móveis
def create_lag_features(df, cols, lags):
    for col in cols:
        for lag in range(1, lags + 1):
            df[f"{col}_lag{lag}"] = df[col].shift(lag)
    return df

def create_moving_average_features(df, cols, windows):
    for col in cols:
        for window in windows:
            df[f"{col}_ma{window}"] = df[col].rolling(window).mean()
    return df

df = create_lag_features(df, ['Chuva_santa', 'Chuva_mucum', 'Chuva', 'Nivel_santa', 'Nivel_mucum'], lags=3)
df = create_moving_average_features(df, ['Chuva_santa', 'Chuva_mucum', 'Chuva', 'Nivel_santa', 'Nivel_mucum'], windows=[3, 6, 12])
df

# Feature Engineering: Variáveis de Interação
df['chuva_total'] = df['Chuva_santa'] + df['Chuva_mucum'] + df['Chuva']
df['nivel_prod'] = df['Nivel_santa'] * df['Nivel_mucum']

# Remover valores nulos resultantes das operações de defasagem e médias móveis
df.dropna(inplace=True)
df