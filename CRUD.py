from models import session, Accessories, Customers, Sales, Base, engine


#Add a new accessory
def add_accessory(name, accessory_type, price, stock):
    new_accessory = Accessories(name=name, accessory_type=accessory_type, price=price, stock=stock)
    session.add(new_accessory)
    session.commit()
    print(f"Added accessory: {name}")


    

                              


