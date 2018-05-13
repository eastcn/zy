"""
@发送邮件
@east
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import yaml


def send_email():
    # 打开配置文件，读取用户名密码
    filepath=open(r'.\config\config.yaml',encoding='utf-8')
    file_config=yaml.load(filepath)
    sender=file_config['email_sender']
    receiver=file_config['email_receiver']
    password=file_config['my_password']
    # 设置邮件内容
    massage=MIMEText('test','plain','utf-8')
    massage['From']=Header('east','utf-8')
    massage['To']=Header('qq','utf-8')
    subject='BAOGAO'
    massage['Subject']=Header(subject,'utf-8')

    # 发送邮件
    try:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(sender, password)
        server.sendmail(sender,receiver,massage.as_string())
        server.quit()
    except smtplib.SMTPException:
        print('error')
