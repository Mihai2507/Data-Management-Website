from connect import DBConnection


def sterge_inregistrare(table, column, value):
    db = DBConnection()
    with db.connection.cursor() as cursor:
        sql = f"DELETE FROM {table} WHERE {column} = %s;"
        cursor.execute(sql, (value,))
        db.connection.commit()
