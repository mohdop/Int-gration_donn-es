import pyodbc

# Paramétrages connection SQL Server  
server = 'MOHAMEDDIOP'
database = 'code_postales'
trusted_connection = 'yes'

# Création d'une 'connection string'
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};TRUSTED_CONNECTION={trusted_connection}'

# Connexion
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

#Création d'une vue des villes du nord pas de calais en utilisant les codes postaux commençant par 59 ou 62
create_view_query = """
CREATE VIEW NordPasDeCalaisCities AS
SELECT * FROM [019HexaSmal]
WHERE Code_postal LIKE '59%' OR Code_postal LIKE '62%'
"""
#Exécuter la commande
cursor.execute(create_view_query)
conn.commit()

#Fermer la connexion
cursor.close()
conn.close()

print("View created successfully.")
