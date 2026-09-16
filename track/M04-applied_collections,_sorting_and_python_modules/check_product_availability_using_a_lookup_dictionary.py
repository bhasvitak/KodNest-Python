def check_availability(inventory, product_code):
    # Write your dictionary lookup logic here
    if product_code in inventory.keys():
        if inventory[product_code] != 0:
            return f"Available: {inventory[product_code]}"
        else:
            return "Out of stock"
    else:
        return "Product not found"


inventory = {
    "P101": 12,
    "P102": 0,
    "P103": 7,
    "P104": 3
}

product_code = input()
print(check_availability(inventory, product_code))