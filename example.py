# -*- coding: utf-8 -*-
import os
from datetime import datetime, date, timedelta
from pyxmli import (Invoice, Group, Line, Tax, Discount, Address, Payment,
                    INVOICE_PAID, RATE_TYPE_FIXED, RATE_TYPE_PERCENTAGE)

'''
XMLi is an open source invoice serialization format.
PyXMLI attempts to reproduce its structure and the container pattern
it's based on.

    Invoice
        Group
            Line
                Tax
                Discount
'''

invoice = Invoice(name="Online shopping on Guitar Heroes Store",
                  description="Perfect gears for a quick jam.",
                  currency="USD",
                  status=INVOICE_PAID,
                  date=datetime.now(),
                  due_date=date.today() + timedelta(days=60),
                  mentions='Guitar Heros Store LLC.',
                  terms='All order changes or cancellations should be ' \
                  'reported prior to shipping and by phone on ' \
                  '1-555-555-5555. Email is not accepted.', #optional
                  custom_id="FF123456")

#Seller
invoice.seller.name = "Guitar Heroes Store"
invoice.seller.email = "contact@guitar-heroes-store.com"
invoice.seller.address = Address(street_address="Boulevard du Lido",
                                 city="Casablanca",
                                 zipcode="20100",
                                 country="MA")

#Billing contact and address
invoice.buyer.name = "Stevie Ray Vaughan"
invoice.buyer.email = "stevie@ray-vaughan.com"
invoice.buyer.address = Address(street_address="E Riverside Dr",
                                city="Austin",
                                state='TX',
                                zipcode="78704",
                                country="US")

#Shipping recipient and address (optional)
invoice.shipping.recipient = invoice.buyer

#Groups allow you to structure your invoice and organize your items 
#in categories. An invoice must at least have one Group instance.
group = Group()
invoice.groups.append(group)

'''
About taxes and discounts:

Every component - and especially taxes and discounts - of the XMLi format has 
been designed to be flexible enough to cover a wide range of countries, 
industries and different scenarios.

Things you should know:
    1. Both are applied on a line per line basis
    2. Both are expressed as a fixed value, or as a percentage of the gross
        total of the line 
    3. Taxes are calculated on the amount left after the discounts
        have been applied
    4. You can't express a discount by adding an invoice line with
        a negative total
'''

#Define a Discount instance that we'll attach to one or many invoice lines
promo_code = Discount(name='Promo Code',
                      description="$30 discount",
                      rate=30,
                      rate_type=RATE_TYPE_FIXED)

#Define a Tax instance that we'll attach to one or many invoice lines  
vat = Tax(name='VAT',
          description="Sales Tax",
          rate=8.25,
          rate_type=RATE_TYPE_PERCENTAGE)

#Instantiate a line to describe an invoice item, and add it to a group
group.lines.append(Line(name="SRV Fender Stratocaster",
                        description="SRV's collaboration with Fender",
                        quantity=1, unit_price=2399.99))

group.lines.append(Line(name="Marshall AS100D Amplifier",
                        description='50 Watt + 50 Watt, 2x8" combo with ' \
                        'two high fidelity, polymer dome tweeters.',
                        quantity=1, unit_price=699.99))

group.lines.append(Line(name="Dunlop JH1B wah-wah pedal",
                        description='Reproduce the famous tones of Hendrix ' \
                        'wah solos from the late 60s.',
                        quantity=1, unit_price=129.99))

#Attach taxes and discounts to lines 
for line in group.lines:
    line.taxes.append(vat)
    line.discounts.append(promo_code)
    
invoice.payments.append(Payment(amount=invoice.total,))

#Sign the invoice using RSA encryption keys ('ssh-keygen -t rsa -b 1024')
keys_dir = os.path.join(os.path.dirname(__file__), 'tests')
print invoice.to_signed_str(open(os.path.join(keys_dir, 'id_rsa'), 'rb'), 
                            open(os.path.join(keys_dir, 'id_rsa.pub'), 'rb'))


'''
OUTPUT:
<invoice invoice-agent="PyXMLi 0.0.1a" version="2.0"><seller><name><![CDATA[Guitar Heroes Store]]></name><email>contact@guitar-heroes-store.com</email><address><streetAddress><![CDATA[Boulevard du Lido]]></streetAddress><city><![CDATA[Casablanca]]></city><zipcode>20100</zipcode><country>MA</country></address></seller><buyer><name><![CDATA[Stevie Ray Vaughan]]></name><email>stevie@ray-vaughan.com</email><address><streetAddress><![CDATA[E Riverside Dr]]></streetAddress><city><![CDATA[Austin]]></city><zipcode>78704</zipcode><state><![CDATA[TX]]></state><country>US</country></address></buyer><shipping><recipient><name><![CDATA[Stevie Ray Vaughan]]></name><email>stevie@ray-vaughan.com</email><address><streetAddress><![CDATA[E Riverside Dr]]></streetAddress><city><![CDATA[Austin]]></city><zipcode>78704</zipcode><state><![CDATA[TX]]></state><country>US</country></address></recipient></shipping><name><![CDATA[Online shopping on Guitar Heroes Store]]></name><description><![CDATA[Perfect gears for a quick jam.]]></description><currency>USD</currency><status>paid</status><date>2012-07-31</date><dueDate>2012-09-29</dueDate><customId><![CDATA[FF123456]]></customId><terms><![CDATA[All order changes or cancellations should be reported prior to shipping and by phone on 1-555-555-5555. Email is not accepted.]]></terms><mentions><![CDATA[Guitar Heros Store LLC.]]></mentions><total>3399.01752</total><payments><payment><amount>3399.01752</amount><date>2012-07-31</date><method>other</method></payment></payments><body><groups><group><lines><line><date>2012-07-31</date><name><![CDATA[SRV Fender Stratocaster]]></name><description><![CDATA[SRV's collaboration with Fender]]></description><quantity>1</quantity><unitPrice>2399.99</unitPrice><discounts><discount description="$30 discount" name="Promo Code" type="fixed">30</discount></discounts><taxes><tax description="Sales Tax" name="VAT" type="percentage">8.25</tax></taxes></line><line><date>2012-07-31</date><name><![CDATA[Marshall AS100D Amplifier]]></name><description><![CDATA[50 Watt + 50 Watt, 2x8" combo with two high fidelity, polymer dome tweeters.]]></description><quantity>1</quantity><unitPrice>699.99</unitPrice><discounts><discount description="$30 discount" name="Promo Code" type="fixed">30</discount></discounts><taxes><tax description="Sales Tax" name="VAT" type="percentage">8.25</tax></taxes></line><line><date>2012-07-31</date><name><![CDATA[Dunlop JH1B wah-wah pedal]]></name><description><![CDATA[Reproduce the famous tones of Hendrix wah solos from the late 60s.]]></description><quantity>1</quantity><unitPrice>129.99</unitPrice><discounts><discount description="$30 discount" name="Promo Code" type="fixed">30</discount></discounts><taxes><tax description="Sales Tax" name="VAT" type="percentage">8.25</tax></taxes></line></lines></group></groups></body><Signature xmlns="http://www.w3.org/2000/09/xmldsig#"><SignedInfo xmlns="http://www.w3.org/2000/09/xmldsig#"><CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments"></CanonicalizationMethod><SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"></SignatureMethod><Reference URI=""><Transforms><Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"></Transform></Transforms><DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"></DigestMethod><DigestValue>Hgs2jtw2Isw70npd4hQBFN3FMcg=</DigestValue></Reference></SignedInfo><SignatureValue>SkdKipnzDzjNxJ+yX/wFAjIFv6z3z5Z4ViWop3pu9DsVU4znNP2aTDFoEm5SuL5dEsRiMQLifnThB1+ZPChLTn9GZO+UX5jNlaSdfRHzjFj22zN7r/VffTRgrG7lMiWxUl+xx9eQdF5EZAEB27X728JGPGLH4y9s5svxfFvHroY=</SignatureValue><KeyInfo><KeyValue><RSAKeyValue><Modulus>4OigfQFbFIsM/oERNAKSeEBkFGsM13t03G/6j4r13YA3ZzRdqEPOhyGIy4M/bS96JB653PYpgrlTRC1FYIBJ0t0nqWiSybwgERsO8F44YX+AMI4DT7kcbZU1lF20WhuBwX0FJJETba8zQc2t1lJL81h49fy70jJ1aSlb+/ClhHc=</Modulus><Exponent>AQAB</Exponent></RSAKeyValue></KeyValue></KeyInfo></Signature></invoice>
'''