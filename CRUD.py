from lib.models import Accessory, Customer, Session

def get_session():
    return Session()

def list_accessories():
    session = get_session()
    accessories = session.query(Accessory).all()
    return accessories

def add_accessory(name, category, price, stock):
    session = get_session()
    try:
        accessory = Accessory(name=name, category=category, price=price, stock=stock)
        session.add(accessory)
        session.commit()
        session.refresh(accessory) 
        return accessory
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close() 


def view_accessory(accessory_id):
    session = get_session()
    accessory = session.query(Accessory).filter(Accessory.id == accessory_id).first()
    return accessory

def update_accessory(accessory_id, name=None, category=None, price=None, stock=None):
    session = get_session()
    accessory = session.query(Accessory).filter(Accessory.id == accessory_id).first()
    
    if accessory:
        if name:
            accessory.name = name
        if category:
            accessory.category = category
        if price:
            accessory.price = price
        if stock is not None:
            accessory.stock = stock
        
        session.commit()
    
    return accessory

def delete_accessory(accessory_id):
    session = get_session()
    accessory = session.query(Accessory).filter(Accessory.id == accessory_id).first()
    
    if accessory:
        session.delete(accessory)
        session.commit()
        return True
    
    return False

def list_customers():
    session = get_session()
    customers = session.query(Customer).all()
    return customers

def add_customer(name, email, phone=None): 
    session = get_session()
    try:
        customer = Customer(name=name, email=email, phone=phone)
        session.add(customer)
        session.commit()
        session.refresh(customer)  
        return customer
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def view_customer(customer_id):
    session = get_session()
    customer = session.query(Customer).filter(Customer.id == customer_id).first()
    return customer

def update_customer(customer_id, name=None, email=None):
    session = get_session()
    customer = session.query(Customer).filter(Customer.id == customer_id).first()
    
    if customer:
        if name:
            customer.name = name
        if email:
            customer.email = email
        
        session.commit()
    
    return customer

def delete_customer(customer_id):
    session = get_session()
    customer = session.query(Customer).filter(Customer.id == customer_id).first()
    
    if customer:
        session.delete(customer)
        session.commit()
        return True
    
    return False