"""
PageFactory uses the factory design pattern. 
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
Pages implemented so far:
1. Tutorial main page
2. Tutorial redirect page
3. Contact Page
4. Bitcoin main page
5. Bitcoin price page
"""

from page_objects.tutorial_main_page import Tutorial_Main_Page
from page_objects.moisturizer_page import Moisturizer_Page
from page_objects.sunscreen_page import Sunscreen_Page
from page_objects.weather_shopper_main_page import Weather_Shopper_Main_Page
from page_objects.checkout_payment_page import Checkout_Payment_Page
from conf import base_url_conf as conf


class PageFactory():
    "PageFactory uses the factory design pattern."
    def get_page_object(page_name,base_url=conf.base_url,trailing_slash_flag=True):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        if page_name == "main page":
            test_obj = Weather_Shopper_Main_Page(base_url=base_url,trailing_slash_flag=trailing_slash_flag)
        elif page_name == "moisturizers":
            test_obj = Moisturizer_Page(base_url=base_url,trailing_slash_flag=trailing_slash_flag)
        elif page_name == "sunscreens":
            test_obj = Sunscreen_Page(base_url=base_url,trailing_slash_flag=trailing_slash_flag)
        elif page_name == "cart" :
            test_obj = Checkout_Payment_Page(base_url=base_url,trailing_slash_flag=trailing_slash_flag)
        return test_obj

    get_page_object = staticmethod(get_page_object)