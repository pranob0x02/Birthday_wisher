from email import message
import pandas as pd
import datetime
import smtplib


#gmail credentials
GMAIL_ID = "gmail id"
GMAIL_PASS = "gmail pass"


def sendEmail(to, sub, msg):
    print(f"Email sent to: {to} \nsubject: {sub} \nmessage: {msg}")
    print("\n")

# configure less secure and login using gmail credentials.
    s = smtplib.SMTP('smtp.gmail.com', 587) #gmail smtp server and port
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PASS)
    s.sendmail(GMAIL_ID, to, f"subject:{sub}\n\n{msg}")
    s.quit()

if __name__ == "__main__":
    df = pd.read_excel(r"Automate Birthday Wish\birthday.xlsx") #path of excel file
    # print(df)
    
    today = datetime.datetime.now().strftime("%d-%m")
    # print(today)

    for index,item in df.iterrows():
        # print(item['birthday'])

        bday = item['birthday'].strftime("%d-%m")
        # print(bday)
        if (today==bday):
            sendEmail(item['email'], "Happy Birthday", item['message'])

             