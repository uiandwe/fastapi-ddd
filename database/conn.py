import logging

logger = logging.getLogger(__name__)  # get root logger
logger.setLevel(logging.DEBUG)

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os

env = os.getenv("env", "test")

# 데이터베이스 연결 설정

DATABASE_URL = "sqlite:///./test.db"

if env == "test":
    DATABASE_URL = "sqlite:///./test.db"
elif env == "dev":
    DATABASE_URL = "sqlite:///./dev.db"

print("DATABASE_URL", DATABASE_URL)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



###############################################################

# 도메인 클래스와 ORM 모델 매핑
from sqlalchemy.orm import registry, mapper
from dbms.order_lines import OrderLines
from domain.data_class import OrderLine
from dbms.batches import Batches
from domain.Batch import Batch
from dbms.allocations import Allocations
from domain.allocate import Allocate

mapper_registry = registry()
mapper_registry.map_imperatively(OrderLine, OrderLines.__table__)
mapper_registry.map_imperatively(Batch, Batches.__table__)
# mapper_registry.map_imperatively(Allocate, Allocations.__table__)

###############################################################
