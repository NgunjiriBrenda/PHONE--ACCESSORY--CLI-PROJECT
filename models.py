from sqlalchemy import Column, Integer, String, Float, FLOAT
from sqlalchemy.ext.declative import declarative_base

Base = declarative_base()

class Accessories(Base):
    __tablename__ = 'accessories'