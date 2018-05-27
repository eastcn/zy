"""
@east
@生成excel测试报告
"""
import xlwt,yaml
from xlwt import *
from Public.log import LOG,logger
from Public.MD5 import set_md5

def style1(): #微软雅黑，文字居中，400高度,加粗
    sty1=XFStyle()
    fnt=Font()
    fnt.name=u'微软雅黑'
    fnt.bold=True
    sty1.font=fnt
    alig=xlwt.Alignment()
    alig.horz=xlwt.Alignment.HORZ_CENTER
    alig.vert=xlwt.Alignment.VERT_CENTER
    sty1.alignment=alig   #给样式添加文字居中
    sty1.font.height=400 #文字高度
    return sty1
def style2():#文字居中，300高度
    sty2=XFStyle()
    alig2=xlwt.Alignment()
    alig2.horz = xlwt.Alignment.HORZ_CENTER
    alig2.vert = xlwt.Alignment.VERT_CENTER
    sty2.alignment=alig2
    sty2.font.height=300
    return sty2
def style3():#文字不居中，300高度
    sty3=XFStyle()
    sty3.font.height=300
    return  sty3
def style4(m):#测试结果的样式设置
    if m=="pass":
        sty4=style1()
        Pattern=xlwt.Pattern()
        Pattern.pattern=xlwt.Pattern.SOLID_PATTERN
        Pattern.pattern_fore_colour=xlwt.Style.colour_map['green']
        sty4.pattern=Pattern
    else:
        sty4=style2()
        Pattern=xlwt.Pattern()
        Pattern.pattern=xlwt.Pattern.SOLID_PATTERN
        Pattern.pattern_fore_colour=xlwt.Style.colour_map['red']
        sty4.pattern=Pattern
    return sty4
def style5():#文字不居中，300高度,红色
    sty5 = XFStyle()
    sty5.font.height = 300
    sty5.font.colour_index=2
    return sty5
def style6():#文字不居中，300高度,绿色
    sty6 = XFStyle()
    sty6.font.height = 300
    sty6.font.colour_index=3
    return sty6



def create(filename,list_pass,list_fail,listids,listnames,listkeys,listcontent,listurls,listmethods,listexpects,list_json,listresult):
    LOG.info('创建EXCEL报告')
    filepath=open(r'.\config\config.yaml',encoding='utf-8')
    file_config=yaml.load(filepath)
    file=Workbook(filename)
    table=file.add_sheet('测试报告',cell_overwrite_ok=True)
    #sheet2
    table2=file.add_sheet('测试一下sheet2')
    table2.write_merge(0,0,0,8,'测试报告')

    #参数md5转换
    md5_params=[]
    for m in range(0,len(listcontent)):
        md5_params.append(set_md5(listcontent[m]))

    style_1=style1()
    for i in  range(0,8):
        table.col(i).width=380*20
    style_2=style2()
    table.write_merge(0,0,0,8,'测试报告',style=style_1)
    table.write_merge(1,2,0,8,'测试概述',style=style_2)
    table.write(3,0,'项目名称',style=style_2)
    table.write(3,1,(file_config['projectname']),style=style_2)
    table.write(3, 2, '测试人', style=style_2)
    table.write(3,3,(file_config['test_person']),style=style_2)
    table.write(3,4,'通过',style=style_2)
    table.write(3,5, list_pass, style=style_2)
    table.write(4,0,'测试时间',style=style_2)
    table.write(4,1, (file_config['test_time']), style=style_2)
    table.write(4,2,'提测时间',style=style_2)
    table.write(4,3, (file_config['gettest_time']), style=style_2)
    table.write(4,4, '失败', style=style_2)
    table.write(4,5, list_fail, style=style_2)
    table.write_merge(5,5,0,8,'测试详情',style=style_2)
    table.write(6,0,'用例ID',style=style3())
    table.write(6,1,'用例名字',style=style3())
    table.write(6,2, 'key', style=style3())
    table.write(6, 3, '参数', style=style3())
    table.write(6,4,'url',style=style3())
    table.write(6, 5, '请求方式', style=style3())
    table.write(6, 6, '预期结果', style=style3())
    table.write(6,7, '实际结果', style=style3())
    table.write(6, 8, '最终结果', style=style3())
    for i in range(len(listids)):
        table.write(i+7,0,listids[i],style=style3())
        table.write(i+7,1,listnames[i],style=style3())
        table.write(i+7,2,listkeys[i],style=style3())
        table.write(i+7,3,md5_params[i],style=style3())
        table.write(i+7,4,listurls[i],style=style3())
        table.write(i+7,5,listmethods[i],style=style3())
        table.write(i+7,6,listexpects[i],style=style3())
        table.write(i+7,7,str(list_json[i]),style=style3())
        if listresult[i]=='fail':
            table.write(i+7,8,listresult[i],style=style5())
        else:
            table.write(i+7,8,listresult[i],style=style6())
    file.save(filename)








