"""
@east
@断言
"""
from Public.log import LOG,logger
@logger('断言测试结果')
def assert_in(expects,result_json):
    if len(expects.split('='))>1:
        data=expects.split(',')
        result = dict([(item.split('=')) for item in data])
        value1=([(str(value)) for value in result.values()])
        value2=([(str(result_json[key])) for key in result.keys()])
        if value1==value2:
            return { "code":0, "result":'pass'}
        else:
            return {"code":1,"result":"fail"}
    else:
        LOG.info('请填写预期结果')
        return {"code":2,"result":"请填写预期结果"}

# @logger('断言测试结果')
# def asserter(expects):
#     if len(expects.split(','))>1:
#         data=expects.split(',')
#         result=dict([(item.split('=')) for item in data])
#         return result
#     else:
#         LOG.info('请填写预期结果')
#         raise {"code":2,"result":"请填写预期结果"}