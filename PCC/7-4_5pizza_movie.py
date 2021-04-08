#Ex. 7-4,5 Pizza Toppings and Movie Tickets

first_message = "Preparing your pizza..\n"
message = "What topping(s) would you like?\n"
message += "Enter (Q or Quit) to exit. >>"

toppings = []
active_pizza = True

print(first_message)
while active_pizza:
    topping = input(message)
    if topping.lower() == 'quit' or topping.lower() == 'q':
        active_pizza = False
        continue
    toppings.append(topping)
    print(f'Adding: {topping}')

for num in range(0, len(toppings) + 1):
    toppings_s = ', '.join(map(str, toppings[num]))

print(f"Your pizza with following toppings has been prepared: {toppings}")

active_movie = None
while active_movie == None:
    choice = input("We hope that your pizza was good. How about a movie ?").lower()
    if choice == "no" or choice == "n":
        active_movie = False
    elif choice == "yes" or choice == "y":
        active_movie = True

while active_movie:
    num_people = int(input("How many people are coming with you?"))
    num_people += 1
    total = 0
    for i in range(0, num_people):
        age = int(input('Enter persons age: >'))
        if age < 3:
            price = 5
        elif age >=3 and age <=12:
            price = 10
        elif age >= 12 and age < 80:
            price = 18
        else:
            price = 0
        total += price
        print(f"Total price for {num_people} is {total}.")
    another = input("Another movie ? (yes or y to confirm)")
    if another.lower() == "yes" or another.lower() == "y":
        continue
    else:
        active_movie = False
