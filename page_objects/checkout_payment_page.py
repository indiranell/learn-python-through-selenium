"""
This class models the main Selenium tutorial page.
URL: selenium-tutorial-main
The page consists of a header, footer, form and table objects
"""
from .Base_Page import Base_Page
from page_objects.checkout_payment_object import Checkout_Payment_Object
from utils.Wrapit import Wrapit


class Checkout_Payment_Page(Base_Page,Checkout_Payment_Object):
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'cart'
        self.open(url)
