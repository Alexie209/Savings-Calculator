from Tests.test_cost_service import test_add_cost, test_delete_cost, test_update_cost, test_cost_per_month, \
    test_costs_for_the_last_12_months, test_cost_delete_all, test_costs_in_descending_order
from Tests.test_repository import test_update_repository, test_add_repository, test_delete_repository
from Tests.test_income_service import test_add_income, test_delete_income, test_update_income, test_income_per_month, \
    test_income_for_the_last_12_months, test_delete_all_income, test_the_highest_income_for_the_last_12_months
from Tests.test_savings_service import test_savings_per_month, test_savings_for_the_last_12_months


def run_all_tests():
    test_add_repository()
    test_delete_repository()
    test_update_repository()

    test_add_income()
    test_delete_income()
    test_update_income()
    test_income_per_month()
    test_income_for_the_last_12_months()
    test_delete_all_income()
    test_the_highest_income_for_the_last_12_months()

    test_add_cost()
    test_delete_cost()
    test_update_cost()
    test_cost_per_month()
    test_costs_for_the_last_12_months()
    test_cost_delete_all()
    test_costs_in_descending_order()

    test_savings_per_month()
    test_savings_for_the_last_12_months()