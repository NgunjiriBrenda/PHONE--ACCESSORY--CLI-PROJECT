from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import relationship, sessionmaker  
from datetime import datetime

Base = declarative_base()

class Accessories(Base):  
    __tablename__ = 'accessories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    accessory_type = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    
 
    sales = relationship("Sales", back_populates="accessory")

class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20))
    email = Column(String(100))
    
    sales = relationship("Sales", back_populates="customer")

class Sales(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    accessory_id = Column(Integer, ForeignKey('accessories.id'), nullable=False)  
    quantity = Column(Integer, nullable=False, default=1)
    date = Column(DateTime, default=datetime.utcnow)
    accessory = relationship("Accessories", back_populates="sales")
    customer = relationship("Customers", back_populates="sales")


engine = create_engine("sqlite:///accessory.db")
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)