#Welcome to the pizza project

## Python CC - 4-1 Pizzas

pizze = ['Slavonska', 'Diavola', '4 Vrste sira', 'Capricosa']

print(pizze)

print("Najbolje pizze:")
for pizza in pizze[:4]:
    print("Volim picu koja se zove", pizza + ".")

pizz1=pizze[:2]
pizz2=pizze[1:3]
pizz3=pizze[2:]

print("Pizze na pocetku -", pizz1)
print("Pizze na sredini -", pizz2)
print("Pizze na kraju -", pizz3)

ivan_pizze = pizze[2:]
ivan_pizze.append('Margarita')
ivan_pizze.append('Calzone')

print("Moje najdraze pizze:")
for pizza in pizze:
    print("-", pizza)

print("Ivanove najdraze pizze:")
for pizza in ivan_pizze:
    print("-", pizza)
print("Volimo", len(pizze), " vrste pizze.")
print("Obozavamo pizze!")
