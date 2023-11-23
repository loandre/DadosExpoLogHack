import psycopg2
from psycopg2 import sql
from datetime import datetime, timedelta

# Conectar ao banco de dados PostgreSQL (substitua os valores conforme necessário)
conn = psycopg2.connect(
    host="localhost",
    database="irrigacao_agua",
    user="postgres",
    password="Paulo12345"
)

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar a tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tabela_data (
        id SERIAL PRIMARY KEY,
        ano INTEGER,
        nome_mes VARCHAR(20),
        semestre INTEGER
    )
""")

# Inserir 10 mil linhas na tabela
for i in range(2018, 2024):
    for j in range(1, 13):
        semestre = 1 if j <= 6 else 2
        mes = datetime.strptime(str(j), "%m").strftime("%B")
        cursor.execute("""
            INSERT INTO tabela_data (ano, nome_mes, semestre)
            VALUES (%s, %s, %s)
        """, (i, mes, semestre))

# Commitar as alterações
conn.commit()

# Fechar a conexão
cursor.close()
conn.close()