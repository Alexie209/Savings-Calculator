from Domain.cost_validator import CostValidator
from Domain.income_validator import IncomeValidator
from Repository.file_repository import FileRepository
from Service.cost_service import CostService
from Service.income_service import IncomeService
from Service.savings_service import SavingsService
from Tests.run_all import run_all_tests
from UI.console import Console

def main():
    run_all_tests()
    estimated_income_repository = FileRepository("estimated_income.txt")
    realized_income_repository = FileRepository("realized_income.txt")
    income_validator = IncomeValidator()
    estimated_income_service = IncomeService(estimated_income_repository, income_validator)
    realized_income_service = IncomeService(realized_income_repository, income_validator)

    estimated_cost_repository = FileRepository("estimated_cost.txt")
    realized_cost_repository = FileRepository("realized_cost.txt")
    cost_validator = CostValidator()
    estimated_cost_service = CostService(estimated_cost_repository, cost_validator)
    realized_cost_service = CostService(realized_cost_repository, cost_validator)

    savings_service = SavingsService(estimated_income_service, realized_income_service,
                                     estimated_cost_service, realized_cost_service)

    console = Console(estimated_income_service, realized_income_service,
                      estimated_cost_service, realized_cost_service, savings_service)
    console.run_main_menu()



main()