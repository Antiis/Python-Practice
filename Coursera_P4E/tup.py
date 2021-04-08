name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counter=dict()
for line in handle:
	words=line.split()
	if line.startswith("From") and len(words) > 3 :
		tmp=words[5]
		tmp=tmp[:2]
		#if tmp not in counter:
		counter[tmp] = counter.get(tmp,0) + 1
		#else:
		#	counter[tmp] = counter[tmp]+1
#print(counter)
tup=sorted(counter.items())
for k,v in tup:
    print(k,v)
    
