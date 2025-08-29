import click

from CRUD import add_accessory, update_accessory_stock, view_accessory_stock, delete_accessory

def main_menu():
    while True:
        click.secho("Welcome to the Phone Accessory Store Manager",fg="red")
        click.secho("Select Option to Proceed",fg="blue")
        click.secho("1.Accessories", fg="yellow")
        click.secho("2.Customers", fg="yellow")
        click.secho("3.Sales", fg="yellow")
        click.secho("4.Exit", fg="blue")

        user_input = click.prompt("Select Option", type=int)

        if user_input == 1:
            accessory_menu()

        elif user_input == 2:
            customer_menu()

        elif user_input == 3:
            sales_menu()


def accessory_menu():
    while True:

#rom CRUD import add_accessory, add_customer, add_sales


    
    

