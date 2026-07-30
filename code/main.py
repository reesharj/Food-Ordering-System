# Import necessary modules 
from typing import List, Dict, Tuple 
 
# Base Menu class 
class Menu: 
    def __init__(self): 
        # Initialize a dictionary to store menu items and their prices 
        self.items: Dict[str, float] = { 
            'Food': { 
                'Nasi Lemak Biasa': 3.00, 
                'Nasi Goreng Kampung': 6.00, 
                'Nasi Goreng Tomyam': 8.00, 
                'Maggi Goreng Pattaya': 6.50, 
                'Mee Goreng Biasa': 5.00, 
                'Bihun Goreng Biasa': 5.00, 
                'Roti Canai Special': 3.00 
            }, 
            'Drinks': { 
                'Lemonade': 2.00, 
                'Water': 0.00, 
                'Juice': 3.50, 
                'Tea': 3.00, 
                'Kopi': 2.00 
            } 
        } 
 
    # Add a new item to the menu 
    def add_item(self, category: str, name: str, price: float): 
        """Add a new item to the menu.""" 
        if category in self.items: 
            self.items[category][name] = price 
        else: 
            self.items[category] = {name: price} 
 
    # Remove an item from the menu 
    def remove_item(self, category: str, name: str): 
        """Remove an item from the menu.""" 
        if category in self.items and name in self.items[category]: 
            del self.items[category][name] 
 
    # Display the menu items 
    def display_menu(self): 
        """Display the menu items.""" 
        print("Menu:") 
        for category, items in self.items.items(): 
            print(f"{category}:") 
            for name, price in items.items(): 
                print(f"  {name}: RM{price:.2f}") 
 
    # Get the price of a menu item 
    def get_price(self, category: str, name: str) -> float: 
        """Get the price of a menu item.""" 
        return self.items.get(category, {}).get(name, 0.0) 
 
# Order class inheriting from Menu 
class Order(Menu): 
    def __init__(self): 
        super().__init__() 
        # Initialize an empty list to store the order items 
        self.order_items: List[Tuple[str, str, int]] = [] 
 
    # Add an item to the order 
    def add_to_order(self, category: str, name: str, quantity: int): 
        """Add an item to the order.""" 
        if category in self.items and name in self.items[category]: 
            self.order_items.append((category, name, quantity)) 
            print(f"{quantity} {name} added to the order.") 
        else: 
            print(f"Sorry, {name} is not available on the menu.") 
 
    # Remove an item from the order 
    def remove_from_order(self, name: str): 
        """Remove an item from the order.""" 
        initial_length = len(self.order_items) 
        self.order_items = [item for item in self.order_items if item[1] != 
name] 
        if len(self.order_items) < initial_length: 
            print(f"{name} removed from the order.") 
        else: 
            print(f"{name} is not in your order.") 
 
    # Display the current order 
    def display_order(self): 
        """Display the current order.""" 
        print("Current Order:") 
        total = 0.0 
        for category, name, quantity in self.order_items: 
            price = self.get_price(category, name) * quantity 
            total += price 
            print(f"{name} x{quantity} - RM{price:.2f}") 
        print(f"Total: RM{total:.2f}") 
 
    # Calculate the total cost of the order 
    def calculate_total(self) -> float: 
        """Calculate the total cost of the order.""" 
        total = sum(self.get_price(category, name) * quantity for category, 
name, quantity in self.order_items) 
        return total 
 
# Main function for user interaction 
def main(): 
    # Print welcome message 
    print("Welcome to JARS Restaurant!") 
 
    # Create an order 
    order = Order() 
 
    # Main loop for the ordering system 
    while True: 
        print("\n1. Display Menu") 
        print("2. Add to Order") 
        print("3. Remove from Order") 
        print("4. Display Order") 
        print("5. Calculate Total") 
        print("6. Exit") 
 
        choice = input("Enter your choice: ") 
        if choice == '1': 
            order.display_menu() 
        elif choice == '2': 
category = input("Enter the category (Food/Drinks): ") 
item = input("Enter the item name: ") 
quantity = int(input("Enter the quantity: ")) 
order.add_to_order(category, item, quantity) 
elif choice == '3': 
item = input("Enter the item name to remove: ") 
order.remove_from_order(item) 
elif choice == '4': 
order.display_order() 
elif choice == '5': 
total = order.calculate_total() 
print(f"Your total is: RM{total:.2f}") 
elif choice == '6': 
print("Thank you for your order!") 
break 
else: 
print("Invalid choice, please try again.") 
if __name__ == "__main__": 
main()
