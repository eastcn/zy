"""
@east
@封装请求
"""

from Public.test_requests import req
reques=req()
class TestApi(object):
    def __init__(self,url,key,content,method):
        self.url=url
        self.key=key
        self.content=content
        self.method=method
    def testapi(self):
        if self.method=='POST':
            param = {'key':self.key,'info':self.content}
            response = reques.post(url=self.url,parms=param)
            return response
        elif self.method=='GET':
            param = {'key':self.key,'info':self.content}
            response = reques.get(url=self.url,parms=param)
            return response
    def getJson(self):
        json_data=self.testapi()
        return json_data

