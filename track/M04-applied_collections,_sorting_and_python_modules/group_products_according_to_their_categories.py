def group_products(products):
    products_by_category = {}

    # Write your grouping logic here
    for name, category in products:
        if category not in products_by_category:
            products_by_category[category] = []
        products_by_category[category].append(name)

    return products_by_category


n = int(input())
products = []

for _ in range(n):
    product_name, category = input().split()
    products.append((product_name, category))

products_by_category = group_products(products)

for category, names in products_by_category.items():
    print(category + ": " + " ".join(names))