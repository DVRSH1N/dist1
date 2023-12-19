from modelDB4.model import Model
from modelDB4.human import human
human = human()

class incident(Model):
    __nameTable = 'incident'
    __date_incidents = 'date_incidents'
    __human_of_incedent_id = 'human_of_incedent_id'
    __role_human_id = 'role_human_id'
    __total = 'total'
    __type_incidents_id = 'type_incidents_id'

    def get(self):
        return super().get(self.__nameTable)

    def selectDateINCEDENT(self):
        dateIN = input("Введите дату начала сортировки")
        dateON = input("Введите дату конца сортировки")
        print(super().selectDateINCEDENT(self.__nameTable, dateIN, dateON))

    def countINCDENT(self):
        print(human.get())
        number = input("Введите id подозреваемого для подсчета преступлений")
        print(super().countINCDENT(self.__nameTable, number))

    def add(self):
        date_incidents = input("Введите дату инцедента ")
        type_incidents_id = input("Введите id типа проишествия ")
        total = input("Введите заключение по делу ")
        print(human.get())
        human_of_incedent_id = input("Введите id человека связанного с инцедентом ")
        role_human_id = input("Введите роль человека в инцеденте ")
        str = f"{self.__date_incidents}, {self.__type_incidents_id}, {self.__total}, {self.__human_of_incedent_id}, {self.__role_human_id}"
        super().add(self.__nameTable, str, date_incidents, type_incidents_id, total, human_of_incedent_id, role_human_id)

    def update(self):
        id = input("Введите id записи которую надо обновить ")
        field = input("Введите переменную записи которую надо обновить ")
        values = input("Введите значение записи которую надо обновить ")
        super().update(self.__nameTable, id, field, values)

    def delete(self, id):
        super().delete(self.__nameTable, id)



