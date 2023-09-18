from domain.allocate import Allocate
from repository.sql_repository import AbstractRepository
from domain.data_class import OrderLine

class InvalidSku(Exception):
    pass


def is_valid_sku(sku, batches):
    return sku in {b.sku for b in batches}


def allocate(line: OrderLine, repo: AbstractRepository, session) -> str:
    batches = repo.list()
    if not is_valid_sku(line.sku, batches):
        raise InvalidSku(f"Invalid sku {line.sku}")
    batchref = Allocate(line, batches)
    session.commit()
    return batchref
