__author__ = 'Tom Stanley'

cost_of_items = int(0)
shipping_discount = float(.1)
total_cost = int(0)
# 10 % discount
total_items_to_ship = int(input("Number of items to ship:"))
while total_items_to_ship <= 0:
    print('Invalid number of items!')
    total_items_to_ship = int(input("Number of items to ship:"))
for i in range(0, total_items_to_ship, 1):
    cost_of_items += float(input("Price of Item:"))
if cost_of_items > 100:
    total_cost += cost_of_items
    shipping_discount *= total_cost
    total_cost -= shipping_discount
    print('Total price for {:} items is ${:.2f}'.format(total_items_to_ship, total_cost))
else:
    total_cost += cost_of_items
    print('Total price for {:} items is ${:.2f}'.format(total_items_to_ship, total_cost))


