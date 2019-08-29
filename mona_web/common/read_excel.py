#coding utf-8
import xlrd

class ExcelRead():
    def __init__(self, excelpath, sheetname="Sheet1"):
        #获取excel文件路径
        self.data = xlrd.open_workbook(excelpath)
        #读取sheet
        self.table = self.data.sheet_by_name(sheetname)
        #获取table的第一行为主键
        self.keys = self.table.row_values(0)
        #获取总行数
        self.rownum = self.table.nrows
        #获取总列数
        self.colnum = self.table.ncols

    def dict_data(self):
        if self.rownum <= 1:
            print("行业总数小于等于1")
        else:
            r = []
            j = 1
            for i in range(self.rownum-1):
                s={}
                #从第二行取values的值
                values = self.table.row_values(j)
                for x in range(self.colnum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
            return r

if __name__ == "__main__":
    filepath = "C:\\Users\\LMN\\PycharmProjects\\Web_Auto\\common\\datas.xlsx"
    data = ExcelRead(filepath)
    result = data.dict_data()
    print(result)
