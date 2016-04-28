import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def notificateMe(msgToSent = "no massage passed in"):
# def notificateMe():
    fromaddr = "ovenma.96@gmail.com"
    toaddr = "billgao0807@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "From Hat's Python script: "

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

def main():
    notificateMe()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
