import requests
import pandas as pd
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_email(email_body,next_chapter,recipients):
    password = 'password'
    sender = "email@gmail.com"
    server = 'smtp.gmail.com:587'
    message = MIMEMultipart("alternative", None, [MIMEText(email_body, 'html')])
    message['Subject'] = 'One Piece [Chapter %s] is out' % next_chapter
    message['From'] = sender
    message['To'] = ", ".join(recipients)
    server = smtplib.SMTP(server)
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipients, message.as_string())
    print("Email Sent.")
    server.quit()


if __name__ == "__main__":
    try:
        print("START")
        # start simple http session request ##
        session = requests.session()
        session.headers.update({'user-agent': 'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/83.0.4103.116 safari/537.36'})
        op_list = session.get('https://w16.read-onepiece.com/')

        ## cleaning to read chapter title only ##
        op_df = pd.DataFrame(op_list.text.split('\n'))
        op_df = op_df[op_df[0].str.contains('a href')]
        op_df = op_df[op_df[0].str.contains('chapter')]

        ## read database to know the latest and next chapter ##
        file = r"C:\Users\ZHENHUI\Desktop\Scripts\onepiece_crawler\OnepieceDatabase.txt"
        database = open(file,"r") 
        last_chapter = database.read()
        next_chapter = str(int(last_chapter) + 1)
        database.close()

        ## find next chapter ##
        result = op_df[op_df[0].str.contains(next_chapter)]
        if len(result) == 0:
            print("no new chapter. program ended.")
        else:
            print("new chapter found.")

            ## extract new chapter links
            email_body = ""
            for item in result.values.tolist():
                email_body = email_body + item[0]
            recipients = ['email1@gmail.com', 'email2@gmail.com', 'email3@hotmail.com']
            send_email(email_body,next_chapter,recipients)

            # update database with new chapter
            with open(file, 'w') as database:
                database.writelines( next_chapter )
                database.close()
    except:
        print("error occured.")
        recipient = ['email@gmail.com']
        #send_email("ERROR","ERROR",recipient)