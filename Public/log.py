"""
@east
@"日志"
"""
import os
import logbook
from logbook.more import ColorizedStderrHandler
from functools import wraps

check_path='.'
Log_Dir=os.path.join(check_path,'Log')
file_stream=False
if not os.path.exists(Log_Dir):
    os.makedirs(Log_Dir)
    os.stream=True

def get_logger(name='api',file_log=file_stream,level=''):
    logbook.set_datetime_format('local')
    ColorizedStderrHandler(bubble=False,level=level).push_thread()
    logbook.TimedRotatingFileHandler(
        os.path.join(Log_Dir,'%s.log'%name),
        date_format='%Y-%m-%dH',bubble=True,encoding='utf-8').push_thread()
    return logbook.Logger(name)
LOG=get_logger(file_log=file_stream,level='INFO')

def logger(param):
    def wrap(function):
        @wraps(function)
        def _wrap(*args,**kwargs):
            LOG.info("当前模块为{}".format(param))
            LOG.info("当前模块获取参数信息,{}".format(str(args)))
            LOG.info("当前模块参数信息,{}".format(str(kwargs)))
            return function(*args,**kwargs)
        return _wrap
    return wrap