import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime 
import time
import calendar

now = datetime.datetime.now()
today_date=datetime.date.today() #today's date
cy = now.year #current year
cm = now.month #current month
cd = now.day #current day
endday_of_month = calendar.monthrange(cy,cm)[1] 

MY_ADDRESS = 'divyanshuanand97@gmail.com'
PASSWORD = '***********'

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('C:/Users/divyanshu.a/Desktop/mycontacts.txt') # read contacts
    message_template = read_template('C:/Users/divyanshu.a/Desktop/message.txt') # read messages

    # set up the SMTP server
    s = smtplib.SMTP(host='czipop.logix.in', port = 587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    
    if cd in [7,15,22,endday_of_month] :

        # For each contact, send the email:
        for name, email in zip(names, emails):
            msg = MIMEMultipart()       # create a message
    
            # add in the actual person name to the message template
            message = message_template.substitute()
    
            # Prints out the message body for our sake
            print(message)
    
            # setup the parameters of the message 
            msg['From']=MY_ADDRESS
            msg['To']=email
            msg['Subject']="ANM - Transactions with Odd Patterns"
            
            # add in the message body 
            msg.attach(MIMEText(message, 'plain'))
            
            # send the message via the server set up earlier.
            s.send_message(msg)
            del msg
            
        # Terminate the SMTP session and close the connection
        s.quit()
    
    
if __name__ == '__main__':
    main()