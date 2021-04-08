from Domain.cost_validator import CostValidator
from Repository.file_repository import FileRepository
from Service.cost_service import CostService
from Tests.utils import clear_file


def test_add_cost():
    clear_file("cost-test.txt")
    cost_repository = FileRepository("cost-test.txt")
    cost_validator = CostValidator()
    cost_service = CostService(cost_repository, cost_validator)
    cost_service.add_cost('1', 'food', 1000, 'May')
    cost_service.add_cost('2', 'rent', 700, 'June')
    assert len(cost_service.get_all()) == 2
    added1 = cost_repository.find_by_id('1')
    assert added1.entity_id == '1'
    assert added1.name == 'food'
    assert added1.total_cost == 1000
    assert added1.month == 'May'
    added2 = cost_repository.find_by_id('2')
    assert added2.entity_id == '2'
    assert added2.name == 'rent'
    assert added2.total_cost == 700
    assert added2.month == 'June'
    try:
        cost_service.add_cost('1', 'other', 500, 'October')
        assert False
    except Exception:
        assert True

def test_delete_cost():
    clear_file("cost-test.txt")
    cost_repository = FileRepository("cost-test.txt")
    cost_validator = CostValidator()
    cost_service = CostService(cost_repository, cost_validator)
    cost_service.add_cost('1', 'food', 1000, 'May')
    cost_service.add_cost('2', 'rent', 700, 'June')
    assert len(cost_service.get_all()) == 2

    cost_service.delete_cost('1')
    assert len(cost_service.get_all()) == 1
    assert cost_repository.find_by_id('1') is None
    assert cost_repository.find_by_id('2') is not None

    try:
        cost_service.delete_cost('1')
        assert False
    except Exception:
        assert True

def test_update_cost():
    clear_file("cost-test.txt")
    cost_repository = FileRepository("cost-test.txt")
    cost_validator = CostValidator()
    cost_service = CostService(cost_repository, cost_validator)
    cost_service.add_cost('1', 'food', 1000, 'May')
    cost_service.add_cost('2', 'rent', 700, 'June')

    cost_service.update_cost('1','other','','')
    updated = cost_repository.find_by_id('1')
    assert updated.entity_id == '1'
    assert updated.name == 'other'
    assert updated.total_cost == 1000
    assert updated.month == 'May'

    try:
        cost_service.update_cost('3','',1232,'August')
        assert False
    except Exception:
        assert True

def test_cost_per_month():
    clear_file("cost-test.txt")
    cost_repository = FileRepository("cost-test.txt")
    cost_validator = CostValidator()
    cost_service = CostService(cost_repository, cost_validator)
    cost_service.add_cost('1', 'food', 1000, 'May')
    cost_service.add_cost('2', 'rent', 700, 'June')
    cost_service.add_cost('3', 'dsfdsf', 400, 'June')

    total_cost = cost_service.cost_per_month()
    assert total_cost['May'] == 1000
    assert total_cost['June'] == 1100
    assert total_cost['March'] == 0
    assert total_cost['February'] == 0


def test_costs_for_the_last_12_months():
    clear_file("cost-test.txt")
    cost_repository = FileRepository("cost-test.txt")
    cost_validator = CostValidator()
    cost_service = CostService(cost_repository, cost_validator)
    cost_service.add_cost('1', 'food', 1000, 'May')
    cost_service.add_cost('2', 'rent', 700, 'June')
    cost_service.add_cost('3', 'dsfdsf', 400, 'June')

    total_cost = cost_service.costs_for_the_last_12_months()
    assert total_cost == 2100


def test_cost_delete_all():
    clear_file("cost-test.txt")
    cost_repository = FileRepository("cost-test.txt")
    cost_validator = CostValidator()
    cost_service = CostService(cost_repository, cost_validator)
    cost_service.add_cost('1', 'food', 1000, 'May')
    cost_service.add_cost('2', 'rent', 700, 'June')
    cost_service.add_cost('3', 'dsfdsf', 400, 'June')

    cost_service.delete_all()
    assert len(cost_service.get_all()) == 0

def test_costs_in_descending_order():
    clear_file("cost-test.txt")
    cost_repository = FileRepository("cost-test.txt")
    cost_validator = CostValidator()
    cost_service = CostService(cost_repository, cost_validator)
    cost_service.add_cost('1', 'food', 1000, 'May')
    cost_service.add_cost('2', 'rent', 700, 'June')
    cost_service.add_cost('3', 'betting', 400, 'June')
    descending = cost_service.costs_in_descending_order()
    assert descending[0][0] == 'food'
    assert descending[0][1] == 1000
    assert descending[1][0] == 'rent'
    assert descending[1][1] == 700
    assert descending[2][0] == 'betting'
    assert descending[2][1] == 400