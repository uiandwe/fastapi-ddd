from email.policy import default
import sqlalchemy
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database.conn import Base


class AgentUser(Base):
    __tablename__ = "agent_user"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    agent_id = Column(String)
    username = Column(String)
    password = Column(String)

    def __str__(self):
        return '{0},{1},{2},{3},{4}, '.format(self.id, self.name, self.type, self.agent_id, self.username)
