#7-8,9 Deli

#Declaring variables
sandwich_orders = ['Egg & cress club', 'Coronation egg mayo', 'Triple-decker steak', 'Club', 'Mozzarella & salami picnic baguette', 'Ploughman’s']
completed_orders = []

#go through list , print one by one and store to completed_orders
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'Preparing your {sandwich} sandwich!\nPrepared!')
    completed_orders.append(sandwich)

#Print out a list of completed_orders
print("\nMade sandwiches:")
for sandwich in completed_orders:
    print(f"\t-{sandwich} sandwich")
