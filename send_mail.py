import smtplib
from email.mime.text import MIMEText
def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '53d42867b9cff2'
    password = '9ef3f0dbf3eb2f'
    message = f"<h3>New FeedBack Submission</h3><ul><li> customer: {customer}</li><li> dealer: {dealer}</li><li> rating: {rating}</li><li> comments: {comments}</li></ul>"

    sender_mail = 'email1@example.com'
    receiver_mail = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject']= 'Lexus Feedback'
    msg['From']= sender_mail
    msg['To']= receiver_mail

    #send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_mail,receiver_mail,msg.as_string())
