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
		<link href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
		<style type="text/css">

			td{ 
				width:80px; 
			}
			
			.ellps {
				width:200px;
/*				text-overflow: ellipsis; //超出部分用....代替  
				overflow: hidden; //超出隐藏  
				border: 1px solid red;*/
				overflow: hidden;
				text-overflow: ellipsis;
				display: -webkit-box;
				-webkit-line-clamp: 4;
				-webkit-box-orient: vertical;
			}
			.modal-dialog {
			    width: 800px;
			}
			.table{
			width: 75%%;
			margin:0 auto;
			}
		</style>

		<script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
		<script src="https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
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
			       Exception: <strong >%s</strong> 
			       Unknown_Error : <strong >%s</strong></span></p>                  
			    <p ><strong>测试详情如下</strong></p>  </div> ''' % (
    starttime, endtime, (endtime - starttime), passge, fail, excepthions, weizhicuowu)
    return beijing


shanghai = '''
        <p>&nbsp;</p>
        <table class="table table-bordered" >
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
            <td class="warp">%s</td>
            <td>%s
           </td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
             <td>
            	<div class='ellps'>%s</div>
            	<a class="btn btn-link a_null">show</a>
            	</td>
            	%s
        </tr>

    ''' % (id, name, key, coneent, url, meth, yuqi, json, passfail(relust))
    return xiangqing


weibu = '''
	</table>
	<!-- 模态框（Modal） -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                <h4 class="modal-title" id="myModalLabel">实际返回</h4>
            </div>
            <div class="modal-body">在这里添加一些文本</div>
            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal -->
</div>
    </body>
    <script type="text/javascript">
    
    	function stringToNum(str, num) {
    		var len = Math.floor(str.length/num)
    		var res = ''
    		for(var i=0; i<num; i++){
    			res = res + str.substr(len*i,len) + '\\r\\n'
    		}
    		res = res + str.substring(len*num, str.length)
    		return res
    	}
    	var cxt = $(".warp");
    	for(var t=0;t<cxt.length;t++)
    	cxt.get(t).innerText = stringToNum(cxt.get(t).innerText,6)
    	//换行
    	
    	$('.a_null').click(function(){
    		var text = $(this).prev().text()
    		console.log(text)
    		$('.modal-body').text(text)
    		$('#myModal').modal('show')
    	})
    	//显示模态框
    	
    </script>
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