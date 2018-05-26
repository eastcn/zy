"""

"""
import os
from Public.log import LOG,logger

titles = '接口测试'

def title(titles):
    title = '''<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>%s</title>
		<style type="text/css">
			td{ width:40px; height:50px;}
		</style>
	</head>
	<body>
	''' % (titles)
    return title


connent = '''
<div style='width: 1170px;margin-left: 15%'>
<h1>接口测试的结果</h1>'''


def shouye(starttime, endtime, passge, fail, excepthions, weizhicuowu):
    beijing = '''
		<p><strong>开始时间:</strong> %s</p>
		<p><strong>结束时间:</strong> %s</p>
		<p><strong>耗时:</strong> %s</p>
		<p><strong>结果:</strong>
			<span >Pass: <strong >%s</strong>
			Fail: <strong >%s</strong>
			       exception: <strong >%s</strong> 
			       weizhicuowu : <strong >%s</strong></span></p>                  
			    <p ><strong>测试详情如下</strong></p>  </div> ''' % (
    starttime, endtime, (endtime - starttime), passge, fail, excepthions, weizhicuowu)
    return beijing


shanghai = '''
        <p>&nbsp;</p>
        <table border='2'cellspacing='1' cellpadding='1' width='1100'align="center" >
		<tr >
            <td ><strong>用例ID&nbsp;</strong></td>
            <td><strong>用例名字</strong></td>
            <td><strong>key</strong></td>
            <td><strong>请求内容</strong></td>
            <td><strong>url</strong></td>
            <td><strong>请求方式</strong></td>
            <td><strong>预期</strong></td>
            <td><strong>实际返回</strong></td>  
            <td><strong>结果</strong></td>
            <td><button>anniu</button></td>
        </tr>
    '''


def passfail(tend):
    if tend == 'pass':
        htl = ' <td bgcolor="green">pass</td>'
    elif tend == 'fail':
        htl = ' <td bgcolor="fail">fail</td>'
    elif tend == 'weizhi':
        htl = '<td bgcolor="red">error</td>'
    else:
        htl = '<td bgcolor="#9300">error</td>'
    return htl


def ceshixiangqing(id, name, key, coneent, url, meth, yuqi, json, relust):
    xiangqing = '''
        <tr width='100'>
            <td>%s</td>
            <td>%s</td>

            <td>%s</td>
            <td>%s
           </td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            %s
        </tr>

    ''' % (id, name, key, coneent, url, meth, yuqi, json, passfail(relust))
    return xiangqing


weibu = '''
	</table>
    </body>
    </html>'''


def relust(titles, starttime, endtime, passge, fail, id, name, key, coneent, url, meth, yuqi, json, relust, exceptions,
           weizhi):
    if type(name) == list:
        relus = ' '
        for i in range(len(name)):
            relus+=(ceshixiangqing(id[i],name[i],key[i],coneent[i],url[i],meth[i],yuqi[i],json[i],relust[i]))
        text = title(titles) + connent + shouye(starttime, endtime, passge, fail, exceptions,
                                                weizhi) + shanghai + relus + weibu
    else:
        text = title(titles) + connent + shouye(starttime, endtime, passge, fail, exceptions,
                                                weizhi) + shanghai + ceshixiangqing(id, name, key, coneent, url, meth,
                                                                                    yuqi, json, relust) + weibu
    return text

def createHtml(filepath, titles, starttime, endtime, passge, fail, id, name, key, coneent, url, meth, yuqi, json,
               relusts, exceptions, weizhi):
    LOG.info('创建HTML报告')
    texts = relust(titles, starttime, endtime, passge, fail, id, name, key, coneent, url, meth, yuqi, json, relusts,
                   exceptions, weizhi)
    with open(filepath, 'wb') as f:
        f.write(texts.encode())