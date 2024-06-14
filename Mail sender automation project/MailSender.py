import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from sys import *

    
def MailSender(filename,time,cnt,delcnt):
    print("Starting time of %s"%time)
    try:
        fromaddr="pratikshashedage1995@gmail.com"
        toaddr=argv[2]

        msg=MIMEMultipart()


        msg['From']=fromaddr
        msg['To']=toaddr

        body="""
        Hello %s,
        
        Please find attached document which contains Log of Duplicate files.
        Starting time of scanning: %s
        Total scanned files are :%d
        Total number of duplicate files found are :%d
        This is auto generated mail.

        Thanks & Regards,
        Pratiksha Hake
        """%(toaddr,time,cnt,delcnt)

        subject="""
        Process log generated at :%s
        """%(time)

        msg['Subject']=subject
        msg.attach(MIMEText(body,'plain'))

        attachment=open(filename,"rb")
        p=MIMEBase('application','txt',Name=filename)

        p.set_payload((attachment).read())
        encoders.encode_base64(p)

        p.add_header('Content-Disposition',"attachment filename=%s" %filename)

        msg.attach(p)

        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()

        s.login(fromaddr,"gmwf lmhy wamx ismd")
        text=msg.as_string()
        s.sendmail(fromaddr,toaddr,text)
        s.quit()

        print("Log file successfully sent through Mail")

    except Exception as E:
        print("Unable to send mail due to",E)
