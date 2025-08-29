from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Accessory(Base):
    __tablename__= "accessories"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)

    sales = relationship("Sales", back_populates="accessory")


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    sales = relationship("Sale", back_populates="customer")


class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    accessory_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    sale_date = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates = "sales")
    accessory = relationship("Accessory", back_populates="sales")


                         



