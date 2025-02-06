import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import schedule
import time

# Path to the birthday file
file_path = "birthday.csv"

# Load birthday data from a CSV file
def load_birthdays(file_path):
    birthdays = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                birthdays.append(row)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"Error loading file: {e}")
    return birthdays

# Check if today is someone's birthday
def check_birthdays(birthdays):
    today = datetime.today().strftime('%m-%d')
    birthday_people = [person for person in birthdays if person['Birthday'] == "January"]
    return birthday_people

# Send an email
def send_email(to_email, subject, body):
    # Email credentials
    sender_email = "kawaichan851@gmail.com"
    sender_password = "yczw kgej csdk cxqm"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Main function to automate birthday emails
def birthday_email_automator():
    birthdays = load_birthdays(file_path)
    birthday_people = check_birthdays(birthdays)

    for person in birthday_people:
        name = person['Name']
        email = person['Email']
        message = f"Happy Birthday, {name}! Wishing you a wonderful day filled with joy and happiness."
        send_email(email, "Happy Birthday!", message)

# Schedule the script to run daily
schedule.every().day.at("08:00").do(birthday_email_automator)

print("Birthday Email Automator is running...")
while True:
    schedule.run_pending()
    time.sleep(1)




import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
import schedule
import time
from datetime import datetime, timedelta

def send_email(task_name, due_date, recipient_email):
    """Sends an email reminder."""
    sender_email = "salinaadhikari606@gmail.com"
    sender_password = "cdhk zzyw iamt deso"

    subject = "Weekly Task Reminder"
    body = f"Hello,\n\nThis is a reminder for your task: {task_name}.\nIt is due on: {due_date}.\n\nPlease ensure it is completed on time.\n\nBest regards,\nTask Reminder System"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"Email sent to {recipient_email} for task '{task_name}'.")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}. Error: {e}")

def check_tasks():
    """Checks the tasks in the CSV file and sends reminders for upcoming deadlines."""
    try:
        with open('tasks.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                task_name = row['task_name']
                due_date = datetime.strptime(row['due_date'], '%Y-%m-%d')
                recipient_email = row['email']

                # Check if the task is due within 7 days
                if datetime.now() <= due_date <= datetime.now() + timedelta(days=7):
                    send_email(task_name, due_date.strftime('%Y-%m-%d'), recipient_email)
    except FileNotFoundError:
        print("Error: 'tasks.csv' file not found.")
    except Exception as e:
        print(f"Error checking tasks: {e}")

# Schedule the task check weekly
schedule.every().monday.at("09:00").do(check_tasks)

print("Task reminder system is running...")
while True:
    schedule.run_pending()
    time.sleep(1)