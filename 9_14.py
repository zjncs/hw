#TUples
#the example of the chapter 1
# name=input('enter name')
# lyrics=open('9_14.txt','r', encoding='utf-8')
# counts=dict()
# for line in lyrics:
#     words=line.split()
#     for word in words:
#         counts[word]=counts.get(word,0)+1
# print(counts)
# bigcount=None
# bigword=None
# for word,count in counts.items():
#     if bigcount is None or count>bigcount:
#         bigword=word
#         bigcount=count
# print(bigword,bigcount)




name = "mbox-short.txt"
handle = open(name,'r',encoding='utf-8')
names=dict()
for line in handle:
    words=line.rstrip()
    pieces=words.split()
    
    if len(pieces)>1:
        piece=pieces[1]
        names[piece]=names.get(piece,0)+1
       
    else:
        continue


bigcount=None
bigword=None
for word,count in names.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)
    
    