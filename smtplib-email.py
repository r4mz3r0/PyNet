import smtplib 

from_address = "rgonzalez10026@gmail.com" 
to_address = "rgonzalez69@ucmerced.edu"
message = "Message" 

from email.mime.text import MIMEText 

mime_message = MIMEText(message, "plain") 
mime_message["From"] = from_address 
mime_message["To"] = to_address 
mime_message["Subject"] = "Subject" 

mime_message = MIMEText(message, "plain", _charset="utf-8") 
message = "<em>Hello</em>, <strong>python</strong>!" 
