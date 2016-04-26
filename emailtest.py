import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def notificateMe(msgToSent):
    fromaddr = "ovenma.96@gmail.com"
    toaddr = "billgao0807@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "email test"

    body = msgToSent
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP()
    server.connect("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(fromaddr, "40bcef5551")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit
    return


# import smtplib
#
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login("billgao0807@gmail.com", "40bcef5551")
#
# msg = "YOUR MESSAGE!"
# server.sendmail("YOUR EMAIL ADDRESS", "THE EMAIL ADDRESS TO SEND TO", msg)
# server.quit()
