#正则表达式
#^ 表示行的开头
#$ 表示行的结尾
#\d 表示匹配数字
#\D 表示匹配非数字
#\w 表示匹配字母、数字、下划线
#\W 表示匹配非字母、数字、下划线
#\s 表示匹配空白字符
#\S 表示匹配非空白字符
#[] 表示匹配括号中的任意一个字符
#[^] 表示匹配不在括号中的任意一个字符
#* 表示匹配前面的字符零次或多次
#+ 表示匹配前面的字符一次或多次
#? 表示匹配前面的字符零次或一次
#{n} 表示匹配前面的字符恰好 n 次
#{n,} 表示匹配前面的字符至少 n 次
#{n,m} 表示匹配前面的字符至少 n 次，至多 m 次
#| 表示或
#() 表示分组
hand=open('mbox-short.txt',encoding='utf-8')
for line in hand:
    line=line.rstrip()
    if line.find('From:')>=0:
        print(line)
import re
hand=open('mbox-short.txt',encoding='utf-8')
#for line in hand:
 #   line=line.rstrip()
  #  if re.search('From:',line):
    #    print(line)
#^x.*y$ 表示匹配以 x 开头，以 y 结尾的字符串
#^x.-\S非空白+大于等于一
#?表示匹配前面的字符零次或一次 nongreedy模式
#\S+@\S+
#^from(\S+@\S+)表示匹配以from开头，后面跟着至少一个非空白字符，再跟着@，再跟着至少一个非空白字符，最后以空白字符结尾

numlist = list()
for line in hand:
    line=line.rstrip()
    stuff=re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff)>0:
        numlist.append(float(stuff[0]))
print(numlist)