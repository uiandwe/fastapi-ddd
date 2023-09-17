import abc
from domain.Batch import Batch


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch: Batch):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> Batch:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, reference) -> Batch:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, batch):
        self.session.add(batch)

    def get(self, reference):
        return self.session.query(Batch).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(Batch).all()

    def delete(self, batch):
        tt = self.session.query(Batch).filter(Batch.reference == batch.reference,
                                              Batch.sku == batch.sku,
                                              Batch.eta == batch.eta,
                                              Batch._purchased_quantity == batch._purchased_quantity).one()
        self.session.delete(tt)
        self.session.commit()