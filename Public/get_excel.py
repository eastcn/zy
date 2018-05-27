"""
@east
@"获取测试用例"
"""
import xlrd
from Public.log import LOG,logger
@logger('获取excel测试用例')
def data_excel():
    try:
        filepath='.\\Case\\case1.xlsx'#打开地址
        file=xlrd.open_workbook(filepath)
        sheet=file.sheets()[0]

        #增加sheet2
        sheet_2=file.sheets()[1]
        nrows_2=sheet_2.nrows

        nrows=sheet.nrows #读取excel行中数据
        listid=[]#建立数据list
        listname = []
        listkey=[]
        listcontent=[]
        listurl=[]
        listmethod=[]
        #listresult=[]
        listexpect=[]
        for i in range(1,nrows):#添加数据
            listid.append(sheet.cell(i,0).value)
            listname.append(sheet.cell(i,1).value)
            listkey.append(sheet.cell(i,2).value)
            listcontent.append(sheet.cell(i,3).value)
            listurl.append(sheet.cell(i,4).value)
            listmethod.append(sheet.cell(i,5).value)
            listexpect.append(sheet.cell(i,6).value)

        for t in range(1,nrows_2):#添加sheet2
            listid.append(sheet_2.cell(t, 0).value)
            listname.append(sheet_2.cell(t, 1).value)
            listkey.append(sheet_2.cell(t, 2).value)
            listcontent.append(sheet_2.cell(t, 3).value)
            listurl.append(sheet_2.cell(t, 4).value)
            listmethod.append(sheet_2.cell(t, 5).value)
            listexpect.append(sheet_2.cell(t, 6).value)

        return listid,listname,listkey,listcontent,listurl,listmethod,listexpect
    except:LOG.info('打开测试用例失败，原因是%s'%Exception)






