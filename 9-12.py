# stuff=list()
# stuff.append("apple")
# stuff.append("banana")
# stuff.append("cherry")
# print(stuff)

# some=[1,2,3,4,5]
# 3 in some # True


# friends=["Alice","Bob","Charlie"]
# print(friends[1])
# #sort the list in alphabetical order

# #some functions to get the average    this onli needs two values and room
# total=0
# count=0
# while True:
#     inp=input("Enter a number (or 'done' to stop): ")
#     if inp=="done":
#         break
#     value=float(inp)
#     total+=value
#     count+=1
# average=total/count
# print("The average is:",average)

# #the second way to get the average   this needs a list of numbers
# numlist=list()
# while True:
#     inp=input("Enter a number (or 'done' to stop): ")
#     if inp=="done":
#         break
#     value=float(inp)
#     numlist.append(value)
# average=sum(numlist)/len(numlist)
# print("The average is:",average)



#how strings work with list
# abc='with three words'
# stuff=abc.split()#split the string into a list of words
# print(stuff)# the mumber of the lists are read by lines 


# fhand=open('test1.txt')
# # for line in fhand:
# #     print(line.rstrip())
# #     if not line.startswith('From '):
# #         continue
# #     words=line.split()
# #     print(words[3])

# #double split
# for line in fhand:
#     words=line.split()#words is a string
#     pieces=words[1].split('i')#pieces 
#     print(pieces)



# fh = open(r'C:\code\code-py\hw\romeo.txt')
# lst=list()
# lsto=str()
# for line in fh:
#     line=line.rstrip()
#     lsto=lsto+line+' '
# lst=lsto.split()
# lst.sort()
# print(lst)
    



# for line in fand:
#     line=line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     words=line.split()
#     print(words[1])
# import chardet

# # 读取文件内容并检测编码
# with open(r'C:\code\code-py\hw\romeo.txt', 'rb') as f:
#     raw_data = f.read()
#     result = chardet.detect(raw_data)
#     encoding = result['encoding']

# # 使用检测到的编码方式打开文件
# fand = open(r'C:\code\code-py\hw\romeo.txt', encoding=encoding)
# data=open(r'C:\code\code-py\hw\mbox-short.txt',encoding='utf-8')

# for line in data:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     words = line.split()
#     print(words[1])
