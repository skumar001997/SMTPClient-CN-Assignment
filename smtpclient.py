import sys
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

arguments = sys.argv
length_argument = len(arguments)
to_email = []
filenames = []
message = str()

for i in range(1,(length_argument)):
    if(arguments[i]=='-f'):
        i+=1
        from_email = arguments[i]
    elif(arguments[i] == '-d'):
        while (arguments[i] != '-i' and arguments[i+1] != '-i' ):
            i+=1
            to_email.append(arguments[i])
    elif(arguments[i] == '-i'):
        while (arguments[i] != '-s' and arguments[i+1] != '-s'):
            i+=1
            filenames.append(arguments[i])            
    elif(arguments[i]== '-s'):
        i+=1
        server_ip = arguments[i]

print("Please enter your password to authenticate")
password = input()

smtp = smtplib.SMTP(server_ip,587)
smtp.starttls()
smtp.login(from_email,password)

msg = MIMEMultipart()

for file in filenames:
    file_content = open(file,'r')
    message+='\n'
    message+= file_content.read()


msg['From'] = from_email
msg['To'] = ', '.join(to_email)
msg['Subject'] =', '.join(filenames)
msg.attach(MIMEText(message,'plain'))

try:
    smtp.sendmail(from_email,to_email[0],msg.as_string())
    print("Email Sent Successfully")
except SMTPException:
    print(SMTPException)
del msg
smtp.quit()
