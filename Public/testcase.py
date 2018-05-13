"""
@east
@测试过程
"""
from Public.get_excel import data_excel
from Public.log import LOG,logger
# from Public.test_Fz import TestApi
from Public.test_requests import requests as req
import json
from Public.asserter import assert_in
listid,listname,listkey,listcontent,listurl,listmethod,listexpect=data_excel()

@logger('测试')
def test():
    list_pass = 0
    list_fail = 0
    list_json = []
    list_relust=[]
    list_place=0
    list_exption=0
    for i in range(len(listurl)):
        status,result_json=req(url=listurl[i],method=listmethod[i],params=listcontent[i])
        # status=res.status_code
        # result_json=json.load(res.text)
        LOG.info('输入> 参数:%s, url:%s ,返回:%s,预期:%s' % (listcontent[i], listurl[i],status , listexpect[i]))
        if status == 200:
            assert_result = assert_in(expects=listexpect[i], result_json=result_json)
            if assert_result['code']==0:
                list_json.append(result_json)
                list_relust.append('pass')
                list_pass+=1
            elif assert_result['code']==1:
                list_json.append(result_json)
                list_relust.append('fail')
                list_fail += 1

            elif assert_result['code'] == 2:
                list_exption += 1
                list_relust.append('exception')
                list_json.append(assert_result['result'])
            else:
                list_place+=1
                list_relust.append('未知错误')
                list_json.append('未知错误')
        else:
            list_json.append(result_json)
            list_relust.append('fail')
            list_fail += 1
    return list_relust, list_fail, list_pass, list_json, list_exption, list_place


        # api=TestApi(url=listurl[i],key=listkey[i],content=listcontent[i],method=listmethod[i])
        # apijson=api.getJson()

    #     if apijson['code']==0:  #测试结果记录
    #         LOG.info('inputdata> 参数:%s, url:%s ,返回:%s,预期:%s' % (listcontent[i], listurl[i], apijson, listexpect[i]))
    #         assert_re = assert_in(asserExcept=listexpect[i], responceJson=apijson)
    #         if assert_re['code'] ==0:
    #             list_json.append(apijson['result'])
    #             list_relust.append('pass')
    #             list_pass+=1
    #         elif assert_re['code']==1:
    #             list_fail+=1
    #             list_relust.append('fail')
    #             list_json.append(apijson['result'])
    #         elif assert_re['code'] == 2:
    #             list_exption += 1
    #             list_relust.append('exception')
    #             list_json.append(assert_re['result'])
    #         else:
    #             list_place+=1
    #             list_relust.append('未知错误')
    #             list_json.append('未知错误')
    #     else:
    #         list_exption += 1
    #         list_relust.append('exception')
    #         list_json.append(apijson['result'])
    #         continue
    # return  list_relust,list_fail,list_pass,list_json,list_exption,list_place