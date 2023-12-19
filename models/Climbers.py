from models.model import Model


class Climbers(Model):
# Приватное поля имя таблицы
    __nameTable = 'Climbers'
    __name = 'name'
    __address = 'address'

# Метод вывода записей из таблицы
    def get(self):
        return super().get(self.__nameTable)

# Метод вывода записей одного поля из таблицы

    def getOneField(self, field):
        return super().getOneField(self.__nameTable, field)

# добавить запись
    def add(self):
        name = input("Введите имя: ")
        address = input("Введите адрес: ")
        str = f"{self.__name}, {self.__address}"
        super().add(self.__nameTable, str, name, address)

    def delete (self, id):
        super().delete(self.__nameTable, id)

    def update(self):
        id = input("Введите id записи которую надо обновить ")
        field = input("Введите переменную записи которую надо обновить ")
        values = input("Введите значение записи которую надо обновить ")
        super().update(self.__nameTable, id, field, values)