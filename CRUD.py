from models import session, Accessories, Customers, Sales, Base, engine


#Add a new accessory
def add_accessory(name, accessory_type, price, stock):
    new_accessory = Accessories(name=name, accessory_type=accessory_type, price=price, stock=stock)
    session.add(new_accessory)
    session.commit()
    print(f"Added accessory: {name}")


#Update accessrory stock
def update_accessory_stock(accessory_id, new_stock):
    accessory = session.query(Accessories.filter_by(id=accessory_id).first())
    if accessory:
        accessory.stock = new_stock
        session.commit()

#View all accessories
def view_accessories():
    accessories = session.query(Accessories).all()
    for accessory in accessories:
        print(f"Id: {accessory.id}, Name: {accessory.name}, Accessory_type: {accessory.accessory_type}, Price: {accessory.price}, Stock: {accessory.stock}")
        return accessories
    

#Delete accessory
def delete_accessory(accssory_id):
    accessories = session.query(Accessories.filter_by(id=accessories).first())

    if accessories:
        session.delete(accessories)
        session.commit()
        
    

                              


