"""
@发送邮件
@east
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from Public.log import LOG,logger
import datetime
import yaml


@logger('发送邮件')

def send_email(fp):
    #设置时间
    time=datetime.datetime.now().strftime("%Y%m%d")
    # 打开配置文件，读取用户名密码
    filepath=open(r'.\config\config.yaml',encoding='utf-8')
    file_config=yaml.load(filepath)
    sender=file_config['email_sender']
    receiver=file_config['email_receiver']
    password=file_config['my_password']
    # 设置邮件内容
    #构造一个发送邮件的合集
    massage=MIMEMultipart()
    #获取创建的excel文件
    result_filepath = fp

    #构建邮件的主题，发件人
    massage['From']=Header(u"eastapitest<%s>"%sender)
    massage['To']=Header(u"我<%s>"%receiver)
    subject='%s测试报告'%time
    massage['Subject']=Header(subject,'utf-8')

    #邮件正文
    msg=MIMEText('详细测试报告见附件1','plain','utf-8')
    massage.attach(msg)

    #构造附件
    attachment = MIMEApplication(open(result_filepath,'rb').read())
    #attachment["Content-Type"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    attachment.add_header('Content-Disposition', 'attachment',filename= '附件1.xls')
    massage.attach(attachment)

    # 发送邮件
    try:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(sender, password)
        server.sendmail(sender,receiver,massage.as_string())
        server.quit()
    except smtplib.SMTPException:
        LOG.info('发送邮件失败，原因：%s' % Exception)
