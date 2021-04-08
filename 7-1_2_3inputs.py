#Ex. 7-1,2,3 Rental car, Restaurant, Number input

car = input("What car would you like to drive? >>")
print (f"Looking for your {car.title()}.\nFound the perfect one for you!")

restaurant = input(f"What restaurant would you like to go with your {car.title()}? >>")
print(f"Fantastic choice!\nYou have arrived at destination: '{restaurant.title()}'.")

num = input("Tell me a number, any number.. >>")
if int(num) % 5 == 0:
    print(f"The number {num} is divisible by 5, I like it! :)")
else:
    print(f"Your number {num} is boring. :|")
