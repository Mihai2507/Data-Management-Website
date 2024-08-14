from citire import citeste_date
from connect import DBConnection


def adauga_inregistrari(date, tabel):
    db = DBConnection()
    existent = False

    if tabel == 'cursanti':
        cnp = date.get('cnp')
        date_existente = citeste_date(tabel)

        for ex in date_existente:
            cnp_existent = ex.get('cnp')
            if cnp_existent == cnp:
                sql = (f"UPDATE {tabel} SET " +
                       ", ".join([f"{key}='{value}'" for key, value in date.items()]) +
                       f" WHERE cnp='{cnp}';")
                existent = True
                break

    if not existent:
        coloane = ", ".join(date.keys())
        valori = "', '".join(date.values())
        sql = (f"INSERT INTO {tabel} ({coloane}) VALUES ('{valori}');")

    with db.connection.cursor() as cursor:
        cursor.execute(sql)
        db.connection.commit()