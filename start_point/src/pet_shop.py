# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, cash):
    shop["admin"]["total_cash"] += cash

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, num_of_pets_sold):
    shop["admin"]["pets_sold"] += num_of_pets_sold

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    pets_of_breed = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pets_of_breed.append(pet)
    return pets_of_breed
    
def find_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            return pet
        
def remove_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            shop["pets"].remove(pet)

def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

# Optional --
def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

# Integration --
def sell_pet_to_customer(shop, pet, customer):
    if pet in shop["pets"]:
        if customer["cash"] >= pet["price"]:
            customer["cash"] -= pet["price"]
            customer["pets"].append(pet)
            shop["admin"]["pets_sold"] += 1
            shop["admin"]["total_cash"] += pet["price"]
            shop["pets"].remove(pet)

            