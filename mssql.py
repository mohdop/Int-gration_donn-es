import pyodbc
import csv
import pandas as pd
import numpy as np
# Informations de connexion à la base de données
server = 'MOHAMEDDIOP'
database = 'code_postales'
trusted_connection = 'yes'

# Création d'une 'connection string'
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};TRUSTED_CONNECTION={trusted_connection}'

# Lecture du fichier CSV 
csv_file = 'communes_data.csv'
df_csv = pd.read_csv(csv_file)

# Connexion à MSSQL
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Parcourir les enregistrements et mettre à jour les lignes
for index, row in df_csv.iterrows():
    code_commune_insee = row['code']
    population = row['population']

    # Vérifier les valeurs Nan
    if pd.notna(population):
        # Charger la population dans la table
        update_query = f"UPDATE [019HexaSmal] SET population = {population} WHERE #Code_commune_INSEE = '{code_commune_insee}'"
        cursor.execute(update_query)
        conn.commit()
    else:
        print(f"Ligne avec la valeur Nan pour le code_commune_insee ignorée: {code_commune_insee}")

# Close connections
cursor.close()
conn.close()

print("Remplissage effectué.")