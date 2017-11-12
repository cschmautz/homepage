""" commext.py: a module to facilitate site communication: comments, emails,
    etc.
"""


import os
import sys
import smtplib
from email import message


ROOT_DIR = os.path.abspath(__file__ + "/../../..")
print("root_dir: " + str(ROOT_DIR))
if __name__ == '__main__':
    sys.path.insert(0, ROOT_DIR)


from instance import config

USER = config.GMAIL_SMTP_USER
PASSWORD = config.GMAIL_SMTP_KEY

def gmail_login(user: str=USER, password: str=PASSWORD):
    """
    Basic function to log in to Gmail's smtp server.
    """
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as gmail_smtp:
        gmail_smtp.login(USER, PASSWORD)


def form_message(msgfrom: str, msgto:str, subject:str, body:str) -> message.EmailMessage:
    """ Used to form a message string into an EmailMessage object.
    """
    to_send = message.EmailMessage()
    to_send['From'] = msgfrom
    to_send['To'] = msgto
    to_send['Subject'] = subject
    to_send.set_content(body)

    return to_send
