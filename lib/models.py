from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import relationship, sessionmaker  
from datetime import datetime

Base = declarative_base()

class Accessory (Base):  
    __tablename__ = 'accessories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    category = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    
 
    sales = relationship("Sale", back_populates="accessory")

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20))
    email = Column(String(100))
    
    sales = relationship("Sale", back_populates="customer")

class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    accessory_id = Column(Integer, ForeignKey('accessories.id'), nullable=False)  
    quantity = Column(Integer, nullable=False, default=1)
    date = Column(DateTime, default=datetime.utcnow)
    accessory = relationship("Accessory", back_populates="sales")
    customer = relationship("Customer", back_populates="sales")


engine = create_engine("sqlite:///accessory.db")
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)