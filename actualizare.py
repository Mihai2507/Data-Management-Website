from connect import DBConnection


def actualizeaza_inregistrare(table, column, old_value, new_value):
    db_connection = DBConnection().get_connection()
    try:
        with db_connection.cursor() as cursor:
            # Construct the SQL query
            sql = f"UPDATE {table} SET {column} = %s WHERE {column} = %s"
            cursor.execute(sql, (new_value, old_value))
        # Commit the transaction
        db_connection.commit()
    except Exception as e:
        print(f"An error occurred while updating the record: {e}")
        db_connection.rollback()
    finally:
        db_connection.close()
