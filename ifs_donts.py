#The if's and dont's and else's of Python

# Logical Operators
"""
== - Equal
!= - Not Equal
<  - Less than
>  - More than
<= - Less or equal to
>= - More or equal to
in - if the value is in list
"""

age = 12

if age < 5:
    price = 0
elif age < 18:
    price = 25
elif age >= 55:
    price = 10
else:
    price = 40

print("Price for admission is £{}".format(price))
