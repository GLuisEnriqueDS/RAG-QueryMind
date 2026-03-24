import sqlite3
from app.config import DB_PATH


def ejecutar_sql(query):

    conn = sqlite3.connect(DB_PATH)

    cur = conn.cursor()

    resultado = cur.execute(query).fetchall()

    conn.close()

    return resultado


def construir_sql(sql_template, analisis):

    sql = sql_template

    if "{{agencia}}" in sql:
        sql = sql.replace("{{agencia}}", analisis["agencia"].title())

    if "{{agente}}" in sql:
        sql = sql.replace("{{agente}}", analisis["agente"].title())

    if "{{representante}}" in sql:
        sql = sql.replace("{{representante}}", analisis["representante"].title())

    if "{{cliente}}" in sql:
        sql = sql.replace("{{cliente}}", analisis["cliente"].title())

    return sql


def cargar_entidades():

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    entidades = {}

    entidades["agencias"] = [row[0] for row in cur.execute("SELECT nombre FROM Agencia").fetchall()]
    entidades["agentes"] = [row[0] for row in cur.execute("SELECT nombre FROM Agente").fetchall()]
    entidades["representantes"] = [row[0] for row in cur.execute("SELECT nombre FROM RepresentanteComercial").fetchall()]
    entidades["clientes"] = [row[0] for row in cur.execute("SELECT nombre FROM Cliente").fetchall()]

    conn.close()

    return entidades
