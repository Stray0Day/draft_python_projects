import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

# Email details
sender = '=?US-ASCII?Q?Keith_Moore?= @stray0.day'
receiver = 'dawid.sturgulewski@point72.com (=?iso-8859-8?b?7eXs+SDv4SDp7Oj08A==?=)'
subject = 'Test email'
message = 'This is a test spoof sent using Python'
return_path = '=?US-ASCII?Q?WhataRascal?= dawid.sturgulewski@point72.com'
cc = '(=?iso-8859-8?b?7eXs+SDv4SDp7Oj08A==?=) <dawid.sturgulewski@point72.com>'
subject = "=?ISO-8859-1?Q?Olle_J=E4rnefors?="



# SMTP server details
smtp_server = 'mail.smtp2go.com'
smtp_port = 2525
smtp_username = 'stray0.day'
smtp_password = 'ZkDJEBJgPGOV28hx'

# Create a message object
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Cc'] = cc
msg['Subject'] = subject
msg['Return-Path'] = return_path
msg['Reply-To'] = sender
msg['Message-ID'] = '<1234567890@example.com>'
msg['Date'] = formatdate(localtime=True)
msg['MIME-Version'] = '1.0'
msg.attach(MIMEText(message, 'plain'))

# Connect to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

# Login to the SMTP server
server.login(smtp_username, smtp_password)

# Send the email
recipients = [receiver, cc]
server.sendmail(sender, recipients, msg.as_string())

# Close the SMTP server connection
server.quit()
