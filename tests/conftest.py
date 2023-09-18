import pytest
from sqlalchemy.orm import sessionmaker, clear_mappers
from sqlalchemy_utils import database_exists, create_database, drop_database

from database.conn import engine, Base


@pytest.fixture(scope="module")
def db():
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(bind=engine)
    connection = engine.connect()
    yield connection
    connection.close()
    drop_database(engine.url)


# 데이터베이스 테스트 세션
@pytest.fixture(scope="module")
def session(db):
    transaction = db.begin()
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
    yield session
    session.close()  # 세션을 닫음
    transaction.rollback()
