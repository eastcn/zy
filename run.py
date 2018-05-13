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
from Public.email import send_email


def start():
    starttime = datetime.datetime.now()
    m = datetime.datetime.now().strftime("%Y%m%d")
    basdir = os.path.abspath(os.path.dirname(__file__))
    listid, listkey, listcontent, listurl, listmethod, listexpect, listname = data_excel()
    list_relust, list_fail, list_pass, list_json, list_exption, list_place = test()
    filepath = os.path.join(basdir + '\\test_Report\\%s-result.xls' % m)
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)  # ?
    save_result(starttime, len(list_relust), ((list_pass)), list_fail)
    create(filename=filepath, list_fail=list_fail, list_pass=list_pass, list_json=list_json, listurls=listurl,
           listkeys=listkey, listcontent=listcontent, listmethods=listmethod, listexpects=listexpect,
           listids=listid, listresult=list_relust, listnames=listname)
    send_email()


if __name__ == '__main__':
    start()
