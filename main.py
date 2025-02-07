import pandas as pd
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(name, email):
    sender_email = "kawaichan851@gmail.com"
    receiver_email = email
    password = "yczw kgej csdk cxqm"
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "BIRTHDAY WISHES!"
    
    body = f"""
    Dearest {name},

    Wishing you a very very Happy Birthday!


    P.S This is an automated email sent using Python.
        """
    
    message.attach(MIMEText(body, "plain"))

    # send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Load Dataframe
try:
    
    df = pd.read_csv("birthday.csv")
    print(df)
except FileNotFoundError:
    print("Error: Birthday_Tracker.csv file not found ")
    exit()
    
# Get today's date
today = datetime.datetime.now()
today_month = today.month
today_day = today.day
# print(today_day)

# Iterate through rows in DateFrame
for index, row in df.iterrows():
    birthday = pd.to_datetime(row['BirthDay'])
    birthday_month = birthday.month
    birthday_day = birthday.day
    
    
    if birthday_month == today_month and birthday_day == today_day:
        name = row['Name']
        email = row['Email']
        print(f"Today is {name}'s birthday!")
        
        send_email(name, email)