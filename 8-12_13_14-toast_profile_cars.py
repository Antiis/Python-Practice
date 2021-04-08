#8-12,13,14

#Toast
def make_toast(*ingredients):
    if len(ingredients) < 1:
        print("\nMade some toasted bread.")
    else:
        print("\nMade a toast with:")
        for ingredient in ingredients:
            print(f'- {ingredient}')

make_toast("Tomatoes","Cheese","Ham","Egg","Salad")
make_toast()

#profile
def build_profile(first_name, last_name, **user_profile):
    user_profile['first_name'] = first_name.title()
    user_profile['last_name'] = last_name.title()
    return user_profile

print(build_profile('Antoni', 'Eisenkohl', age = 24, has_SO = True, footsize = 43))

#cars

def make_car(make, type, **car_attributes):
    car_attributes['make'] = make.upper()
    car_attributes['type'] = type.title()
    return car_attributes

car = make_car('BMW', 'cabrio', color = 'Blue', sport_version = True)
print(car)
