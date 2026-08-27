import oracledb
from database import conectar
# CREATE
def insertar_job(conexion):
    try:
        job_id = input("Ingresa el ID del puesto: ")
        job_title = input("Ingresa el nombre del puesto: ")
        min_salary = int(input("Ingresa el salario minimo: "))
        max_salary = int(input("Ingresa el salario maximo: "))

        cursor = conexion.cursor()

        sql = """
            INSERT INTO HR.JOBS
            (job_id, job_title, min_salary, max_salary)
            VALUES (:1, :2, :3, :4)
        """

        cursor.execute(
            sql,
            [job_id, job_title, min_salary, max_salary]
        )

        conexion.commit()

        print("Puesto insertado correctamente.")

        cursor.close()

    except oracledb.Error as error:
        print("Error al insertar:", error)
        conexion.rollback()

    except ValueError:
        print("Los salarios deben ser numeros.")


# READ

def mostrar_jobs(conexion):
    try:
        cursor = conexion.cursor()

        sql = """
            SELECT job_id, job_title, min_salary, max_salary
            FROM HR.JOBS
            ORDER BY job_id
        """

        cursor.execute(sql)

        resultados = cursor.fetchall()

        print("LISTA DE JOBS")

        if len(resultados) == 0:
            print("No hay puestos registrados.")
        else:
            for job in resultados:
                print("------------------------------------------")
                print("ID:", job[0])
                print("Puesto:", job[1])
                print("Salario minimo:", job[2])
                print("Salario maximo:", job[3])

        cursor.close()

    except oracledb.Error as error:
        print("Error al consultar:", error)



# UPDATE

def actualizar_job(conexion):
    try:
        job_id = input("Ingresa el ID del puesto que quieres actualizar: ")

        job_title = input("Nuevo nombre del puesto: ")
        min_salary = int(input("Nuevo salario minimo: "))
        max_salary = int(input("Nuevo salario maximo: "))

        cursor = conexion.cursor()

        sql = """
            UPDATE HR.JOBS
            SET job_title = :1,
                min_salary = :2,
                max_salary = :3
            WHERE job_id = :4
        """

        cursor.execute(
            sql,
            [job_title, min_salary, max_salary, job_id]
        )

        if cursor.rowcount == 0:
            print("No se encontro un puesto con ese ID.")
        else:
            conexion.commit()
            print("Puesto actualizado correctamente.")

        cursor.close()

    except oracledb.Error as error:
        print("Error al actualizar:", error)
        conexion.rollback()

    except ValueError:
        print("Los salarios deben ser numeros.")



# DELETE


def eliminar_job(conexion):
    try:
        job_id = input("Ingresa el ID del puesto que quieres eliminar: ")

        cursor = conexion.cursor()

        sql = """
            DELETE FROM HR.JOBS
            WHERE job_id = :1
        """

        cursor.execute(sql, [job_id])

        if cursor.rowcount == 0:
            print("No se encontro un puesto con ese ID.")
        else:
            conexion.commit()
            print("Puesto eliminado correctamente.")

        cursor.close()

    except oracledb.Error as error:
        print("Error al eliminar:", error)
        conexion.rollback()



# MENU


def menu():
    conexion = conectar()

    if conexion is None:
        return

    while True:

        print("CRUD")
        print("1. Insertar puesto")
        print("2. Mostrar puestos")
        print("3. Actualizar puesto")
        print("4. Eliminar puesto")
        print("5. Salir")
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            insertar_job(conexion)

        elif opcion == "2":
            mostrar_jobs(conexion)

        elif opcion == "3":
            actualizar_job(conexion)

        elif opcion == "4":
            eliminar_job(conexion)

        elif opcion == "5":
            print("Programa finalizado.")
            conexion.close()
            break

        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    menu()