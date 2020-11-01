import smtplib 

smtp = smtplib.SMTP('smtp_server') 

try: 
    smtp.sendmail('rgonzalez10026@gmail.com', ['rgonzalez69@ucmerced.edu'], "This is a test e-mail message")
except SMTPException as exception: 
    print("Error: unable to send email:  " + exception) 
finally: 
    smtp.quit()
