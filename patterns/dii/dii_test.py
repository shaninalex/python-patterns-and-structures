import unittest
from unittest.mock import patch

from dii import Authorizer_SMS, PaymentProcessor, Order


class Order_TestCase(unittest.TestCase):
    def test_init(self):
        order = Order()
        self.assertEqual(order.status, "open")

    def test_set_status(self):
        order = Order()
        order.set_status("paid")
        self.assertEqual(order.status, "paid")


class Authorizer_SMS_TestCase(unittest.TestCase):
    def test_init_authorized(self):
        auth = Authorizer_SMS()
        self.assertFalse(auth.is_authorized())

    def test_code_decimal(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        self.assertTrue(auth.code.isdecimal())

    def test_authorize_success(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        with patch("builtins.input", return_value=auth.code):
            auth.authorize()
            self.assertTrue(auth.is_authorized())

    @patch("builtins.input", return_value="1234567")
    def test_authorize_fail(self, mocked_input):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        auth.authorize()
        self.assertFalse(auth.is_authorized())


class PaymentProcessor_TestCase(unittest.TestCase):
    def test_init(self):
        auth = Authorizer_SMS()
        p = PaymentProcessor(auth)
        self.assertTrue(p.authorizer, auth)

    def test_payment_success(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        with patch("builtins.input", return_value=auth.code):
            p = PaymentProcessor(auth)
            order = Order()
            p.pay(order)
            self.assertEqual(order.status, "paid")

    def test_payment_fail(self):
        auth = Authorizer_SMS()
        auth.generate_sms_code()
        with patch("builtins.input", return_value="1234567"):
            p = PaymentProcessor(auth)
            order = Order()
            self.assertRaises(Exception, p.pay, order)
