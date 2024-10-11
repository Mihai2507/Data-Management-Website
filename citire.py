from connect import DBConnection


def citeste_date(tabel):
    db = DBConnection()
    with db.connection.cursor() as cursor:
        sql = f"SELECT * FROM {tabel};"
        cursor.execute(sql)
        rezultate = cursor.fetchall()
    return rezultate
