#DICTIONARIES
#next I will create a dictionary and print the times of the names
# count=dict()
# names=["John","Mary","David","John","David","Mary","John","Mary"]
# for name in names:
#     if name in count:
#         count[name]+=1
#     else:
#         count[name]=1
# print(count)
# x=count.get("Johnf",2)
# print(x)


#counting pattern
congts=dict()
print('enter a line of text:')
line=input('')
words=line.split()
print('words',words)
print('counting pattern')
for word in words:
    congts[word]=congts.get(word,0)+1
print(congts)