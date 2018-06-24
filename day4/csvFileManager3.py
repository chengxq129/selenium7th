import csv
#每个测试用例对应着不同的csv文件
#每条测试用例都会打开一个csv文件，所有每次也应该关闭该文件

class CsvFileManager3:
    @classmethod
    def read(self):
        path = r'C:\Users\51Testing\PycharmProjects\selenium7th\data\test_data.csv'
        file = open(path,'r')
        try:#try尝试执行以下代码
            #通过csv代码库读取打开的csv文件，获取到文件中的数据集
            data_table = csv.reader(file)
            #for循环，item每一行，in在数据集中，data_table表示数据集
            #data_table中有几行数据，我们就会执行几次
            a = [1,2,3,4,5]
            a[6]   #这时数组可能发生数据下标越界
            #如何保证无论程序执行过程中是否报错，都能正常关闭已打开的文件
            for item in data_table:
                print(item)

        finally:#finally最终，不论过程是否报错，都会执行以下代码
            # 方法最后应该添加close方法

            file.close()
            print("file.close() method is executed")

#如果想测试一下这个方法
if __name__ == '__main__':
    #csvr = CsvFileManager2
    #csv.read()
    #如果在方法前面加上classmethod，表示这个方法可以直接用类调用
    #如果在方法上写了一个classmethod，就不需要先实例化对象后才能调用
    CsvFileManager3.read()