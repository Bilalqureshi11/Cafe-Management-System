menu = {
    'Burger': 60,
    'Pizza': 120,
    'Fries': 50,
    'Pasta': 40,
    'Coffee': 80,
}

print("Welcome to Bilal's Cafe")
print('Burger: Rs.60\nPizza: Rs.120\nFries: Rs.50\nPasta: Rs.40\nCoffee: Rs.80')

order_total = 0

while True:
    item = input('Enter the name of the item you want to order: ').title()

    if item in menu:
        order_total += menu[item]
        print(f'Your item {item} has been added to your order.')
    else:
        print(f'Ordered item {item} is not available!')

    another_order = input('Do you want to add another item? (Yes/No): ').title()
    if another_order != 'Yes':
        break

print(f'The total amount to pay is Rs.{order_total}')
