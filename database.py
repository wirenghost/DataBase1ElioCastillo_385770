import oracledb
import os
from dotenv import load_dotenv

# CONEXION A ORACLE

def conectar():
    load_dotenv()

    local_dsn = "db.freesql.com:1521/26ai_un3c1"

    try:
        connection = oracledb.connect(
            user="A385574_SCHEMA_SHQ8Z",
            password="0lKGRMYUY98J3J!S2GN1ZTOTB2XCJZ",
            dsn=local_dsn
        )

        print("Successfully connected to Oracle Database")

        cursor = connection.cursor()

        for result in cursor.execute("SELECT * FROM DUAL"):
            print(result)

        cursor.close()

        return connection

    except oracledb.Error as error:
        print("Error al conectar a Oracle:", error)
        return None
