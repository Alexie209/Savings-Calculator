from Domain.income import Income
from Domain.income_validator import IncomeValidator
from Repository.file_repository import FileRepository


class IncomeService:
    def __init__(self, income_repository: FileRepository, income_validator: IncomeValidator):
        self.__income_repository = income_repository
        self.__income_validator = income_validator

    def add_income(self, income_id, name, realized_income, month):
        '''
        The function adds an income to your list
        :param income_id: the id of your income (string)
        :param name: the name of your income (string)
        :param realized_income: your realized income (positive integer)
        :param month: the month
        :return:
        '''
        income = Income(income_id, name, realized_income, month)
        self.__income_validator.validate(income)
        self.__income_repository.add(income)

    def delete_income(self, income_id):
        '''
        It delets an income after its id
        :param income_id: the id of the income to be deleted
        :return:
        '''
        self.__income_repository.delete(income_id)

    def update_income(self, income_id, name, realized_income, month):
        '''
        It updates an income after its id
        :param income_id: The id of the income to update
        :param name: The new name or nothing for not change
        :param realized_income: The new realized income or nothing for not change
        :param month: The new month or nothing for not change
        :return:
        '''
        income = self.__income_repository.find_by_id(income_id)
        if income is None:
            raise KeyError(f"It doesn't exist an income with the id {income_id}")
        if name != "":
            income.name = name
        if str(realized_income) != '':
            income.realized_income = realized_income
        if month != '':
            income.month = month

        self.__income_validator.validate(income)
        self.__income_repository.update(income)


    def get_all(self):
        '''

        :return: income list
        '''
        return self.__income_repository.get_all()

    def income_per_month(self):
        '''

        :return:a dictionary that has as keys the months of the year
        and as value the income realized in that month
        '''
        result = {}
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                  'September', 'October', 'November', 'December']
        for month in months:
            result[month] = 0
        for element in self.__income_repository.get_all():
            result[element.month] += element.realized_income

        return result

    def income_for_the_last_12_months(self):
        '''

        :return: the realized income in the last 12 months
        '''
        total_income = 0
        for income in self.__income_repository.get_all():
            total_income += income.realized_income
        return total_income

    def delete_all(self):
        '''
        it delete all the income
        :return:
        '''
        for income in self.__income_repository.get_all():
            self.__income_repository.delete(income.entity_id)

    def the_highest_income_for_the_last_12_months(self):
        '''

        :return:a list of tuples containing the names of the incomes and
        the income from the last 12 months in descending order
        '''
        incomes = {}
        for income in self.__income_repository.get_all():
            incomes[income.name] = 0
        for income in self.__income_repository.get_all():
            incomes[income.name] += income.realized_income
        final_result = sorted(incomes.items(), key=lambda x:x[1], reverse=True)
        return final_result