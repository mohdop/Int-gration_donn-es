import pyodbc

server = 'MOHAMEDDIOP'
database = 'code_postales'
trusted_connection = 'yes'

# Création d'une 'connection string'
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};TRUSTED_CONNECTION={trusted_connection}'

# Se connecter à SQL Server
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Créer un déclencheur pour le suivi des codes INSEE intégrés
create_trigger_query = """
CREATE TRIGGER TrackIntegration
ON [019HexaSmal]
AFTER INSERT
AS
BEGIN
    DECLARE @InsertedCodeCommuneInsee NVARCHAR(255)
    SELECT @InsertedCodeCommuneInsee = #Code_commune_INSEE FROM INSERTED

    INSERT INTO IntegrationLog (IntegrationDate, IntegratedCodeCommuneInsee)
    VALUES (GETDATE(), @InsertedCodeCommuneInsee)
END
"""

cursor.execute(create_trigger_query)
conn.commit()

# Fermer les connexions
cursor.close()
conn.close()

print("Trigger created successfully.")
