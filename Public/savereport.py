from Public.log import LOG,logger
@logger('保存测试结果')
def save_result(testtime,toial,passnum,fail):
    try:
        f=open('result.txt','a')
        f.write("%s=%s=%s=%s \n"%(testtime,toial,passnum,fail))
        f.close()
    except:
        LOG.info('保存测试结果出错，原因：%s'%Exception)