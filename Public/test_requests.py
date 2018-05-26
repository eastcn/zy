"""
@east
@封装request
"""
import requests,json,ast
from Public.log import LOG,logger

@logger('requests封装')
def request(url, method, params,cookie):
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0"}
    params_dict=ast.literal_eval(params)
    cookie_dict=ast.literal_eval(cookie)
    if method == 'POST':
        response = requests.post(url=url,data=params_dict,headers=header,cookies=cookie_dict)
        status=response.status_code
        json_result=json.loads(response.text)
        return status,json_result
    elif method == 'GET':
        #LOG.info('%s'%isinstance(params,str))
        response = requests.get(url, params_dict,cookies=cookie_dict)
        status = response.status_code
        json_result = json.loads(response.text)
        return status,json_result
    else:
        status=0
        json_result={}
        return status,json_result
# class req(object):
#     def __init__(self):
#         self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0"}
#     def get(self,url,parms):   #get请求
#         try:
#             r=requests.get(url,params=parms,headers=self.headers)
#             return r
#             # r.encoding='UTF-8'
#             # status=r.status_code
#             #
#             # json_response=json.loads(r.text)
#             # return {'code':0,'result':json_response}
#         except Exception as e:
#             LOG.info('get请求出错，原因：%s'%e)
#             return {'code':1, 'result': 'get请求出错，出错原因:%s'%e}
#     def post(self, url, parms):#post消息
#         data = json.dumps(parms)
#         try:
#             r =requests.post(url,data=data,headers=self.headers)
#             json_response = json.loads(r.text)
#             return {'code':0, 'result': json_response}
#         except Exception as e:
#             LOG.info('post请求出错，出错原因:%s' % e)
#             return {'code':1, 'result': 'post请求出错，出错原因:%s' % e}
#


    # def delfile(self,url,parms):#删除的请求
    #     try:
    #         del_word=requests.delete(url,params=parms,headers=self.headers)
    #         json_response=json.loads(del_word.text)
    #         return {'code':0, 'result': json_response}
    #     except Exception as e:
    #         LOG.info('del请求出错，出错原因:%s' % e)
    #         return {'code': 1, 'result': 'del请求出错，出错原因:%s' % e}
    # def putfile(self,url,parms):#put请求
    #     try:
    #         data=json.dumps(parms)
    #         me=requests.put(url,data)
    #         json_response=json.loads(me.text)
    #         return {'code': 0, 'result': json_response}
    #     except Exception as e:
    #         LOG.info('put请求出错，出错原因:%s' % e)
    #         return {'code': 1, 'result': 'put请求出错，出错原因:%s' % e}


