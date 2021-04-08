from Domain.entity import Entity


class Cost(Entity):
    def __init__(self, cost_id, name, total_cost, month):
        super().__init__(cost_id)
        self.__name = name
        self.__total_cost = total_cost
        self.__month = month

    @property
    def name(self):
        return self.__name

    @property
    def total_cost(self):
        return self.__total_cost

    @property
    def month(self):
        return self.__month

    def __str__(self):
        return f"\ncost id: {self.entity_id}\nname: {self.__name} " \
               f"\ntotal cost: {self.__total_cost}\nmonth: {self.__month}"

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @total_cost.setter
    def total_cost(self, new_total_cost):
        self.__total_cost = new_total_cost

    @month.setter
    def month(self, new_month):
        self.__month = new_month