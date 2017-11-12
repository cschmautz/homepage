"""
forms_tc.py

Test case class for the forms module.
"""

import unittest
import test
from src import forms


class FormsTestCase(unittest.TestCase):
    """
    TestCase surrounding the forms module's first class functions.
    """

    def test_form_title_basic(self):
        """
        A simple validation for the form subject regex checker (for emails).
        """
        ex_t = "Good jerb on yer site!!"
        self.assertTrue(forms.is_message_title_valid(ex_t),
                        msg="A simple title should pass validations!")

    def test_form_title_complex(self):
        """
        A simple validation for the form subject regex checker (for emails).
        """
        ex_t = "Whoaaa crazy title!! (Lols~`[/#_-[]()"
        self.assertTrue(forms.is_message_title_valid(ex_t),
                        msg="A complex title should pass validations!")

    def test_form_title_fail(self):
        """
        A validation for failure characters in the form title.
        """
        ex_t = "B@d title, b@d title - what ya gonna do!??!"
        self.assertFalse(forms.is_message_title_valid(ex_t),
                         msg="Bad chars should fail validations!")

    def test_form_body_basic(self):
        """
        A simple validation for the form body regex checker.
        """
        ex_b = """Wow! What a cool example your site is for Flask! Totes
                  ma-gotes man, keep it up.
               """

        self.assertTrue(forms.is_message_body_valid(ex_b),
                        msg="A simple message should pass validations!")

    def test_form_body_complex(self):
        """
        A more complex validation for the form body regex checker.
        """
        ex_b = """It has come to my attention, good sir, that in our midst
                  is a fine literary piece of work, whose nature is of the
                  cyber-brain-stuff the modern man calls 'programming';
                  however, I must admit there is more to be writ upon the
                  digital tablets!

                  Press on - to the mark of the high calling, and fulfill
                  the basic tenants of the linguistic and artist alike:
                  give your all to the craft, work until it doesn't seem like
                  it is work at all, and then break into greatness by showing
                  others the craft. Spread the love of the craft and live
                  forever through your works.
               """

        self.assertTrue(forms.is_message_body_valid(ex_b),
                        msg="A complex message should pass validations!")

    def test_form_body_fail(self):
        """
        A validation for failure characters inside the message body.
        """
        ex_b = """I just really don't like this f!@%*&-ing blog, and this
                  overused, overdone, 'material' theme that everyone and their
                  mother uses!

                  !@)$$!)@# be original! You're not a pro unless you use your
                  own JavaScript and CSS libraries, c'mon.
               """

        self.assertFalse(forms.is_message_body_valid(ex_b),
                         msg="A body with bad chars should fail validations!")

    def test_form_email_basic(self):
        """
        A simple validation for the email field's inputs.
        """
        ex_e = "wazzzzuuuup112@gmail.com"
        self.assertTrue(forms.is_message_email_valid(ex_e),
                        msg="A simple gmail email.. Should pass validations!")

    def test_form_email_complex(self):
        """
        A more complex validation for the email field's inputs.
        """
        ex_e = "j1.judo@mail.example.com"
        self.assertTrue(forms.is_message_email_valid(ex_e),
                        msg="A complex custom email / domain, should pass!")

    def test_form_email_failure(self):
        """
        A failure validation for the email field's inputs.
        """
        ex_e = "j1.judo.mail.example.com"
        self.assertFalse(forms.is_message_email_valid(ex_e),
                         msg="Non-valid characters should fail validations!")

    def test_form_email_ipv4(self):
        """
        A test for the IPv4 spec accetped by SMTP.
        """
        ex_e = "j1.judo@[24.254.16.245]"
        self.assertTrue(forms.is_message_email_valid(ex_e),
                        msg="IPv4 address regex for domain did not pass!")

    def test_form_email_ipv4_fail(self):
        """
        A failure test for the IPv4 spec accetped by SMTP.
        """
        ex_e = "j1.judo@[2455.2542.16.245]"
        self.assertFalse(forms.is_message_email_valid(ex_e),
                         msg="Incorrect IPv4 should not pass!")

    def test_form_email_ipv6(self):
        """
        A test for the IPv6 spec accetped by SMTP.
        """
        ex_e1 = "j1.judo@[2001:0db8:85a3:0000:0000:8a2e:0370:7334]"
        self.assertTrue(forms.is_message_email_valid(ex_e1),
                        msg="IPv6 address regex for domain did not pass!")

        ex_e2 = "j1.judo@[2001:db8:85a3:0:0:8a2e:370:7334]"
        self.assertTrue(forms.is_message_email_valid(ex_e2),
                        msg="IPv6 address regex for domain did not pass!")

        ex_e3 = "j1.judo@[::1]"
        self.assertTrue(forms.is_message_email_valid(ex_e3),
                        msg="IPv6 address regex for domain did not pass!")


if __name__ == '__main__':
    unittest.main()
