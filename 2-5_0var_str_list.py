# Welcome to Python!

print('Welcome to the "Python World"!')

# Declaring strings
first_name = "       JoHN "
last_name = " clOvER  "

# Use of f string to assign to a variable and using a title and strip methe right format
full_name = "{} {}".format(first_name.strip(), last_name.strip())

print("Hello, {}!\nThis was made with strings:\n\t - '{}'\n\t - '{}'"
      .format(full_name.title(), first_name, last_name))

# Declaring a number using addition, subtraction and multiplication
num = 13 + 2 * 21 - (7 + 41)

# Declaring a CONSTANT should be in capital letters to
# indicate that it should not be changed
NUM_CONST = 5

# Printing a number
print ("Number:", num,"\nAnother number:", NUM_CONST)

# LIST's
# Declaring a list
bicycles = ['trek', 'redline', 'cube', 'specialized', 'bmx']

# printing a whole list (RAW FORMAT)
print("This is a raw list: ", bicycles)

# printing an item in the list with index 0 (a.k.a. first item)
print("Printing a list item with the 0 index:", bicycles[0].title())

# printing an item in the list with index 4 (a.k.a. now last item)
print("My first bicycle was a {}.".format(bicycles[4].upper()) )

# Using the append method you add an item to the back of the list and
# access it with [-1] regardles of the number of items in the list
# eg. bicycles[-3] will return the THIRD item from the end
bicycles.append("Canyon")

print("Last list item (appended) is", bicycles[-1])

#Changing a value of the second item

print("Before [1]:", bicycles[1])
bicycles[1] = "bianchi"
print("After [1]:", bicycles[1])

#removing last item but returnes value to be worked with
print('Before "pop":', bicycles)
last_bike = bicycles.pop()
print('After "pop":', bicycles, "\nPoped item:", last_bike)

#inserting value back to the list as first item
bicycles.insert(0,last_bike.upper())
print('After "insert":', bicycles)

#sorting a LIST (reverse default is FALSE) and printing length
bicycles.sort(reverse=True)
print('After "sort":', bicycles,"\nLength of list is:", len(bicycles))

#Working with lists
favorites = ['Suncica',
             'Ivan',
             'Karla',
             'Borna',
             'Gea',
             'Helena',
             'Martin',
             'Irena',
             'Mirjana']

# FOR Loop
print ("Favorites:")
for person in favorites:
    print("\t-{}".format(person.title()))
