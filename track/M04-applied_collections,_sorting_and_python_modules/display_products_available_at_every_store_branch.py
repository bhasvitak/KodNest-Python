n = int(input())
branches = []

for _ in range(n):
    data = input().split()
    branch_name = data[0]
    products = data[1:]

    branches.append({
        "branch": branch_name,
        "products": products
    })

# Write your code here
for i in branches:
    for j in i["products"]:
        print(f"{i['branch']}: {j}")