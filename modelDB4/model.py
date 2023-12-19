from queries.connection2 import connection


class Model:
    # метод вывода данных из таблицы

    def myGetCursor(self, query):
        with connection().cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
        connection().close()

    def get(self, nameTable):
        query = "SELECT * FROM %s" % nameTable
        return self.myGetCursor(query)

    def delete(self, table, id):
        with connection().cursor() as cursor:
            queries_delete_rows = f"DELETE FROM %s WHERE ID = %s" % (table, id)
            cursor.execute(queries_delete_rows)
            return cursor.fetchall()
        connection().close()
        print("запись удалена")

    def add(self, table, str, *values):
        with connection().cursor() as cursor:
            print(f"INSERT INTO {table} ({str}) VALUES {values}")
            query = f"INSERT INTO {table} ({str}) VALUES {values}"
            cursor.execute(query)
        connection().close()
        print(f"Новая запись в таблицу {table} добавлена")


    # def selectDate(self, table, datetime):
    #     with connection().cursor() as cursor:
    #         query = (
    #         f"SELECT DATE(Doctor_appointments.datetime) AS Day, COUNT(*) AS appointments_count FROM {table} WHERE DATE(Doctor_appointments.datetime) = '{datetime}' GROUP BY Day")
    #             cursor.execute(query)
    #         return cursor.fetchall()
    #  connection().close()

    def selectDateINCEDENT(self, nameTable, dateIN, dateON):
        with connection().cursor() as cursor:
            query = f"SELECT * FROM incident WHERE date_incidents >= '%s' AND date_incidents <= '%s'" % (dateIN, dateON)
            cursor.execute(query)
            connection().commit()
        connection().close()


    def countINCDENT (self, nameTable, number):
        with connection().cursor() as cursor:
            query = f"SELECT COUNT(*) FROM incident WHERE human_of_incedent_id = '%s'" % number
            cursor.execute(query)
            connection().commit()
        connection().close()

    def update(self, table, id, field, values):
        with connection().cursor() as cursor:
            print(f"UPDATE {table} set {field} = '{values}' where id = {id}")
            queries_update = f"UPDATE {table} set {field} = '{values}' where id = {id}"
            cursor.execute(queries_update)
            connection().commit()
        connection().close()
        print("Запись обновлена")

    def delete(self, table, id):
        with connection().cursor() as cursor:
            queries_delete_rows = f"DELETE FROM {table} WHERE ID = {id}"
            cursor.execute(queries_delete_rows)
            connection().commit()
        connection().close()
        print("запись удалена")




