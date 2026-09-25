inventory = {
    "Electronics": {
        "Mouse": 15,
        "Keyboard": 8
    },
    "Stationery": {
        "Notebook": 20,
        "Pen": 30
    },
    "Groceries": {
        "Rice": 12,
        "Milk": 10
    }
}

category = input().strip()
product = input().strip()
new_stock = int(input())

inventory[category][product] = new_stock

print(inventory)