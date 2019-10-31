"""
This class models the sunscreens page
"""
from .Base_Page import Base_Page
import conf.weather_shopper_conf as locators
from utils.Wrapit import Wrapit
import re

class Sunscreens_Object:
    "Page Object for the Sunscreens page"
    
    #locators
    add_sunscreen_button = locators.add_moisturizer_sunscreen_button
    cart_count = locators.cart_count
    spf30_price=locators.spf30_price
    spf50_price=locators.spf50_price
    add_item =locators.add_item

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_add_sunscreen_button(self):
        "Click sunscreens add button"
        result_flag = self.click_element(self.add_sunscreen_button)
        self.conditional_write(result_flag,
            positive='Clicked on add button for sunscreen',
            negative='Could not click add button for sunscreen',
            level='debug')    

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_all_sunscreen_button(self):
        "Click all add button for sunscreen"
        result_flag =False
        number_of_sunscreens= self.get_elements(self.add_sunscreen_button)
        for element in number_of_sunscreens:
            result_flag = self.click_element(self.add_sunscreen_button)
            self.conditional_write(result_flag,
            positive='Clicked on add sunscreen button',
            negative='Could not click on add sunscreen button',
            level='debug')    
        
        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_added_count(self):
        "Check the count of added items to the card with the number of add button.They should be same"
        result_flag =False
        number_of_sunscreens= self.get_elements(self.add_sunscreen_button)
        number_of_add_button = len(number_of_sunscreens)
        cart_cnt = self.get_text(self.cart_count)
        cart_cnt = cart_cnt.decode('utf-8')
        
        if(number_of_add_button == int(cart_cnt[0])):
            result_flag=True
            self.conditional_write(result_flag,
            positive='All sunscreens added to the cart',
            negative='Some sunscreens are not added to the cart',
            level='debug')    
        
        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def add_all_sunscreens_verify_cart(self):
        "Add all sunscreens to the cart and verify if added successfully"
        result_flag =self.click_all_sunscreen_button()
        result_flag &=self.check_added_count()    

        return result_flag
    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_least_expensive_spf50(self):
        list_price_least_expensive_spf50 =[]
        min_price =10000000
        self.wait(5)
        result_flag = False
        spf50_count = self.get_elements(self.spf50_price)
        for element in spf50_count:
                split_price = element.text
                new_price = re.findall(r'\b\d+\b', split_price)
                new_price = int(new_price[0])
                if(new_price <= min_price):
                        min_price = new_price
                list_price_least_expensive_spf50.append(new_price)
                result_flag = True
                self.conditional_write(result_flag,
                positive='SPF-50 sunscreens are added to the array',
                negative='Could not create array of SPF-50 sunscreen',
                level='debug')    

        return list_price_least_expensive_spf50 

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_least_expensive_spf50(self,list_price_least_expensive_spf50):
        "Click on add for least expensive SPF-50 sunscreen"
        min_value = min(list_price_least_expensive_spf50)
        min_value_str = str(min_value)
        result_flag = self.click_element(self.add_item%min_value_str)
        self.conditional_write(result_flag,
                positive='Clicked on SPF-50 sunscreen add button',
                negative='Could not click on add button of SPF-50 sunscreen',
                level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_least_expensive_spf30(self):
        list_price_least_expensive_spf30 =[]
        min_price =10000000
        self.wait(5)
        result_flag = False
        spf30_count = self.get_elements(self.spf30_price)
        for element in spf30_count:
                split_price = element.text
                new_price = re.findall(r'\b\d+\b', split_price)
                new_price = int(new_price[0])
                if(new_price <= min_price):
                        min_price = new_price
                list_price_least_expensive_spf30.append(new_price)
                result_flag = True
                self.conditional_write(result_flag,
                positive='SPF-30 sunscreens are added to the array',
                negative='Could not create array of SPF-30 sunscreens',
                level='debug')    

        return list_price_least_expensive_spf30 

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_least_expensive_spf30(self,list_price_least_expensive_spf30):
        "Click on add for least expensive SPF-30 sunscreen"
        min_value = min(list_price_least_expensive_spf30)
        min_value_str = str(min_value)
        result_flag = self.click_element(self.add_item%min_value_str)
        self.conditional_write(result_flag,
                positive='Clicked on SPF-30 sunscreen add button',
                negative='Could not click on add button of SPF-30 sunscreen',
                level='debug')

        return result_flag
    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_cart(self):
        "Click cart items button"
        result_flag = self.click_element(self.cart_button)
        self.conditional_write(result_flag,
            positive='Clicked on cart button',
            negative='Could not click cart button',
            level='debug')    

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_redirect_cart(self):
        "Check the cart screen is loaded on redirect"
        result_flag = False
        cart_url = 'cart'        
        if cart_url.lower() in self.get_current_url().lower():
            result_flag = True
            self.switch_page("cart")
        self.conditional_write(result_flag,
            positive='Landed on cart screen',
            negative='Could not land on cart screen',
            level='debug')    

        return result_flag 

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def select_2_least_expensive_sunscreens(self):
        "select least priced SPF-50 and SPF-30 sunscreens"
        list_price_least_expensive_spf50 =self.get_least_expensive_spf50()
        list_price_least_expensive_spf30 =self.get_least_expensive_spf30()
        result_flag =self.click_least_expensive_spf50(list_price_least_expensive_spf50)  
        result_flag &= self.click_least_expensive_spf30(list_price_least_expensive_spf30)
        result_flag &=self.click_cart()
        result_flag &=self.check_redirect_cart()

        return result_flag

    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_most_expensive_sunscreens(self):
        "get the most expensive item"
        list_price_most_expensive_sunscreens =[]
        min_price =10000000
        self.wait(5)
        result_flag = False
        number_of_items= self.get_elements(self.price_tag)
        for element in number_of_items:
            split_price = element.text
            new_price = re.findall(r'\b\d+\b', split_price)
            new_price = int(new_price[1])
            if(new_price >= min_price):
                min_price = new_price
            list_price_most_expensive_sunscreens.append(new_price)
            result_flag = True
        self.conditional_write(result_flag,
            positive='Most expensive item array is created',
            negative='Could not create array of most expensive items',
            level='debug')    

        return list_price_most_expensive_sunscreens

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_add_expensive_sunscreens(self,list_price_most_expensive_sunscreens):
        "Click on add for expensive item"
        max_value = max(list_price_most_expensive_sunscreens)
        print(max_value)
        max_value_str = str(max_value)
        result_flag = self.click_element(self.add_most_expensive%max_value_str)
        self.conditional_write(result_flag,
            positive='Clicked on add of most expensive sunscreen',
            negative='Could not click expensive sunscreen ',
            level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def select_expensive_sunscreen(self):
        "Add all items to the cart and verify if added successfully"
        list_price_most_expensive_sunscreens =self.get_most_expensive_sunscreens()
        result_flag =self.click_add_expensive_sunscreens(list_price_most_expensive_sunscreens)
        result_flag &=self.click_cart()
        result_flag &=self.check_redirect_cart()
        return result_flag