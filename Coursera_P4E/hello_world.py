print("Hello world!")

def computepay(h,r):
    if h>40:
        pay = 40 * r + ((h-40) * r * 1.5)
    else:
        pay = h * r
    return pay

hrs = float(input("Enter Hours:"))
rat = float(input("Enter Rate:"))
p = computepay(hrs,rat)
print("Pay",p)
