n = int(input())
products = []

for _ in range(n):
    product_name, price = input().split()
    products.append((product_name, int(price)))

# Write your code here
sorted_products = sorted(products , key=lambda product: (product[1],product[0]))
for i in sorted_products:
    print(*i)