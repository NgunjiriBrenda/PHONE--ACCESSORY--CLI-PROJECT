import click
from CRUD import (
    list_accessories, add_accessory, update_accessory, delete_accessory,
    list_customers, add_customer, update_customer, delete_customer
)

def main_menu():
    while True:
        click.secho("\n" + "="*40, fg="blue")
        click.secho("Welcome to Phone Accessory Manager!")
        click.secho("1. Accessory Management", fg="yellow")
        click.secho("2. Customer Management", fg="yellow")
        click.secho("3. Sale Management", fg="yellow")
        click.secho("4. Exit", fg="red")
        click.secho("="*40, fg="blue")

        user_prompt = click.prompt("Select Option", type=int)
        
        if user_prompt == 1:
            accessory_menu()
        elif user_prompt == 2:
            customer_menu()
        elif user_prompt == 3:
            click.secho("Goodbye!", fg="green")
            break
        else:
            click.secho("Invalid choice. Please try again.", fg="red")

def accessory_menu():
    while True:
        click.secho("\nAccessory Management", fg="green")
        click.secho("1. List Accessories", fg="yellow")
        click.secho("2. Add Accessory", fg="yellow")
        click.secho("3. Update Accessory", fg="yellow")
        click.secho("4. Delete Accessory", fg="yellow")
        click.secho("5. Back to Main Menu", fg="blue")
        
        user_prompt = click.prompt("Select Option", type=int)
        
        if user_prompt== 1:
            accessories = list_accessories()
            click.secho("\nAll Accessories:", fg="blue")
            for accessory in accessories:
                click.echo(f"ID: {accessory.id}, Name: {accessory.name}, Category: {accessory.category}, Price: ${accessory.price}, Stock: {accessory.stock}")
        
        elif user_prompt == 2:
            name = click.prompt("Accessory Name")
            category = click.prompt("Category")
            price = click.prompt("Price", type=float)
            stock = click.prompt("Stock", type=int)
            accessory = add_accessory(name, category, price, stock)
            click.secho(f"Added accessory: {accessory.name}", fg="green")
        
        elif user_prompt == 3:
            accessory_id = click.prompt("Accessory ID to update", type=int)
            name = click.prompt("New Name (press Enter to skip)", default="", show_default=False)
            category = click.prompt("New Category (press Enter to skip)", default="", show_default=False)
            price_str = click.prompt("New Price (press Enter to skip)", default="", show_default=False)
            stock_str = click.prompt("New Stock (press Enter to skip)", default="", show_default=False)
            
            price = float(price_str) if price_str else None
            stock = int(stock_str) if stock_str else None
            
            accessory = update_accessory(accessory_id, name or None, category or None, price, stock)
            if accessory:
                click.secho(f"Updated accessory: {accessory.name}", fg="green")
            else:
                click.secho("Accessory not found", fg="red")
        
        elif user_prompt == 4:
            accessory_id = click.prompt("Accessory ID to delete", type=int)
            if delete_accessory(accessory_id):
                click.secho("Accessory deleted successfully", fg="green")
            else:
                click.secho("Accessory not found", fg="red")
        
        elif user_prompt == 5:
            break

def customer_menu():
    while True:
        click.secho("\nCustomer Management", fg="green")
        click.secho("1. List Customers", fg="yellow")
        click.secho("2. Add Customer", fg="yellow")
        click.secho("3. Update Customer", fg="yellow")
        click.secho("4. Delete Customer", fg="yellow")
        click.secho("5. Back to Main Menu", fg="blue")
        
        user_prompt = click.prompt("Select Option", type=int)
        
        if user_prompt == 1:
            customers = list_customers()
            click.secho("\nAll Customers:", fg="blue")
            for customer in customers:
                click.echo(f"ID: {customer.id}, Name: {customer.name}, Email: {customer.email}")
        
        elif user_prompt == 2:
            name = click.prompt("Customer Name Phone")
            email = click.prompt("Email")
            phone = click.prompt("Phone")
            customer = add_customer(name, email, phone)
            click.secho(f"Added customer: {customer.name}", fg="green")
        
        elif user_prompt == 3:
            customer_id = click.prompt("Customer ID to update", type=int)
            name = click.prompt("New Name (press Enter to skip)", default="", show_default=False)
            email = click.prompt("New Email (press Enter to skip)", default="", show_default=False)
            phone = click.prompt("New Phone (press Enter to skip)", default="", show_default=False)
            
            customer = update_customer(customer_id, name or None, email or None)
            if customer:
                click.secho(f"Updated customer: {customer.name}", fg="green")
            else:
                click.secho("Customer not found", fg="red")
        
        elif user_prompt == 4:
            customer_id = click.prompt("Customer ID to delete", type=int)
            if delete_customer(customer_id):
                click.secho("Customer deleted successfully", fg="green")
            else:
                click.secho("Customer not found", fg="red")
        
        elif user_prompt == 5:
            break

if __name__ == "__main__":
    main_menu()