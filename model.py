from sqlalchemy import Column, Integer, String

from alchemy.base_model import BaseModel

class Coze(BaseModel):
    __tablename__ = "coze"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    key = Column(String(100))

class WorkFlow(BaseModel):
    __tablename__ = "work_flow"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    workflow_id = Column(String(100))
