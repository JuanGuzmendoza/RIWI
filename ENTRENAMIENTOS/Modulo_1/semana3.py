


inventario=[]
#===============
#-BUSINESS LOGIC
#===============
def search_product(product_name):
    """
    This function find a product to the inventory.
    It takes the name of product  and find the product in the inventory.
    it is userful to find a product to the inventory
    """
    for i in inventario:
        if product_name in i:
                print("=== Product Found ===")
                print(f"📦 Name: {product_name}")
                print(f"🧮 Amount: {i[product_name]["amount"]}")
                print(f"💲 Price: {i[product_name]["price"]}")
                print("=====================")
                return True
    print("🚫 Product not found")
    return False


def create_product(product_name, product_amount, product_price):
    """
    this function adds a new product to the inventory.
    It takes the name , amount and price , and puts them in the list.
    it is useful to sotre new produts in the system 
    """
    inventario.append({product_name:{
        "amount":int((product_amount)),
        "price":float((product_price))
    }})


def update_price_product(product_name,new_price_product):
    """
    This function updates the price of a product in the inventory.
    It takes the product name and the new price.
    We use it when we need to change the product price.
    """
    for i in inventario:
        if product_name in i:
            i[product_name]["price"]=float(new_price_product)
            return True
    return False


def delete_product(product_name):
    """
    This function deletes a product in the inventory.
    It takes the product name and removes it from the list.
    We use it when we need to delete a product that is no longer needed.
    """

    for i in inventario:
        if product_name in i:
            inventario.remove(i)
            print(f"✅ The product '{product_name}' was successfully deleted.")
            return True
    print("🚫 Product not found.")
    return False


def total_inventory_value():
    """
    This function shows the total value of the inventory.
    It takes the main list (inventario) and multiplies the amount and price of each product.
    We use it when we need to see how much the inventory is worth.
    """

    total = sum(map(lambda item: list(item.values())[0]["amount"] * list(item.values())[0]["price"], inventario))
    print(f"💰 Total inventory value: ${total}")
    return total

        

#=====================
#-VALIDATION FUNCTIONS
#=====================
def validation_numbers(value,tipe):
    """
    This function validates the type of a value.
    It takes a type (int or float) and checks if the value matches it.
    We use it when we need to validate numbers in the program.
    """
    try:
        return True if tipe(value)>0 else print("only can values positive")
    except:
        print(f"only can of values positive and {tipe}")
        return False


def validation_equality_product(product_name):
    """
    This function checks if a product exists in the inventory.
    It takes the product name and looks for it in the inventory list.
    If the product exists, the function returns True.
    If it does not exist, the function returns False.
    We use it when we need to verify if a product is already in the inventory.
    """

    for i in inventario:
        if product_name in i:
            return True
    return False



#==============
#-MENU INTERFAZ
#==============
def menu_interface():
    """
    This function shows the main menu to select one option
    """
    print("--🛒 \033[92m  DIGITAL INVENTORY \033[0m 🛒-- ".center(40))
    print("1. Add a product")
    print("2. Search a product")
    print("3. Update the price")
    print("4. Delete a product")
    print("5. Show total inventory value")
    print("6. show all product in inventory")
    print("--Select one option")
    option=input("-")
    print("\n")
    return option


def show_all_products():
    """
    This function shows the estorage of products in the inventory
    """
    if not inventario:
        print("🚫 The inventory is empty.")
        return False
    print("=== 🗂️ \033[33mAll Products in Inventory\033[0m ===")
    for product in inventario:
        for name, details in product.items():
            print(f"📦 Name: {name}")
            print(f"🧮 Amount: {details['amount']}")
            print(f"💲 Price: {details['price']}")
            print("-" * 30)


#==============
#-MAIN FUNCTION
#==============
def main_function():
    """
    This function manages the main logic of the code to control the inventory CRUD.
    """

    while True:
        match menu_interface():
            #CASE -1 
            case"1":
                while True:
                    print("="*30)
                    print("=== 📦\033[36mAdd a product\033[0m📦 ")
                    product_name=input("-Name of product \n")
                    # The (while True) is used to validate the type of value with its function: validation_numbers 
                    while True: 
                        product_price=input("-Price of the product\n")
                        if validation_numbers(product_price,float):
                            break
                    while True:
                        product_amount=input("-Amount of product \n")
                        if validation_numbers(product_amount,int):
                            break
                    # After all the validations in the price and amount inputs.
                    # This code validates if the product already exists in the inventory to repeat the cycle or add the new product
                    if validation_equality_product(product_name):
                        print("\033[31m !the value already exists! \033[0m!")   
                        continue  
                    else:                    
                        create_product(product_name, product_amount, product_price)
                        break
                    
            #CASE -2 
            case"2":
                print("=== 📦\033[36mSearch a product\033[0m📦 ")
                product_name=input("-Name of product to Search details\n")
                # Uses the search_product() function with the product_name variable
                search_product(product_name)
                
            #CASE -3
            case"3":
                print("=== 📦\033[Update the price of a product\033[0m📦 ")
                # Uses the show_all_products() function to validate if the inventory has products
                if show_all_products()==False:
                    continue    
                while True:
                    product_name=input("-Name of product to update price\n")
                    if validation_equality_product(product_name):
                        while True:
                            product_price=input("-Price of product \n")
                            if validation_numbers(product_price,float):
                                break
                        update_price_product(product_name,product_price)
                        print("=== Product price updated successfully ===")
                        break
                    else:
                        print("🚫 Product not found. Please try again.")
                        
            #CASE -4
            case"4":
                print("=== 🗑️ Delete a Product ===")
                if show_all_products()==False:
                    continue    
                while True:
                    product_name = input("- Name of product to delete\n")
                    if validation_equality_product(product_name):
                        delete_product(product_name)
                        break
                    else:
                        print("🚫 Product not found. Please try again.")
                        
            #CASE -5
            case"5":
                total_inventory_value()
            
            #CASE -6
            case"6":
                show_all_products()
            
            #CASE -Any
            case _:
                break

main_function()


