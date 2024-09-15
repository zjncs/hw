#tuples
c={'a':10,'b':20,'c':30}
tmp=list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp)
tmp=sorted(tmp,reverse=True)
print(tmp)


name = "mbox-short.txt"
handle = open(name, 'r', encoding='utf-8')
counts=dict()
for line in handle:
    if line.startswith('From'):
        word=line.split()
        if len(word) >= 6:
            time=word[5]
            hour=time[:2]
            counts[hour]=counts.get(hour,0)+1
for k,v in sorted(counts.items()):
    print(k,v)