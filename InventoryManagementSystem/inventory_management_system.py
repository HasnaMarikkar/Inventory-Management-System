inventory ={}

#Adding Items
def add_item():
    name = input("Name of the item: ")
    category = input("Category: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))
    inventory[name] = {
        "category": category,
        "quantity": quantity,
        "price": price,
    }
    print(f"{name} successfully added in the inventory.")

#Remove Items
def remove_item():
    name = input ("Item to be removed: ")
    if name in inventory:
        del inventory[name]
        print(f"{name} successfully removed from the inventory.")
    else:
        print("Item not found, Try again!")

#Update Items
def update_items():
    name= input("Name of the item: ")
    if name in inventory:
        print("1. Update Name\n2. Update Category\n3. Update Quantity\n4. Update Price")
        choice = input("Choose an Option")
        if choice == "1":
            name = input("Name of the item: ")
            inventory[name] = inventory.pop(name)
        elif choice == "2":
            category = input("Category: ")
            inventory[name]["category"] = category
        elif choice =="3":
            quantity = int(input("Quantity: "))
            inventory[name]["quantity"] = quantity
        elif choice =="4":
            price = float(input("Price: "))
            inventory[name]["price"] = price
        else:
            print("Invalid Entry")
    else:
        print("NULL")

#View the Items
def view_items():
        if not inventory:
            print("ALL OUT!")
        else:
            print("{:<15} {:<15} {:<15} {:<15}".format("Name", "Category", "Quantity", "Price"))
            for name, data in inventory.items():
                print("{:<15} {:<15} {:<15} {:<15.2f}".format(
                    name, data["category"], data["quantity"], data["price"]
                ))
#Search Items
def search_item():
    keyword = input("Enter Item Name or Category: ").lower()
    found=False
    for name, data in inventory.items():
        if keyword in name.lower() or keyword in data["category"].lower():
            if not found:
                print("{:<15} {:<15} {:<15} {:<15.2f}".format("Name", "Category", "Quantity","Price"))
                found=True
            print("{:<15} {:<15} {:<15} {:<15.2f}".format(name, data["category"], data["quantity"], data["price"]))
    if not found:
        print("Invalid Item or Category Entry!")

#Save Items to the Inventory
def save_inventory():
    with open("inventory.txt","w") as file:
        for name, data in inventory.items():
            file.write(f"{name}, {data['category']},{data['quantity']},{data['price']}\n")
    print("Inventory Saved Successfully!")

#Loading Inventory from the File
def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                if line.strip():  # skip empty lines
                    name, category, quantity, price = line.strip().split(",")
                    inventory[name] = {
                        "category": category,
                        "quantity": int(quantity),
                        "price": float(price)
                    }
        print("Inventory Successfully Loaded!")
    except FileNotFoundError:
        print("Inventory Not Found, Retry!")

#Menu
def main():
    load_inventory()
    while True:
        print("\n The Inventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. View All Items")
        print("5. Search Items")
        print("6. Save Inventory")
        print("7. Load Inventory")
        print("8. Exit")

        choice=input("Enter Choice: ")

        if choice=="1":
            add_item()
        elif choice=="2":
            remove_item()
        elif choice=="3":
            update_items()
        elif choice=="4":
            view_items()
        elif choice=="5":
            search_item()
        elif choice=="6":
            save_inventory()
        elif choice=="7":
            load_inventory()
        elif choice=="8":
            print("Exiting!")
            save_inventory()
            break
        else:
            print("Invalid Input")

if __name__ == '__main__':
    main()