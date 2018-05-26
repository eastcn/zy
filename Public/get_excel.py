"""
@east
@"获取测试用例"
"""
import xlrd
from Public.log import LOG,logger
@logger('获取excel测试用例')
def data_excel():
    try:
        filepath='.\\Case\\case1.xlsx'
        file=xlrd.open_workbook(filepath)
        sheet=file.sheets()[0]
        nrows=sheet.nrows
        listid=[]
        listname = []
        listkey=[]
        listcontent=[]
        listurl=[]
        listmethod=[]
        #listresult=[]
        listexpect=[]
        for i in range(1,nrows):
            listid.append(sheet.cell(i,0).value)
            listname.append(sheet.cell(i,1).value)
            listkey.append(sheet.cell(i,2).value)
            listcontent.append(sheet.cell(i,3).value)
            listurl.append(sheet.cell(i,4).value)
            listmethod.append(sheet.cell(i,5).value)
            listexpect.append(sheet.cell(i,6).value)
        return listid,listname,listkey,listcontent,listurl,listmethod,listexpect
    except:LOG.info('打开测试用例失败，原因是%s'%Exception)





