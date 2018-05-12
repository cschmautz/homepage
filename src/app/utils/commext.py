""" commext.py: a module to facilitate site communication: comments, emails,
    etc.
"""


import os
import sys
import smtplib
from email import message

try:
    from ...instance import config
except ImportError:
    config = {} # should only happen in remote testsuite
    config['GMAIL_SMTP_USER'] = '' # reasonable default for testsuite
    config['GMAIL_SMTP_KEY'] = '' # reasonable default for testsuite

GUSER = config.GMAIL_SMTP_USER
GPASSWORD = config.GMAIL_SMTP_KEY

def gmail_login(user: str = GUSER, password: str = GPASSWORD):
    """
    Basic function to log in to Gmail's smtp server.
    """
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as gmail_smtp:
        gmail_smtp.login(user, password)


def gmail_send(msg: message.EmailMessage, msgfrom: str, msgto: str,
               user: str = GUSER, password: str = GPASSWORD):
    """
    Basic function to send email via Gmail's smtp server; requires a service
    account, or an app password.
    """
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as gmail_smtp:
        gmail_smtp.login(user, password)
        gmail_smtp.send_message(msg=msg, from_addr=msgfrom, to_addrs=msgto)


def form_message(msgfrom: str, msgto: str, subject: str, content: str) -> message.EmailMessage:
    """
    Used to form a message string into an EmailMessage object.
    """
    # NOTE: since the Gmail server strips off important information, put
    # this information inside the 'content' of the email message instead.
    msg_content = ("From: " + str(msgfrom) +
                   "\nSubject: " + str(subject) +
                   "\nContent: " + str(content))

    to_send = message.EmailMessage()
    to_send['From'] = msgfrom
    to_send['To'] = msgto
    to_send['Subject'] = subject
    to_send.set_content(msg_content)

    return to_send
