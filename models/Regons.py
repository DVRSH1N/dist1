from models.model import Model

class Regons(Model):
    __nameTable = 'Regons'
    __country = 'country'
    __region = 'region'

    def get(self):
        return super().get(self.__nameTable)

    def getOneField(self, field):
        return super().getOneField(self.__nameTable, field)

    def add(self):
        country = input("Введите страну: ")
        region = input("Введите регион: ")
        str = f"{self.__country}, {self.__region}"
        super().add(self.__nameTable, str, country, region)

    def delete (self, id):
        super().delete(self.__nameTable, id)

    def update(self):
        id = input("Введите id записи которую надо обновить ")
        field = input("Введите переменную записи которую надо обновить ")
        values = input("Введите значение записи которую надо обновить ")
        super().update(self.__nameTable, id, field, values)