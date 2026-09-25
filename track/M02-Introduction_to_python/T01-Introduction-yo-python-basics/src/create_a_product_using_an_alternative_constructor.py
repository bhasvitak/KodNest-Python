class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_string(cls, data):
        name, price = data.split(",")
        return cls(name, int(price))


data = input().strip()
product = Product.from_string(data)

print(f"Product: {product.name}")
print(f"Price: {product.price}")