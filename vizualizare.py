from connect import DBConnection


def obtine_date(tabel):
    db = DBConnection().get_connection()
    try:
        with db.cursor() as cursor:
            sql = f"SELECT * FROM {tabel}"
            cursor.execute(sql)
            date = cursor.fetchall()
            return date
    finally:
        db.close()
