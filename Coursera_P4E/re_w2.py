#Python script for regular expressions
import re

# Configure Data inputs
f1 = "sum_42.txt"
f2 = "sum_1173766.txt"

print(" Wellcome to the regular expressions assigment!\n Sample or Actual data ?\n Enter '1' for Sample or '2' Actual data..")

ch = input(" Enter: " )
#Choosing what file to open or to quit
if ch == "1":
    handle=open(f1,"r")
elif ch == "2":
    handle=open(f2,"r")
else:
    print(" Not a valid input.\nExiting...")
    quit()

#opening the file , striping each line and finding all numbers, if there is a list loop through it and append as single variable to data
data = []
for line in handle:
    line = line.rstrip()
    t_data = re.findall("[0-9]+",line)
    if len(t_data) < 1: continue
    for numb in t_data:
        data.append(numb)
# adding the files in one variable
sum = 0
for num in data:
    sum = sum + int(num)
print(" Sum of numbers in the file:", sum)
