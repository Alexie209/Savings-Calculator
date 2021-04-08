from Domain.cost_validator import CostValidator
from Domain.income_validator import IncomeValidator
from Repository.file_repository import FileRepository
from Service.cost_service import CostService
from Service.income_service import IncomeService
from Service.savings_service import SavingsService
from Tests.utils import clear_file


def test_savings_per_month():
    clear_file("estimated-income-test.txt")
    income_repository = FileRepository("estimated-income-test.txt")
    income_validator = IncomeValidator()
    estimated_income_service = IncomeService(income_repository, income_validator)


    clear_file("estimated-cost-test.txt")
    cost_repository = FileRepository("estimated-cost-test.txt")
    cost_validator = CostValidator()
    estimated_cost_service = CostService(cost_repository, cost_validator)


    clear_file("realized-income-test.txt")
    income_repository_2 = FileRepository("realized-income-test.txt")
    realized_income_service = IncomeService(income_repository_2, income_validator)
    realized_income_service.add_income('1', 'salariu', 3000, 'June')
    realized_income_service.add_income('2', 'bursa', 700, 'March')
    realized_income_service.add_income('3', 'betting', 200, 'May')

    clear_file("realized-cost-test.txt")
    cost_repository_2 = FileRepository("realized-cost-test.txt")
    realized_cost_service = CostService(cost_repository_2, cost_validator)
    realized_cost_service.add_cost('1', 'food', 1000, 'May')
    realized_cost_service.add_cost('2', 'rent', 700, 'June')
    realized_cost_service.add_cost('3', 'dsfdsf', 400, 'June')
    realized_cost_service.add_cost('4', 'sdf', 300, 'July')

    savings_service = SavingsService(estimated_income_service,realized_income_service,
                                     estimated_cost_service, realized_cost_service)
    savings_per_month = savings_service.savings_per_month()
    assert savings_per_month['June'] == 1900
    assert savings_per_month['March'] == 700
    assert savings_per_month['May'] == -800
    assert savings_per_month['July'] == -300
    assert savings_per_month['February'] == 0

def test_savings_for_the_last_12_months():
    clear_file("estimated-income-test.txt")
    income_repository = FileRepository("estimated-income-test.txt")
    income_validator = IncomeValidator()
    estimated_income_service = IncomeService(income_repository, income_validator)

    clear_file("estimated-cost-test.txt")
    cost_repository = FileRepository("estimated-cost-test.txt")
    cost_validator = CostValidator()
    estimated_cost_service = CostService(cost_repository, cost_validator)

    clear_file("realized-income-test.txt")
    income_repository_2 = FileRepository("realized-income-test.txt")
    realized_income_service = IncomeService(income_repository_2, income_validator)
    realized_income_service.add_income('1', 'salariu', 3000, 'June')
    realized_income_service.add_income('2', 'bursa', 700, 'March')
    realized_income_service.add_income('3', 'betting', 200, 'May')

    clear_file("realized-cost-test.txt")
    cost_repository_2 = FileRepository("realized-cost-test.txt")
    realized_cost_service = CostService(cost_repository_2, cost_validator)
    realized_cost_service.add_cost('1', 'food', 1000, 'May')
    realized_cost_service.add_cost('2', 'rent', 700, 'June')
    realized_cost_service.add_cost('3', 'dsfdsf', 400, 'June')
    realized_cost_service.add_cost('4', 'sdf', 300, 'July')

    savings_service = SavingsService(estimated_income_service, realized_income_service,
                                     estimated_cost_service, realized_cost_service)
    total_savings = savings_service.savings_for_the_last_12_months()
    assert total_savings == 1500
