from models.dbms.data_class import OrderLine
from models.dbms.exceptions import OutOfStock
from typing import Optional, List, Set
from models.dbms.Batch import Batch


def allocate(line: OrderLine, batches: List[Batch]) -> str:
    try:
        batch = next(b for b in sorted(batches) if b.can_allocate(line))
        batch.allocate(line)
        return batch.reference
    except StopIteration:
        raise OutOfStock(f"Out of stock for sku {line.sku}")