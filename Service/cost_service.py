from Domain.cost import Cost, Cost
from Domain.cost_validator import CostValidator
from Repository.file_repository import FileRepository


class CostService:
    def __init__(self, cost_repository: FileRepository, cost_validator: CostValidator):
        self.__cost_repository = cost_repository
        self.__cost_validator = cost_validator

    def add_cost(self, cost_id, name, total_cost, month):
        '''
        The function adds an cost to your list
        :param cost_id: the id of your cost (string)
        :param name: the name of your cost (string)
        :param total_cost: your total cost (positive integer)
        :month: the month
        :return:
        '''
        cost = Cost(cost_id, name, total_cost, month)
        self.__cost_validator.validate(cost)
        self.__cost_repository.add(cost)

    def delete_cost(self, cost_id):
        '''
        It delets an cost after its id
        :param cost_id: the id of the cost to be deleted
        :return:
        '''
        self.__cost_repository.delete(cost_id)

    def update_cost(self, cost_id, name, total_cost, month):
        '''
        It updates an cost after its id
        :param cost_id: The id of the cost to update
        :param name: The new name or nothing for not change
        :param total_cost: The new total cost or 0 for not change
        :month: The new month ot nothing to not change
        :return:
        '''
        cost = self.__cost_repository.find_by_id(cost_id)
        if cost is None:
            raise KeyError(f"It doesn't exist an expense with the id {cost_id}")
        if name != "":
            cost.name = name
        if str(total_cost) != '':
            cost.total_cost = total_cost
        if month != '':
            cost.month = month

        self.__cost_validator.validate(cost)
        self.__cost_repository.update(cost)


    def get_all(self):
        '''

        :return: cost list
        '''
        return self.__cost_repository.get_all()

    def cost_per_month(self):
        '''

        :return: a dictionary that has as keys the months of the year
        and as value the cost realized in that month
        '''
        result = {}
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                  'September', 'October', 'November', 'December']
        for month in months:
            result[month] = 0
        for element in self.__cost_repository.get_all():
            result[element.month] += element.total_cost

        return result

    def costs_for_the_last_12_months(self):
        '''

        :return: the total cost in the last 12 months
        '''
        total_cost = 0
        for cost in self.__cost_repository.get_all():
            total_cost += cost.total_cost
        return total_cost

    def delete_all(self):
        '''
        It delete all costs
        :return:
        '''
        for cost in self.__cost_repository.get_all():
            self.__cost_repository.delete(cost.entity_id)

    def costs_in_descending_order(self):
        '''

        :return: a list of tuples containing the names of the costs and
        the costs from the last 12 months in descending order
        '''
        costs = {}
        for cost in self.__cost_repository.get_all():
            costs[cost.name] = 0
        for cost in self.__cost_repository.get_all():
            costs[cost.name] += cost.total_cost
        final_result = sorted(costs.items(), key=lambda x: x[1], reverse= True)
        return final_result
