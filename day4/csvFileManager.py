#1.要想读取csv文件，首先要导入csv代码库
#这个csv也不用下载，是python内置的代码库
#如果要读取excel需要下载相应的代码库：xlrd
#怎么下载：1）通过命令下载：在dos窗口中：输入pip install -U xlrd
#selenium也可通过命令下载：pip install -U selenium或者pip3 install selenium
#-U是升级到最新版的意思，pip是python语言最常用的项目管理工具，和java中的maven类似
#如果你安装了两个版本：python2和python3，那么可能需要把pip改成pip3
#       2）点击file--点击settings--点击project下面的interpreter--点击+，搜索需要的代码库，并可直接安装
import csv

#2.指定要读取的文件的路径
#1)每一个反斜线前面加一个反斜线
#path = 'C:\\Users\\51Testing\\PycharmProjects\\selenium7th\\data\\test_data.csv'
#2)把每一个反斜线都改成正斜线
#path = 'C:/Users/51Testing/PycharmProjects/selenium7th/data/test_data.csv'
#打印报错：因为字符串中包含转义字符\t等
#相比，第二种方法更好一点，因为java，python都是跨平台语言
#在Windows操作系统中，用反斜线\表示目录结构
#但是在Linux操作系统中，只有正斜线/表示目录结构
#如果用双反斜线，那么代码失去了跨平台的能力，linux用不了
#如果用正斜线，代码可同时在linux和Windows用
#3)如果在字符串外面加上r，则认为中间所有代码不存在转义字符
path = r'C:\Users\51Testing\PycharmProjects\selenium7th\data\test_data.csv'
#print(path)
#3.打开路径所对应的文件,默认为只读模式
file = open(path,'r')
#4.读取文件的内容，通过什么来读取？
#reader()方法是专门用来读取文件的
data_table = csv.reader(file)

#5.打印data_table中的每一行数据，怎么办？循环for-each语句
#for是循环关键字，item代表每一行，每循环一次，item就代表最新的一行数据，data_table表示整个文件中的所有数据
for item in data_table:
    print(item)
#
#很多的测试用例可能都需要从excel中读取数据，所以我们应该对这些代码做一个简单的封装，建一个文件叫csvFileManager2，把以上代码封装到一个方法中，并且再建一个文件来读取封装好的方法