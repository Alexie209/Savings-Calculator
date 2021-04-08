from copy import deepcopy

import jsonpickle as jsonpickle

from Domain.entity import Entity


class FileRepository:
    def __init__(self, filename):
        self.__storage = {}
        self.__filename = filename

    def __read_file(self):
        '''
        it reads the data from the file
        :return:
        '''
        try:
            with open(self.__filename, 'r') as fp:
                # return json.load(fp)
                self.__storage = jsonpickle.decode(fp.read())
        except:
            self.__storage = {}

    def __write_file(self):
        '''
        it writes the data to file
        :return:
        '''
        with open(self.__filename, 'w') as fp:
            # json.dump(lista, fp)
            fp.write(jsonpickle.encode(self.__storage))

    def find_by_id(self, entity_id):
        '''
        it finds the entity after its id
        :param entity_id: string
        :return: the entity whith the id: entity_id or None if it doesn't exist
        '''
        self.__read_file()
        if entity_id in self.__storage:
            return deepcopy(self.__storage[entity_id])
        return None

    def get_all(self):
        self.__read_file()
        return deepcopy(list(self.__storage.values()))

    def add(self, entity: Entity):
        '''
        adds an entity
        :param entity: the entity to add to the list
        :return:
        '''
        if self.find_by_id(entity.entity_id):
            raise KeyError(f"It already exists an entity with the id {entity.entity_id}")
        self.__storage[entity.entity_id] = entity
        self.__write_file()

    def delete(self, entity_id):
        '''
        it delets an entity after its id
        :param entity_id: string
        :return:
        '''
        if self.find_by_id(entity_id) is None:
            raise KeyError(f"It doesn't exist any entity with the id {entity_id}")
        del self.__storage[entity_id]
        self.__write_file()

    def update(self, entitate: Entity):
        '''
        it updates an entity after its id
        :param entitate: the entity to update
        :return:
        '''
        if self.find_by_id(entitate.entity_id) is None:
            raise KeyError(f"It doesn't exist any entity with the id {entitate.entity_id}")

        self.__storage[entitate.entity_id] = entitate
        self.__write_file()