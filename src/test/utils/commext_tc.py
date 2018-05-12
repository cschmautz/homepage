"""
commext_tc.py: module for testing the commext.py module in the main
application code.
"""


import unittest
import datetime
from datetime import timezone
from email import message


from ...app.utils import commext


class CommextTestCase(unittest.TestCase):
    """
    TestCase surrounding the commext module's first class functions.
    """

    def test_login_to_gmail(self):
        """
        Test a simple logon to the Gmail SMTP server.
        """
        if commext.GUSER: # because reasons
            try:
                commext.gmail_login()
            except:
                self.fail("""
                        Something went wrong logging into the Gmail's smtp
                        server with the provided credentials! It is most
                        likely that the 'instance' folder is not configured
                        properly, or that some data has been overwritten.

                        Check that this folder exists at the project root,
                        and verify that 'config.py' exists there, with the
                        appropriate variables for connecting.
                        """)
        else:
            print(flush=True)
            print("GUSER not found - skipping test_login_to_gmail.", flush=True)

    def test_create_email_msg(self):
        """
        Test to ensure the EmailMessage object builder outputs the correct
        object upon creation.
        """
        test_date = datetime.datetime.now(timezone.utc).isoformat()

        msg = commext.form_message(msgfrom=commext.GUSER,
                                   msgto=commext.GUSER,
                                   subject=(str(test_date) + ' - Unit test, test.'),
                                   content='This is a test, nobody move!!')

        if not isinstance(msg, message.EmailMessage):
            self.fail("""
                      An 'EmailMessage' type was not returned from form_message
                      indicating a failure of the function's purpose - to build
                      such an object.
                      """)

        if msg['Subject'] != (str(test_date) + ' - Unit test, test.'):
            self.fail('The subject was not constructed as expected.')

        if msg['From'] != commext.GUSER:
            self.fail('The "From" header was not constructed as expected.')

        if msg['To'] != commext.GUSER:
            self.fail('The "To" header was not constructed as expected.')

        if msg.get_content() in 'This is a test, nobody move!!':
            self.fail('The message body was not constructed as expected.')

    def test_send_email_to_self(self):
        """
        Test sending an email to self.
        """

        if commext.GUSER: # because reasons
            test_date = datetime.datetime.now(timezone.utc).isoformat()

            msg = commext.form_message(msgfrom=commext.GUSER,
                                    msgto=commext.GUSER,
                                    subject=(str(test_date) +
                                                ' - test_send_email_to_self()'),
                                    content='This is a test, nobody move!!')

            try:
                commext.gmail_send(msg,
                                msgfrom=commext.GUSER,
                                msgto=commext.GUSER)
            except:
                self.fail("""
                        Something went wrong sending an email through Gmail's
                        SMTP endpoint. Ensure the idiomatic 'instance' folder
                        containing 'config.py' that has the necesary variables
                        to run this test.
                        """)
        else:
            print(flush=True)
            print("GUSER not found - skipping test_send_email_to_self.", flush=True)


if __name__ == '__main__':
    unittest.main()
