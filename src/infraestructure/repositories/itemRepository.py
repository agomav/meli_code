from infraestructure.dbconnector import item
from infraestructure.repositories import BaseRepository
from domain.repositories import intemRepositoryInterface


class itemRepository(BaseRepository.BaseRepository):

    def insert(self, new_item):
        with self.db_connection.begin():
            self.db_connection.execute(
                item.insert(),
                new_item
            )

