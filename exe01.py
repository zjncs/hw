# xfile=open('exe01.txt')
# for letter in xfile:
#     print(letter)
# 使用with语句来自动关闭文件
# with open('exe01.txt') as xfile:
#     for line in xfile:
#         print(line, end='')  # 使用end=''避免额外的换行
# import os

# # 列出当前目录中的所有文件和文件夹
# current_directory = os.getcwd()
# files_and_dirs = os.listdir(current_directory)

# if 'exe01.txt' in files_and_dirs:
#     print("文件 'exe01.txt' 存在于当前工作目录中。")
# else:
#     print("文件 'exe01.txt' 不存在于当前工作目录中。")
import os

# 更改当前工作目录
os.chdir('c:\\code\\code-py')

# 打开文件
try:
    with open('exe01.txt') as xfile:
        for line in xfile:
            print(line, end='')
except FileNotFoundError:
    print("文件 'exe01.txt' 不存在于指定路径中。")

