fname = "romeo.txt"#input("Enter file name: ")
fh = open(fname)
lst = list(fh)
y=[]
wordc=[]
for line in lst:
    x = line.split()
    y = y + x

for word in y:
    if word not in wordc:
        wordc.append(word)
#    print(word)
wordc.sort()
print(wordc)
