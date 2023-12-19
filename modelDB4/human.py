from modelDB4.model import Model

class human(Model):
    __nameTable = 'human'
    __addres = 'addres'
    __criminal_record = 'criminal_record'
    __first_name = 'first_name'
    __last_name = 'last_name'
    __numberOFreg = 'numberOFreg'
    __patronymic = 'patronymic'


    def get(self):
        return super().get(self.__nameTable)

    def add(self):
        addres = input("Введите аддрес")
        criminal_record = input("Введите кол-во приводов в полицию")
        first_name = input("Введите имя")
        last_name = input("Введите фамилию")
        numberOFreg = input ("Номер регистрации")
        patronymic = input("Введите отчество")
        str = f"{self.__addres}, {self.__criminal_record}, {self.__first_name}, {self.__last_name}, {self.__numberOFreg}, {self.__patronymic}"
        super().add(self.__nameTable, str, addres, criminal_record, first_name, last_name, numberOFreg, patronymic)

    def update(self):
        id = input("Введите id записи которую надо обновить ")
        field = input("Введите переменную записи которую надо обновить ")
        values = input("Введите значение записи которую надо обновить ")
        super().update(self.__nameTable, id, field, values)

    # def selectDateINCEDENT(self):
    #     dateIN = input("Введите дату начала сортировки")
    #     dateON = input("Введите дату конца сортировки")
    #     print(super().selectDateINCEDENT(self.__nameTable, dateIN, dateON))


