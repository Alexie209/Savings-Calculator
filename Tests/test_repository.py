from Domain.entity import Entity
from Repository.file_repository import FileRepository
from Tests.utils import clear_file


def test_add_repository():
    clear_file("repository-test.txt")
    entitati_repository = FileRepository("repository-test.txt")

    entitate1 = Entity('1')

    entitati_repository.add(entitate1)
    assert len(entitati_repository.get_all()) == 1
    added = entitati_repository.find_by_id('1')
    assert added is not None
    assert added.entity_id == '1'

    try:
        entitate2 = Entity('1')
        entitati_repository.add(entitate2)
        assert False
    except Exception:
        assert True

def test_delete_repository():
    clear_file("repository-test.txt")
    entitati_repository = FileRepository("repository-test.txt")
    entitate1 = Entity('1')
    entitate2 = Entity('2')
    entitati_repository.add(entitate1)
    entitati_repository.add(entitate2)

    try:
        entitati_repository.delete('3')
        assert False
    except Exception:
        assert True

    entitati_repository.delete('1')
    assert len(entitati_repository.get_all()) == 1
    deleted = entitati_repository.find_by_id('1')
    assert deleted is None
    remaining = entitati_repository.find_by_id('2')
    assert remaining is not None
    assert remaining.entity_id == '2'

def test_update_repository():
    clear_file("repository-test.txt")
    entitati_repository = FileRepository("repository-test.txt")
    entitate1 = Entity('1')
    entitate2 = Entity('2')
    entitati_repository.add(entitate1)
    entitati_repository.add(entitate2)

    entitate3 = Entity('1')
    entitati_repository.update(entitate3)
    updated = entitati_repository.find_by_id('1')
    assert updated is not None
    assert updated.entity_id == '1'

    unchanged = entitati_repository.find_by_id('2')
    assert unchanged is not None
    assert unchanged.entity_id == '2'

    try:
        entitate4 = Entity('3')
        entitati_repository.update(entitate4)
        assert False
    except Exception:
        assert True