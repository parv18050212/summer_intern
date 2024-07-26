from flask import Flask


app = Flask(__name__)


@app.route("/sum")
def lwsum():
    x = 5+3
    return(str(x))

@app.route("/whatsapp")
def send_message():
    import pywhatkit
    pywhatkit.sendwhatmsg_instantly('+919410780293',"sale gaddar")
    return("message sent")

@app.route("/send_mail")
def send_mail():
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('parv23155@gmail.com','')
    server.sendmail('parv23155@gmail.com','parvagarwal73@gmail.com','message')

    return('mail sent')

@app.route('/schedule_mail')
def sch_mail():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import schedule
    import time
    def send_email():
       

        
        msg = MIMEMultipart()
        msg['From'] = 'parv23155@gmail.com'
        msg['To'] = 'parvagarwal73@gmail.com'
        msg['Subject'] = 'Scheduled Email'
        body = 'This email was sent at a scheduled time.'
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com',587)

        server.starttls()

        server.login('parv23155@gmail.com','')

        server.sendmail('parv23155@gmail.com','parvagarwal73@gmail.com', 'hello friend')

        server.quit()
        return("Successfully sent email message to %s:" % (msg['To']))
    schedule.every().day.at("21:47").do(send_email)
    while True:
        schedule.run_pending()
        time.sleep(1)

        
app.run(port=80,host='0.0.0.0')

