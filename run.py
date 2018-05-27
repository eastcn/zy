# encoding:utf-8
"""
@east
@"执行脚本"
"""
from  Public.creatreport_excel import create
import os, threading, datetime
from Public.get_excel import data_excel
from Public.testcase import test
from Public.savereport import save_result
from Public.create_html import createHtml
from Public.email import send_email
from Public.log import LOG

def start():
    # 读取时间
    starttime = datetime.datetime.now()

    # 设置开始时间
    m = datetime.datetime.now().strftime("%Y%m%d")

    # 打开地址
    basdir = os.path.abspath(os.path.dirname(__file__))

    # 读取测试数据
    listid, listname, listkey, listcontent, listurl, listmethod, listexpect = data_excel()

    #进行测试
    list_relust, list_fail, list_pass, list_json, list_exption, list_place = test(listid, listname, listkey, listcontent, listurl, listmethod, listexpect)

    # 创建测试报告地址
    filepath_excel = os.path.join(basdir + '\\test_Report\\%s-result.xls' % m)
    if os.path.exists(filepath_excel) is False:
        os.system(r'touch %s' % filepath_excel)
    filepath_html=os.path.join(basdir + '\\test_Report\\%s-result.html' % m)
    if os.path.exists(filepath_html) is False:
        os.system(r'touch %s' % filepath_html)

    # 保存测试报告
    save_result(starttime, len(list_relust), ((list_pass)), list_fail)

    #设置测试报告的样式
    create(filename=filepath_excel, list_fail=list_fail, list_pass=list_pass, list_json=list_json, listurls=listurl,
           listkeys=listkey, listcontent=listcontent, listmethods=listmethod, listexpects=listexpect,
           listids=listid, listresult=list_relust, listnames=listname)

    #创建HTML报告
    endtime=datetime.datetime.now()
    createHtml(titles='接口测试报告', filepath=filepath_html, starttime=starttime,
               endtime=endtime, passge=list_pass, fail=list_fail,
               id=listid, name=listname, key=listkey, coneent=listcontent, url=listurl, meth=listmethod,
               yuqi=listexpect, json=list_json, relusts=list_relust, weizhi=list_place, exceptions=list_exption)
    # 发送邮件
    #send_email(fp=filepath_excel)
    LOG.info('测试完成')

if __name__ == '__main__':
    start()
