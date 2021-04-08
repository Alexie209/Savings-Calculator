from Domain.entity import Entity


class Income(Entity):
    def __init__(self, income_id, name, realized_income, month):
        super().__init__(income_id)
        self.__name = name
        self.__realized_income = realized_income
        self.__month = month

    @property
    def name(self):
        return self.__name

    @property
    def realized_income(self):
        return self.__realized_income

    @property
    def month(self):
        return self.__month

    def __str__(self):
        return f"\nincome id: {self.entity_id}\nname: {self.__name} " \
               f"\nrealized income: {self.__realized_income}\nmonth:{self.__month}\n"

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @realized_income.setter
    def realized_income(self, new_realized_income):
        self.__realized_income = new_realized_income

    @month.setter
    def month(self, new_month):
        self.__month = new_month