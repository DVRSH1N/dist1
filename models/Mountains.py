from models.model import Model

class Mountains(Model):
    __nameTable = 'Mountains'
    __height = 'height'
    __name = 'name'
    __region_id = 'region_id'



    def get(self):
        return super().get(self.__nameTable)

    def getOneField(self, field):
        return super().getOneField(self.__nameTable, field)

    def add(self):
        name = input("Введите название горы: ")
        height = input("Введите высоту горы: ")
        region_id = input("введите id региона: ")
        str = f"{self.__name}, {self.__height},{self.__region_id}"
        super().add(self.__nameTable, str, name, height, region_id)

    def delete(self, id):
        super().delete(self.__nameTable, id)

    def update(self):
        id = input("Введите id записи которую надо обновить ")
        field = input("Введите переменную записи которую надо обновить ")
        values = input("Введите значение записи которую надо обновить ")
        super().update(self.__nameTable, id, field, values)