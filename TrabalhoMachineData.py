import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


dataset = pd.read_csv(
    'machine.data' 
)

#print('comprimento da sepala')
#indices de tipo inteiro
#s1 = pd.Series([1, 3, 4, 5, np.nan, 7, 8])
#s1 = pd.DataFrame(np.random.randn(6, 4), columns=list("ABCD"))
dataset.head()
#print(s1)
print(dataset)
print("Tipo de dado de cada coluna")
mostra = dataset.dtypes 
print(mostra)
#s1 = df['Sepal length'].mean()
print('mostra cada atributo das colunas')
coluna = list(dataset.columns)
print (coluna)

input("Aperte <enter> para continuar")

#s1 = s1.style.highlight_max(color = 'lightgreen', axis = 0)
print( '__Media das Colunas__')
print('Media da coluna 3\n ', dataset['MYCT'].mean())
print('Media da coluna 4\n ', dataset['MMIN'].mean())
print('Media da coluna 5\n ', dataset['MMAX'].mean())
print('Media da coluna 6\n ', dataset['CACH'].mean())
print('Media da coluna 7\n ', dataset['CHMIN'].mean())
print('Media da coluna 8\n ', dataset['CHMAX'].mean())
print('Media da coluna 9\n ', dataset['PRP'].mean())
print('Media da coluna 10\n ', dataset['ERP'].mean())


print('___Desvio Padrao___')
print('Desvio da coluna 3\n ', dataset['MYCT'].std())
print('Desvio da coluna 4\n ', dataset['MMIN'].std())
print('Desvio da coluna 5\n ', dataset['MMAX'].std())
print('Desvio da coluna 6\n ', dataset['CACH'].std())
print('Desvio da coluna 7\n ', dataset['CHMIN'].std())
print('Desvio da coluna 8\n ', dataset['CHMAX'].std())
print('Desvio da coluna 9\n ', dataset['PRP'].std())
print('Desvio da coluna 10\n ', dataset['ERP'].std())

input("Aperte <enter> para continuar")

print('_______Moda_______')
print('Moda da coluna 3\n ', dataset['MYCT'].mode())
print('Moda da coluna 4\n ', dataset['MMIN'].mode())
print('Moda da coluna 5\n ', dataset['MMAX'].mode())
print('Moda da coluna 6\n ', dataset['CACH'].mode())
print('Moda da coluna 7\n ', dataset['CHMIN'].mode())
print('Moda da coluna 8\n ', dataset['CHMAX'].mode())
print('Moda da coluna 9\n ', dataset['PRP'].mode())
print('Moda da coluna 10\n ', dataset['ERP'].mode())

print('_______Mediana_______')
print('Mediana da coluna 3\n ', dataset['MYCT'].median())
print('Mediana da coluna 4\n ', dataset['MMIN'].median())
print('Mediana da coluna 5\n ', dataset['MMAX'].median())
print('Mediana da coluna 6\n ', dataset['CACH'].median())
print('Mediana da coluna 7\n ', dataset['CHMIN'].median())
print('Mediana da coluna 8\n ', dataset['CHMAX'].median())
print('Mediana da coluna 9\n ', dataset['PRP'].median())
print('Mediana da coluna 10\n ', dataset['ERP'].median())

input("Aperte <enter> para continuar")

print('_______Valor_Maximo_______')
print('Max da coluna 3\n ', dataset['MYCT'].max())
print('Max da coluna 4\n ', dataset['MMIN'].max())
print('Max da coluna 5\n ', dataset['MMAX'].max())
print('Max da coluna 6\n ', dataset['CACH'].max())
print('Max da coluna 7\n ', dataset['CHMIN'].max())
print('Max da coluna 8\n ', dataset['CHMAX'].max())
print('Max da coluna 9\n ', dataset['PRP'].max())
print('Max da coluna 10\n ', dataset['ERP'].max())

print('_______Valor_Minimo_______')
print('Min da coluna 3\n ', dataset['MYCT'].min())
print('Min da coluna 4\n ', dataset['MMIN'].min())
print('Min da coluna 5\n ', dataset['MMAX'].min())
print('Min da coluna 6\n ', dataset['CACH'].min())
print('Min da coluna 7\n ', dataset['CHMIN'].min())
print('Min da coluna 8\n ', dataset['CHMAX'].min())
print('Min da coluna 9\n ', dataset['PRP'].min())
print('Min da coluna 10\n ', dataset['ERP'].min())

input("Aperte <enter> para continuar")

#print('min da coluna 1:\n ',dataset['Sepallength'].min())
print('______Tabela Odenada de Forma Ascendente_______')
print(dataset.sort_values('MYCT'))
print('______Tabela Ordenada de Forma Descendente_______')
print(dataset.sort_values('MYCT', ascending=False))

print(dataset['MYCT'].describe())

input("Aperte <enter> para continuar")

print('____Coluna com valores abaixo da Media:_____')
print('Coluna 3:') 
print(dataset[['MYCT']] < dataset[['MYCT']].mean())
print('Coluna 4:') 
print(dataset[['MMIN']] < dataset[['MMIN']].mean()) 
print('Coluna 5:') 
print(dataset[['MMAX']] < dataset[['MMAX']].mean())
print('Coluna 6:') 
print(dataset[['CACH']] < dataset[['CACH']].mean())
print('Coluna 7:') 
print(dataset[['CHMIN']] < dataset[['CHMIN']].mean())
print('Coluna 8:') 
print(dataset[['CHMAX']] < dataset[['CHMAX']].mean()) 
print('Coluna 9:') 
print(dataset[['PRP']] < dataset[['PRP']].mean())
print('Coluna 10:') 
print(dataset[['ERP']] < dataset[['ERP']].mean())

print('____Coluna com valores abaixo da Media:_____')
print('Coluna 3:') 
print(dataset[['MYCT']] > dataset[['MYCT']].mean())
print('Coluna 4:') 
print(dataset[['MMIN']] > dataset[['MMIN']].mean()) 
print('Coluna 5:') 
print(dataset[['MMAX']] > dataset[['MMAX']].mean())
print('Coluna 6:') 
print(dataset[['CACH']] > dataset[['CACH']].mean())
print('Coluna 7:') 
print(dataset[['CHMIN']] > dataset[['CHMIN']].mean())
print('Coluna 8:') 
print(dataset[['CHMAX']] > dataset[['CHMAX']].mean()) 
print('Coluna 9:') 
print(dataset[['PRP']] > dataset[['PRP']].mean())
print('Coluna 10:') 
print(dataset[['ERP']] > dataset[['ERP']].mean())

