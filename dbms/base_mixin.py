import sqlalchemy
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid


class BaseMixin:
    id = Column(Integer, primary_key=True, index=True)
    create_at = Column(DateTime(timezone=True),
                       server_default=sqlalchemy.sql.func.now())
    modified_at = Column(DateTime(timezone=True))
    uuid = Column(UUID(as_uuid=True), index=True,  default=uuid.uuid4)
