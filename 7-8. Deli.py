orders = ['Veggie', 'Steak & Cheese', 'Roast Beef', 'B.L.T.', 'Cold Cuts']

completed_orders = []

for order in orders:
    print(f"The order of {order} is ready.")
    completed_orders.append(order)

print ("\nList of completed orders:")
for order in completed_orders:
    print(order)
