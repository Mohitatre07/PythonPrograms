import qrcode  # Library for generating QR codes
import pycountry  # Library for working with ISO country and currency codes

class MenuItem:
    def __init__(self, name, price):
        self.name = name  # Name of the menu item
        self.price = price  # Price of the menu item

class Order:
    def __init__(self):
        self.items = []  # List to store ordered items

    def add_item(self, item):
        self.items.append(item)  # Add an item to the order

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price  # Calculate total price of the order
        return total

    def generate_bill(self, currency):
        bill = f"Order Details (in {currency}):\n"  # Header for the bill
        for item in self.items:
            bill += f"{item.name}: {item.price} {currency}\n"  # Add each item to the bill
        bill += f"Total: {self.calculate_total()} {currency}"  # Add total price to the bill
        return bill

def generate_qr_code(data, filename):
    # Generate QR code from data and save it to a file
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def submit_menu():
    # Create a dictionary of menu items
    menu = {}

    print("Enter menu items and prices (press 'done' to finish):")
    while True:
        item_name = input("Enter item name: ").capitalize()
        if item_name == "Done":
            break
        item_price = float(input("Enter item price: "))
        menu[item_name] = MenuItem(item_name, item_price)  # Add menu item to the menu dictionary

    return menu

def select_country():
    # Prompt user to select a country and return its name and currency code
    print("Select your country:")
    for country in pycountry.countries:
        print(f"{country.name}: {country.alpha_2}")
    country_code = input("Enter your country code (ISO 3166-1 alpha-2): ").upper()
    country = pycountry.countries.get(alpha_2=country_code)
    if country:
        currency_code = pycountry.currencies.get(numeric=country.numeric).alpha_3
        return country.name, currency_code
    else:
        print("Invalid country code. Defaulting to USA.")
        country = pycountry.countries.get(alpha_2="US")
        currency_code = pycountry.currencies.get(numeric=country.numeric).alpha_3
        return country.name, currency_code

def main():
    # Main function to run the program
    print("Welcome to the Meal Ordering App!\n")

    country, currency = select_country()  # Get country and currency information

    menu = submit_menu()  # Create menu

    order = Order()  # Create an order

    print("\nMenu:")
    for item_name, item in menu.items():
        print(f"{item_name}: {item.price} {currency}")  # Display menu to user

    while True:
        choice = input("Enter item to order (press 'done' to finish): ").capitalize()
        if choice == "Done":
            break
        elif choice in menu:
            order.add_item(menu[choice])  # Add selected items to the order
        else:
            print("Invalid choice!")

    bill = order.generate_bill(currency)  # Generate bill
    print("\n", bill)
    generate_qr_code(bill, "bill_qr.png")  # Generate QR code for the bill
    print("QR code generated for the bill.")

if __name__ == "__main__":
    main()
