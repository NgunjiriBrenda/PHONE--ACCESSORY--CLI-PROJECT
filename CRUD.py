from models import session, Accessories, Customers, Sales, Base, engine


#Add a new accessory
def add_accessory(name, accessory_type, price, stock):
    new_accessory = Accessories(name=name, accessory_type=accessory_type, price=price, stock=stock)
    session.add(new_accessory)
    session.commit()
    print(f"Added accessory: {name}")

# Updates an existing accessory
def update_accessory_stock(accessory_id, new_stock):
    accessory = session.query(Accessories).filter_by(id=accessory_id).first()
    if accessory():
        accessory.stock = new_stock
        session.commit()
        print(f"Updated stock for '{accessory.name}' to {new_stock}")
    else:
        print(f"Accessory with ID {accessory_id}not found")


#view all accessories
def view_accessories():
    accessories = session.querry(Accessories).all()
    for accessory in accessories:
        print(f'ID: {accessory.id}, Name: {accessory.name}, Type:{accessory.accessory_type}, Price: ${accessory.price}, Stock:{accessory.stock}')
        return accessories
    