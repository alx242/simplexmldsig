import os
import sys
import random
import unittest
from datetime import datetime, date, timedelta
from decimal import Decimal


sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'pyxmli'))
from pyxmli import (to_unicode, to_byte_string, is_valid_email,
                    Invoice, Payment, Group, Line, Discount, Tax)
from pyxmli import version


TODAY = date.today()
NOW = datetime.now()
DUMMY_PRODUCTS = (('PRODUCT_A', 'DESC_A'),
                  ('PRODUCT_B', 'DESC_B'),
                  ('PRODUCT_C', 'DESC_C'))
DUMMY_EMAILS = ['dummy-email@dispostable.com',
                'dummy-email@dispostable.co.uk',
                'dummy+hello@dispostable.co.uk',
                'dummy_hello@dispo-stable.co.uk',]
DUMMY_INVALID_EMAILS = ['dummy-email@.com',
                        'dummy$!email@.com',
                        'dummy-email@.co.ds',
                        '@dispo.co.ds',]
DUMMY_SELLER = {'name':'James Hetfield',
                'email':'hetfield@fourhorseman-gears.com',
                'address': {'street_address':'Death Magnetic street',
                            'zipcode':'00001',
                            'city':'San Francisco',
                            'state':'CA',
                            'country':'US'}}
DUMMY_BUYER = {'name': 'Kirk Hammett',
               'email': "hammett@fourhorseman-gears.com",
               'dddress': {'street_address':'Master of Puppets street',
                           'zipcode':'00002',
                           'city':'San Francisco',
                           'state':'CA',
                           'country':'US'}}


class XMLiTestCase(unittest.TestCase):
    def setUp(self):
        super(XMLiTestCase, self).setUp()
        
        
class UtilsTestCase(XMLiTestCase):
    def test_to_unicode(self):
        self.assertEqual(type(to_unicode('hello')), unicode,
                         'Expected a unicode instance.')
    
    def test_to_byte_string(self):
        self.assertEqual(type(to_byte_string(u'hello')), str,
                         'Expected a str instance.')
    
    def test_is_valid_email(self):
        for address in DUMMY_EMAILS:
            self.assertTrue(is_valid_email(address),
                            '%s is a valid email address.' % address)
            
        for address in DUMMY_INVALID_EMAILS:
            self.assertFalse(is_valid_email(address),
                            '%s is not a valid email address.' % address)


class PaymentTestCase(XMLiTestCase):
    AMOUNT = float('%d.%d' % (random.randint(), random.randint()))
    
    def __init__(self, *args, **kwargs):
        super(PaymentTestCase, self).__init__(*args, **kwargs)
        self.payment = Payment()
    
    def test_amount(self):
        self.assertRaises(ValueError, setattr, self.payment, 'amount', "hello")
        self.assertRaises(ValueError, setattr, self.payment, 'amount', "1.2.3")
        
        self.payment.amount = self.AMOUNT
        self.assertTrue(self.payment.amount == Decimal(str(self.AMOUNT)))
        
    def test_date(self):
        self.assertRaises(ValueError, setattr, self.payment, 'date', '12/6/12')
        self.assertRaises(ValueError, setattr, self.payment, 'date', 'hello')
        self.assertRaises(ValueError, setattr, self.payment, 'date', 1233445)
        
        self.payment.date = NOW
        self.assertTrue(self.payment.date == NOW)
        
        self.payment.date = TODAY
        self.assertTrue(self.payment.date == TODAY)
        


#MORE TESTS COMING
        
if __name__ == '__main__':
    unittest.main()