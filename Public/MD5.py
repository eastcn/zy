"""
@east
@md5转格式
"""
import hashlib

#转成MD5格式
def set_md5(str):
    h1=hashlib.md5()#给予一个md5对象
    h1.update(str.encode(encoding='utf-8'))
    str_md5=h1.hexdigest()
    return str_md5
