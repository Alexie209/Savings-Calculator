from Domain.income import Income


class IncomeValidator():
    '''
    it validates an income and it raises errors is necessary
    '''
    def validate(self, income: Income):
        errors = []
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                  'september', 'october', 'november', 'december']
        if income.realized_income < 0:
            errors.append("The realized income must be entirely positive (otherwise it is an expense)")
        if income.name == '':
            errors.append("The income name must be a string")
        if income.month.lower() not in months:
            errors.append(f"It doesn't exist a month with the name '{income.month}'.")
        if len(errors) > 0:
            raise ValueError(errors)