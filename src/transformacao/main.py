import pandas as pd
import sqlite3
from datetime import datetime

df = pd.read_json('../data/data.json')

# Incluindo novos campos no Data Frame
df['_source'] = "https://lista.mercadolivre.com.br/informatica/portateis-acessorios/_Container_black-friday-f1-ce-games-e-notebooks#applied_filter_id%3Dcategory%26applied_filter_name%3DCategorias%26applied_filter_order%3D4%26applied_value_id%3DMLB430687%26applied_value_name%3DPort%C3%A1teis+e+Acess%C3%B3rios%26applied_value_order%3D7%26applied_value_results%3D212%26is_custom%3Dfalse"
df['_data_coleta'] = datetime.now()

# Transformando os valores dos preços em FLOAT
df['old_price'] = df['old_price'].fillna(0).astype(float)
df['new_price'] = df['new_price'].fillna(0).astype(float)
df['reviews_rating'] = df['reviews_rating'].fillna(0).astype(float)

# Remover os parenteses do campo reviews_total
df['reviews_total'] = df['reviews_total'].str.replace('[\(\)]', '', regex=True)
df['reviews_total'] = df['reviews_total'].fillna(0).astype(int)

# Criando uma conexão com o Sqlite
conn = sqlite3.connect('../data/data.db')

# Salvando os dados no banco de dados
df.to_sql('produtos_ML', conn, if_exists='replace', index=False)

# Fechando conexão com o banco de dados
conn.close()

print(df)