from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Accessory, Customer

engine = create_engine("sqlite:///accessory.db", echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session= Session()

#Add Accessories
accessory = [
    Accessory(name ="Silicon Phone Case", type="Case", price = 1000, stock= 50),
    Accessory(name = "Phone Charm", type="Charm", price = 250, stock=100),
    Accessory(name = "Screen Protector", type="Protector", Price = 500,stock=200 ),
    Accessory(name = "Wireless Charger", type="Charger", Price = 350, stock=100),
]

customers = [
    Customer(name="Jasmine James", email="jasmine@gmail.com"),
    Customer(name="Bella Keith", email="bella@gmail.com"),
    Customer(name="Josh Andrew", email="josh@gmail.com"),
    Customer(name="Maureen Karimi", email="molly@gmail.com"),
]

session.add_all(accessory+ customers)

session.comit()

print("Database seeded successfully")