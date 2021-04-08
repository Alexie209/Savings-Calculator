from Domain.income_validator import IncomeValidator
from Repository.file_repository import FileRepository
from Service.income_service import IncomeService
from Tests.utils import clear_file


def test_add_income():
    clear_file("income-test.txt")
    income_repository = FileRepository("income-test.txt")
    income_validator = IncomeValidator()

    income_service = IncomeService(income_repository, income_validator)

    income_service.add_income('1', 'salariu', 3000, 'March')
    income_service.add_income('2', 'bursa', 700, 'May')
    assert len(income_service.get_all()) == 2

    added1 =  income_repository.find_by_id('1')
    assert added1.entity_id == '1'
    assert added1.name == 'salariu'
    assert added1.realized_income == 3000
    assert added1.month == 'March'

    added2 = income_repository.find_by_id('2')
    assert added2.entity_id == '2'
    assert added2.name == 'bursa'
    assert added2.realized_income == 700
    assert added2.month == 'May'

    try:
        income_service.add_income('1','other',500,'July')
        assert False
    except Exception:
        assert True


def test_delete_income():
    clear_file("income-test.txt")
    income_repository = FileRepository("income-test.txt")
    income_validator = IncomeValidator()

    income_service = IncomeService(income_repository, income_validator)

    income_service.add_income('1', 'salariu', 3000, 'March')
    income_service.add_income('2', 'bursa', 700, 'May')
    income_service.add_income('3', 'betting', 200,'December')
    assert len(income_service.get_all()) == 3

    income_service.delete_income('1')
    assert len(income_service.get_all()) == 2

    income_service.delete_income('2')
    assert len(income_service.get_all()) == 1

    assert income_repository.find_by_id('1') is None
    assert income_repository.find_by_id('2') is None
    assert income_repository.find_by_id('3') is not None

    try:
        income_service.delete_income('1')
        assert False
    except Exception:
        assert True


def test_update_income():
    clear_file("income-test.txt")
    income_repository = FileRepository("income-test.txt")
    income_validator = IncomeValidator()

    income_service = IncomeService(income_repository, income_validator)

    income_service.add_income('1', 'salariu', 3000, 'March')
    income_service.add_income('2', 'bursa', 700, 'May')
    income_service.add_income('3', 'betting', 200, 'December')

    income_service.update_income('3','investments',5000,'')
    updated = income_repository.find_by_id('3')
    assert updated.entity_id == '3'
    assert updated.name == 'investments'
    assert updated.realized_income == 5000
    assert updated.month == 'December'

    try:
        income_service.update_income('4','',3434,'March')
        assert False
    except Exception:
        assert True

def test_income_per_month():
    clear_file("income-test.txt")
    income_repository = FileRepository("income-test.txt")
    income_validator = IncomeValidator()

    income_service = IncomeService(income_repository, income_validator)

    income_service.add_income('1', 'salariu', 3000, 'March')
    income_service.add_income('2', 'bursa', 700, 'March')
    income_service.add_income('3', 'betting', 200, 'December')

    income_per_month = income_service.income_per_month()
    assert income_per_month['March'] == 3700
    assert income_per_month['December'] == 200
    assert income_per_month['May'] == 0
    assert income_per_month['January'] == 0


def test_income_for_the_last_12_months():
    clear_file("income-test.txt")
    income_repository = FileRepository("income-test.txt")
    income_validator = IncomeValidator()

    income_service = IncomeService(income_repository, income_validator)

    income_service.add_income('1', 'salariu', 3000, 'March')
    income_service.add_income('2', 'bursa', 700, 'March')
    income_service.add_income('3', 'betting', 200, 'December')

    total_income = income_service.income_for_the_last_12_months()
    assert total_income == 3900


def test_delete_all_income():
    clear_file("income-test.txt")
    income_repository = FileRepository("income-test.txt")
    income_validator = IncomeValidator()

    income_service = IncomeService(income_repository, income_validator)

    income_service.add_income('1', 'salariu', 3000, 'March')
    income_service.add_income('2', 'bursa', 700, 'March')
    income_service.add_income('3', 'betting', 200, 'December')

    income_service.delete_all()
    assert len(income_service.get_all()) == 0


def test_the_highest_income_for_the_last_12_months():
    clear_file("income-test.txt")
    income_repository = FileRepository("income-test.txt")
    income_validator = IncomeValidator()

    income_service = IncomeService(income_repository, income_validator)

    income_service.add_income('1', 'salariu', 3000, 'March')
    income_service.add_income('2', 'bursa', 700, 'March')
    income_service.add_income('3', 'betting', 200, 'December')
    income_service.add_income('4', 'salariu', 2500, 'May')
    income_service.add_income('5', 'bursa', 700, 'July')

    result = income_service.the_highest_income_for_the_last_12_months()
    assert result[0][0] == 'salariu'
    assert result[0][1] == 5500
    assert result[1][0] == 'bursa'
    assert result[1][1] == 1400
    assert result[2][0] == 'betting'
    assert result[2][1] == 200

