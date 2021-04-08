from Service.cost_service import CostService
from Service.income_service import IncomeService
from Service.savings_service import SavingsService


class Console:
    def __init__(self, estimated_income_service: IncomeService, realized_income_service: IncomeService,
                 estimated_cost_service: CostService, realized_cost_service: CostService,
                 savings_service: SavingsService):
        self.__estimated_income_service = estimated_income_service
        self.__realized_income_service = realized_income_service
        self.__estimated_cost_service = estimated_cost_service
        self.__realized_cost_service = realized_cost_service
        self.__savings_service = savings_service

    def print_main_menu(self):
        print("-------------MENU-------------")
        print("1. Edit your income")
        print("2. Edit your costs")
        print("3. What do you want to know?")
        print("x. Exit")

    def run_main_menu(self):
        while True:
            self.print_main_menu()
            option = input("Choose an option: ")
            if option  == '1':
                self.run_income_menu()
            elif option == '2':
                self.run_cost_menu()
            elif option == '3':
                self.run_features_menu()
            elif option == 'x':
                break
            else:
                print("Invalid option! Try again! ")

    def print_income_menu(self):
        print("-------------INCOME MENU-------------")
        print("1. Estimated income")
        print("2. Realized income")
        print("b. Back")

    def print_estimated_income_menu(self):
        print("-------------ESTIMATED INCOME MENU-------------")
        print("1. Add")
        print("2. Delete")
        print("3. Update")
        print("4. Delete all")
        print("s. Show all")
        print("b. Back")

    def print_realized_income_menu(self):
        print("-------------REALIZED INCOME MENU-------------")
        print("1. Add")
        print("2. Delete")
        print("3. Update")
        print("4. Delete all")
        print("s. Show all")
        print("b. Back")

    def run_income_menu(self):
        while True:
            self.print_income_menu()
            option = input("Choose an option: ")
            if option == '1':
                self.run_estimated_income_menu()
            elif option == '2':
                self.run_realized_income_menu()
            elif option == 'b':
                break
            else:
                print("Invalid option! Try again! ")

    def run_estimated_income_menu(self):
        while True:
            self.print_estimated_income_menu()
            option = input("Choose an option: ")
            if option == '1':
                self.ui_add_estimated_income()
            elif option == '2':
                self.ui_delete_estimated_income()
            elif option == '3':
                self.ui_update_estimated_income()
            elif option == '4':
                self.ui_delete_all_estimated_income()
            elif option == 's':
                self.ui_show_all_estimated_income()
            elif option == 'b':
                break
            else:
                print("Invalid option! Try again! ")

    def run_realized_income_menu(self):
        while True:
            self.print_realized_income_menu()
            option = input("Choose an option: ")
            if option == '1':
                self.ui_add_realized_income()
            elif option == '2':
                self.ui_delete_realized_income()
            elif option == '3':
                self.ui_update_realized_income()
            elif option == '4':
                self.ui_delete_all_realized_income()
            elif option == 's':
                self.ui_show_all_realized_income()
            elif option == 'b':
                break
            else:
                print("Invalid option! Try again! ")


    def print_cost_menu(self):
        print("-------------COST MENU-------------")
        print("1. Estimated costs")
        print("2. Realized costs")
        print("b. Back")


    def print_estimated_cost_menu(self):
        print("-------------ESTIMATED COST MENU-------------")
        print("1. Add")
        print("2. Delete")
        print("3. Update")
        print("4. Delete all")
        print("s. Show all")
        print("b. Back")


    def print_realized_cost_menu(self):
        print("-------------REALIZED COST MENU-------------")
        print("1. Add")
        print("2. Delete")
        print("3. Update")
        print("4. Delete all")
        print("s. Show all")
        print("b. Back")

    def run_cost_menu(self):
        while True:
            self.print_cost_menu()
            option = input("Choose an option: ")
            if option == '1':
                self.run_estimated_cost_menu()
            elif option  == '2':
                self.run_realized_cost_menu()
            elif option == 'b':
                break
            else:
                print("Invalid option! Try again!")

    def run_estimated_cost_menu(self):
        while True:
            self.print_estimated_cost_menu()
            option = input("Choose an option: ")
            if option == '1':
                self.ui_add_estimated_cost()
            elif option == '2':
                self.ui_delete_estimated_cost()
            elif option == '3':
                self.ui_update_estimated_cost()
            elif option == '4':
                self.ui_delete_all_estimated_costs()
            elif option == 's':
                self.ui_show_all_estimated_costs()
            elif option == 'b':
                break
            else:
                print("Invalid option! Try again!")

    def run_realized_cost_menu(self):
        while True:
            self.print_realized_cost_menu()
            option = input("Choose an option: ")
            if option == '1':
                self.ui_add_realized_cost()
            elif option == '2':
                self.ui_delete_realized_cost()
            elif option == '3':
                self.ui_update_realized_cost()
            elif option == '4':
                self.ui_delete_all_realized_costs()
            elif option == 's':
                self.ui_show_all_realized_costs()
            elif option == 'b':
                break
            else:
                print("Invalid option! Try again!")

    def print_features_menu(self):
        print("-------------FEATURES MENU-------------")
        print("1. Show income per month ")
        print("2. Show income for the last 12 months ")
        print("3. Show the incomes in the last 12 months in descending order")
        print("4. Show costs pers month ")
        print("5. Show costs for the last 12 months ")
        print("6. Show the costs in the last 12 months in descending order")
        print("7. Show savings per month ")
        print("8. Show savings for the last 12 months ")
        print("----------------------")
        print("b. Back")

    def run_features_menu(self):
        while True:
            self.print_features_menu()
            option = input("Choose an option: ")
            if option == '1':
                self.ui_income_per_month()
            elif option == '2':
                self.ui_income_for_the_last_12_months()
            elif option == '3':
                self.ui_the_highest_income_for_the_last_12_months()
            elif option == '4':
                self.ui_costs_per_month()
            elif option == '5':
                self.ui_costs_for_the_last_12_months()
            elif option == '6':
                self.ui_costs_in_descending_order()
            elif option == '7':
                self.ui_savings_per_month()
            elif option == '8':
                self.ui_savings_for_the_last_12_months()
            elif option == 'b':
                break
            else:
                print("Invalid option! Try again!")


    def ui_delete_all_estimated_income(self):
        while True:
            print("Are you sure?")
            print("1. Yes")
            print("2. No")
            option = input("Choose an option: ")
            if option == '1':
                self.__estimated_income_service.delete_all()
                break
            elif option == '2':
                break
            else:
                print("Invalid option! Try again!")


    def ui_the_highest_income_for_the_last_12_months(self):
        realized_result = self.__realized_income_service.the_highest_income_for_the_last_12_months()
        estimated_result = self.__estimated_income_service.the_highest_income_for_the_last_12_months()
        for income in estimated_result:
            print(f"You estimated that you wil earn {income[1]} from your {income[0]}.")
        print("-------------------")
        for income in realized_result:
            print(f"You earned a total of {income[1]} from your {income[0]}.")


    def ui_income_per_month(self):
        realized_income_per_month = self.__realized_income_service.income_per_month()
        estimated_income_per_month = self.__estimated_income_service.income_per_month()
        month = input("Choose a month: ")
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                  'september', 'october', 'november', 'december']
        while month.lower() not in months:
            print(f"It doesn't exist a month with the name '{month}'")
            month = input("Write the month: ")
        print(f"In {month.capitalize()} you had a total estimated income of:"
              f" {estimated_income_per_month[month.capitalize()]}")
        print(f"In {month.capitalize()} you had a total realized income of:"
              f" {realized_income_per_month[month.capitalize()]}")


    def ui_income_for_the_last_12_months(self):
        total_realized_income = self.__realized_income_service.income_for_the_last_12_months()
        total_estimated_income = self.__estimated_income_service.income_for_the_last_12_months()
        print("In the last 12 months you had a total estimated income of ",total_estimated_income)
        print("In the last 12 months you had a total realized income of ",total_realized_income)


    def ui_add_estimated_income(self):
        try:
            income_id = input("Write an id for your income: ")
            name = input("Write a name for your income: ")
            realized_income = int(input("Write your income: "))
            month = input("Write the month: ")
            months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                      'september', 'october', 'november', 'december']
            while month.lower() not in months:
                print(f"It doesn't exist a month with the name '{month}'")
                month = input("Write the month: ")
            self.__estimated_income_service.add_income(income_id, name, realized_income, month.capitalize())
            print("Your estimated income has been successfully added!")
        except Exception as e:
            print(e)


    def ui_show_all_estimated_income(self):
        for income in self.__estimated_income_service.get_all():
            print(income)


    def ui_delete_estimated_income(self):
        try:
            income_id = input("Write the id of the income you want to delete ")
            self.__estimated_income_service.delete_income(income_id)
            print("Your estimated income has been successfully deleted! ")
        except Exception as e:
            print(e)


    def ui_update_estimated_income(self):
        try:
            income_id = input("Write the id of the income you want to update: ")
            name = input("Write the new name of the income or press Enter to not change: ")
            realized_income = input("Write the new realized income or press Enter to not change: ")
            month = input("Write the new month or press Enter to not change ")
            months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                      'september', 'october', 'november', 'december']
            if month != '':
                while month.lower() not in months:
                    print(f"It doesn't exist a month with the name '{month}'")
                    month = input("Write the new month or press Enter to not change: ")
            self.__estimated_income_service.update_income(income_id, name, realized_income,month.capitalize())
            print("Your estimated income has been successfully updated! ")
        except Exception as e:
            print(e)


    def ui_add_realized_income(self):
        try:
            income_id = input("Write an id for your income: ")
            name = input("Write a name for your income: ")
            realized_income = int(input("Write your income: "))
            month = input("Write the month: ")
            months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                      'september', 'october', 'november', 'december']
            while month.lower() not in months:
                print(f"It doesn't exist a month with the name '{month}'")
                month = input("Write the month: ")
            self.__realized_income_service.add_income(income_id, name, realized_income, month.capitalize())
            print("Your realized income has been successfully added! ")
        except Exception as e:
            print(e)


    def ui_show_all_realized_income(self):
        for income in self.__realized_income_service.get_all():
            print(income)


    def ui_delete_realized_income(self):
        try:
            income_id = input("Write the id of the income you want to delete ")
            self.__realized_income_service.delete_income(income_id)
            print("Your realized income has been successfully deleted! ")
        except Exception as e:
            print(e)


    def ui_update_realized_income(self):
        try:
            income_id = input("Write the id of the income you want to update: ")
            name = input("Write the new name of the income or press Enter to not change: ")
            realized_income = input("Write the new realized income or press Enter to not change: ")
            month = input("Write the new month or press Enter to not change: ")
            months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                      'september', 'october', 'november', 'december']
            if month != '':
                while month.lower() not in months:
                    print(f"It doesn't exist a month with the name '{month}'")
                    month = input("Write the new month or press Enter to not change: ")
            self.__realized_income_service.update_income(income_id, name, realized_income,month.capitalize())
            print("Your realized income has been successfully updated! ")
        except Exception as e:
            print(e)


    def ui_delete_all_realized_income(self):
        while True:
            print("Are you sure?")
            print("1. Yes")
            print("2. No")
            option = input("Choose an option: ")
            if option == '1':
                self.__realized_income_service.delete_all()
                break
            elif option == '2':
                break
            else:
                print("Invalid option! Try again!")


    def ui_costs_in_descending_order(self):
        realized_result = self.__realized_cost_service.costs_in_descending_order()
        estimated_result = self.__estimated_cost_service.costs_in_descending_order()
        for cost in estimated_result:
            print(f"You estimated that you will spend {cost[1]} for {cost[0]} ")
        print("-------------------")
        for cost in realized_result:
            print(f"You spent a total of {cost[1]} for {cost[0]}")


    def ui_delete_all_estimated_costs(self):
        while True:
            print("Are you sure?")
            print("1. Yes")
            print("2. No")
            option = input("Choose an option: ")
            if option == '1':
                self.__estimated_cost_service.delete_all()
                break
            elif option == '2':
                break
            else:
                print("Invalid option! Try again!")


    def ui_delete_all_realized_costs(self):
        while True:
            print("Are you sure?")
            print("1. Yes")
            print("2. No")
            option = input("Choose an option: ")
            if option == '1':
                self.__realized_cost_service.delete_all()
                break
            elif option == '2':
                break
            else:
                print("Invalid option! Try again!")


    def ui_costs_per_month(self):
        estimated_costs_per_month = self.__estimated_cost_service.cost_per_month()
        realized_costs_per_month = self.__realized_cost_service.cost_per_month()
        month = input("Choose a month: ")
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                  'september', 'october', 'november', 'december']
        while month.lower() not in months:
            print(f"It doesn't exist a month with the name '{month}'")
            month = input("Write the month: ")
        print(f"In {month.capitalize()} you estimated that you will spend a total of: "
              f"{estimated_costs_per_month[month.capitalize()]}")
        print(f"In {month.capitalize()} you spent a total of: "
              f"{realized_costs_per_month[month.capitalize()]}")


    def ui_costs_for_the_last_12_months(self):
        total_estimated_cost = self.__estimated_cost_service.costs_for_the_last_12_months()
        total_realized_cost = self.__realized_cost_service.costs_for_the_last_12_months()
        print("In the last 12 months you estimated that you will spend a total of ",total_estimated_cost)
        print("In the last 12 months you have spent a total of ",total_realized_cost)


    def ui_add_estimated_cost(self):
        try:
            cost_id = input("Write an id for your cost: ")
            name = input("Write a name for your cost: ")
            total_cost = int(input("Write your total cost: "))
            month = input("Write the month: ")
            months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                      'september', 'october', 'november', 'december']
            while month.lower() not in months:
                print(f"It doesn't exist a month with the name '{month}'")
                month = input("Write the month: ")
            self.__estimated_cost_service.add_cost(cost_id, name, total_cost, month.capitalize())
            print("Your estimated cost has been successfully added! ")
        except Exception as e:
            print(e)


    def ui_add_realized_cost(self):
        try:
            cost_id = input("Write an id for your cost: ")
            name = input("Write a name for your cost: ")
            total_cost = int(input("Write your total cost: "))
            month = input("Write the month: ")
            months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                      'september', 'october', 'november', 'december']
            while month.lower() not in months:
                print(f"It doesn't exist a month with the name '{month}'")
                month = input("Write the month: ")
            self.__realized_cost_service.add_cost(cost_id, name, total_cost, month.capitalize())
            print("Your realized cost has been successfully added! ")
        except Exception as e:
            print(e)


    def ui_show_all_estimated_costs(self):
        for cost in self.__estimated_cost_service.get_all():
            print(cost)


    def ui_show_all_realized_costs(self):
        for cost in self.__realized_cost_service.get_all():
            print(cost)


    def ui_delete_estimated_cost(self):
        try:
            cost_id = input("Write the id of the cost you want to delete ")
            self.__estimated_cost_service.delete_cost(cost_id)
            print("Your estimated cost has been successfully deleted! ")
        except Exception as e:
            print(e)


    def ui_delete_realized_cost(self):
        try:
            cost_id = input("Write the id of the cost you want to delete ")
            self.__realized_cost_service.delete_cost(cost_id)
            print("Your realized cost has been successfully deleted! ")
        except Exception as e:
            print(e)


    def ui_update_estimated_cost(self):
        try:
            cost_id = input("Write the id of the cost you want to update: ")
            name = input("Write the new name of the cost or press Enter to not change: ")
            total_cost = input("Write the new total cost or press Enter to not change: ")
            month = input("Write the new month or press Enter to not change: ")
            months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                      'september', 'october', 'november', 'december']
            if month != '':
                while month.lower() not in months:
                    print(f"It doesn't exist a month with the name '{month}'")
                    month = input("Write the new month or press Enter to not change: ")
            self.__estimated_cost_service.update_cost(cost_id, name, total_cost, month.capitalize())
            print("Your estimated cost has been successfully updated! ")
        except Exception as e:
            print(e)


    def ui_update_realized_cost(self):
        try:
            cost_id = input("Write the id of the cost you want to update: ")
            name = input("Write the new name of the cost or press Enter to not change: ")
            total_cost = input("Write the new total cost or press Enter to not change: ")
            month = input("Write the new month or press Enter to not change: ")
            months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                      'september', 'october', 'november', 'december']
            if month != '':
                while month.lower() not in months:
                    print(f"It doesn't exist a month with the name '{month}'")
                    month = input("Write the new month or press Enter to not change: ")
            self.__realized_cost_service.update_cost(cost_id, name, total_cost, month.capitalize())
            print("Your realized cost has been successfully updated! ")
        except Exception as e:
            print(e)


    def ui_savings_per_month(self):
        savings_per_month = self.__savings_service.savings_per_month()
        month = input("Choose a month: ")
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                  'september', 'october', 'november', 'december']
        while month.lower() not in months:
            print(f"It doesn't exist a month with the name '{month}'")
            month = input("Write the month: ")
        if savings_per_month[month.capitalize()] < 0:
            print(f"You spent too much. Your balance for {month.capitalize()} is "
                  f"{savings_per_month[month.capitalize()]}.")
        elif savings_per_month[month.capitalize()] > 0:
            print(f"Very well! In {month.capitalize()} you saved "
                  f"a total of {savings_per_month[month.capitalize()]}.")
        else:
            print(f"You should try harder! Your balance for {month.capitalize()}"
                  f" is {savings_per_month[month.capitalize()]}.")


    def ui_savings_for_the_last_12_months(self):
        total_savings = self.__savings_service.savings_for_the_last_12_months()
        if total_savings < 0:
            print("Too bad! You spent too much in the last 12 months! Your balance is: ",
                  total_savings)
        elif total_savings == 0:
            print(f"You should try harder! Your balance for the last 12 months is: {total_savings}")
        else:
            print(f"Very well! Your total savings for the last 12 months is: {total_savings}")
