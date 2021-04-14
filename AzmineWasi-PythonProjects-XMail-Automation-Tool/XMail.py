import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

#mail body
mail_content = '''

'''
#The mail addresses and password
sender_address = ''
sender_pass = ''

form = pd.read_excel("data.xlsx")
mail_list = form['Mail'].to_list()
name_list = form['Name'].to_list()

total = len(name_list)
i=0
print("Total Sending :",total)
while (i<total):

	receiver_address = mail_list[i]
	receiver_name = name_list[i]
	receiver_header=mail_list[i].replace(".","_")
	print("Initializing... ",receiver_address)
	mail_content= mail_content.format(name=receiver_name)
	#Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['Subject'] = ''
	#The subject line
	#The body and the attachments for the mail
	message.attach(MIMEText(mail_content, 'html'))
	attach_file_name = receiver_header+".png"
	print("Attachment name :",attach_file_name)
	with open(attach_file_name, 'rb') as fp:
	    img = MIMEImage(fp.read())
	    img.add_header('Content-Disposition', 'attachment', filename=attach_file_name)
	    message.attach(img)
	#Create SMTP session for sending the mail
	session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	session.starttls() #enable security
	session.login(sender_address, sender_pass) #login with mail_id and password
	text = message.as_string()
	session.sendmail(sender_address, receiver_address, text)
	session.quit()
	print('Mail Sent')
	i=i+1