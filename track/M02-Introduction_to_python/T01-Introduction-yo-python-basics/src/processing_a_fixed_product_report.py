# 1. Read inputs
product_id = input()
product_name = input()
category = input()
unit_price = float(input())
quantity = int(input())
reorder_level = int(input())

# 2. Store exactly five details in a tuple (do NOT include reorder_level)
product_record = (product_id, product_name, category, unit_price, quantity)

# 3. Access product ID and name using tuple indexes
indexed_product_id = product_record[0]
indexed_product_name = product_record[1]

# 4. Unpack the complete tuple into separate variables
rec_id, rec_name, rec_category, rec_price, rec_quantity = product_record

# 5. Calculate stock value
stock_value = rec_price * rec_quantity

# 6. Determine stock status using reorder level rule
if rec_quantity == 0:
    stock_status = "Out of Stock"
elif rec_quantity <= reorder_level:
    stock_status = "Reorder Required"
else:
    stock_status = "Sufficient Stock"

# 7. Display the output exactly as required
print(f"Product ID: {indexed_product_id}")
print(f"Product Name: {indexed_product_name}")
print(f"Category: {rec_category}")
print(f"Unit Price: {rec_price:.2f}")
print(f"Available Quantity: {rec_quantity}")
print(f"Stock Value: {stock_value:.2f}")
print(f"Stock Status: {stock_status}")