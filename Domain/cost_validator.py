from Domain.cost import Cost


class CostValidator():
    '''
    It validates a cost and it raises errors is necessary
    '''
    def validate(self, cost: Cost):
        errors = []
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                  'september', 'october', 'november', 'december']
        if cost.total_cost < 0:
            errors.append("The total cost must be entirely positive (even if it's a cost)")
        if cost.name == '':
            errors.append("The cost name must be a string")
        if cost.month.lower() not in months:
            errors.append(f"It doesn't exist a month with the name '{cost.month}'.")
        if len(errors) > 0:
            raise ValueError(errors)