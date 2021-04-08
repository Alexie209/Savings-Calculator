from Service.cost_service import CostService
from Service.income_service import IncomeService


class SavingsService():
    def __init__(self, estimated_income_service: IncomeService, realized_income_service: IncomeService,
                 estimated_cost_service: CostService, realized_cost_service):
        self.__estimated_income_service = estimated_income_service
        self.__realized_income_service = realized_income_service
        self.__estimated_cost_service = estimated_cost_service
        self.__realized_cost_service = realized_cost_service

    def savings_per_month(self):
        '''

        :return: a dictionary that has as keys the months of the year
        and as value the savings realized in that month
        '''
        savings = {}
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                  'September', 'October', 'November', 'December']
        for month in months:
            savings[month] = 0
        income = self.__realized_income_service.income_per_month()
        cost = self.__realized_cost_service.cost_per_month()
        for month in savings:
            savings[month] = income[month] - cost[month]

        return savings


    def savings_for_the_last_12_months(self):
        '''

        :return: the total savings for the last 12 months
        '''
        total_income = self.__realized_income_service.income_for_the_last_12_months()
        total_costs = self.__realized_cost_service.costs_for_the_last_12_months()
        total_savings = total_income - total_costs

        return total_savings



