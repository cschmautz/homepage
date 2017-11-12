import os
import sys
import unittest
import test


ROOT_DIR = os.path.abspath(__file__ + "/../../..")
print("root_dir: " + str(ROOT_DIR))
if __name__ == '__main__':
    sys.path.insert(0, ROOT_DIR)


from src.utils import commext


class CommextTestCase(unittest.TestCase):
    """
    TestCase surrounding the commext module's first class functions.
    """

    def test_login_to_gmail(self):
        """ Test a simple logon to the Gmail SMTP server.
        """
        try:
            commext.gmail_login()
        except:
            self.fail(msg="""
                           Something went wrong logging into the Gmail's smtp
                           server with the provided credentials! It is most
                           likely that the 'instance' folder is not configured
                           properly, or that some data has been overwritten.

                           Check that this folder exists at the project root,
                           and verify that 'config.py' exists there, with the
                           appropriate variables for connecting.
                           """)


if __name__ == '__main__':
    unittest.main()
