"""
This class models the moisturizers page
"""
from .Base_Page import Base_Page
import conf.weather_shopper_conf as locators
from utils.Wrapit import Wrapit
import re

class Moisturizers_Object:
    "Page Object for the moisturizer's  page"
    #locators
    add_moisturizer_button = locators.add_moisturizer_sunscreen_button
    cart_count = locators.cart_count
    almond_price =locators.almond_price
    aloe_price = locators.aloe_price
    add_item = locators.add_item
    cart_button = locators.cart_button

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_add_moisturizer_button(self):
        "Click  moisturizers add button"
        result_flag = self.click_element(self.add_moisturizer_button)
        self.conditional_write(result_flag,
            positive='Clicked on add button for Moisturizer',
            negative='Could not click add button for Moisturizer',
            level='debug')    

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_all_moisturizer_button(self):
        "Click all add button for moisturizer's page"
        result_flag =False
        number_of_moisturizers= self.get_elements(self.add_moisturizer_button)
        for element in number_of_moisturizers:
            result_flag = self.click_element(self.add_moisturizer_button)
            self.conditional_write(result_flag,
            positive='Clicked on add moisturizer button',
            negative='Could not click on add moisturizer button',
            level='debug')    
        return result_flag
    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_added_count(self):
        "Check the count of added items to the cart with the number of add button. They should be same"
        result_flag =False
        number_of_moisturizers= self.get_elements(self.add_moisturizer_button)
        number_of_add_button = len(number_of_moisturizers)
        cart_cnt = self.get_text(self.cart_count)
        cart_cnt = cart_cnt.decode('utf-8')
        
        if(number_of_add_button == int(cart_cnt[0])):
            result_flag=True
            self.conditional_write(result_flag,
            positive='All moisturizers added to the cart',
            negative='Some moisturizers are not added to the cart',
            level='debug')    
        
        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def add_all_moisturizers_verify_cart(self):
        "Add all mosturizers to the cart and verify if added successfully"
        result_flag =self.click_all_moisturizer_button()
        result_flag &=self.check_added_count()    

        return result_flag
        
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_least_expensive_almond(self):
        list_price_least_expensive_almond =[]
        min_price =10000000
        self.wait(5)
        result_flag = False
        almonds_count = self.get_elements(self.almond_price)
        for element in almonds_count:
                split_price = element.text
                new_price = re.findall(r'\b\d+\b', split_price)
                new_price = int(new_price[0])
                if(new_price <= min_price):
                        min_price = new_price
                list_price_least_expensive_almond.append(new_price)
                result_flag = True
                self.conditional_write(result_flag,
                positive='Almonds are added to the array',
                negative='Could not create array of almonds',
                level='debug')    

        return list_price_least_expensive_almond 

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_least_expensive_almond(self,list_price_least_expensive_almond):
        "Click on add for least expensive almond"
        min_value = min(list_price_least_expensive_almond)
        min_value_str = str(min_value)
        result_flag = self.click_element(self.add_item%min_value_str)
        self.conditional_write(result_flag,
                positive='Clicked on almonds add button',
                negative='Could not click on add button of almonds',
                level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_least_expensive_aloe(self):
        list_price_least_expensive_aloe =[]
        min_price =10000000
        self.wait(5)
        result_flag = False
        aloe_count = self.get_elements(self.aloe_price)
        for element in aloe_count:
                split_price = element.text
                new_price = re.findall(r'\b\d+\b', split_price)
                new_price = int(new_price[0])
                if(new_price <= min_price):
                        min_price = new_price
                list_price_least_expensive_aloe.append(new_price)
                result_flag = True
                self.conditional_write(result_flag,
                positive='Aloe are added to the array',
                negative='Could not create array of aloe',
                level='debug')    

        return list_price_least_expensive_aloe 

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_least_expensive_aloe(self,list_price_least_expensive_aloe):
        "Click on add for least expensive Aloe"
        min_value = min(list_price_least_expensive_aloe)
        min_value_str = str(min_value)
        result_flag = self.click_element(self.add_item%min_value_str)
        self.conditional_write(result_flag,
                positive='Clicked on aloe add button',
                negative='Could not click on add button of aloe',
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
    def select_2_least_expensive_moisturizers(self):
        "select least priced almond and aloe moiturizers"
        list_price_least_expensive_almond =self.get_least_expensive_almond()
        list_price_least_expensive_aloe =self.get_least_expensive_aloe()
        result_flag =self.click_least_expensive_almond(list_price_least_expensive_almond)  
        result_flag &= self.click_least_expensive_aloe(list_price_least_expensive_aloe)
        result_flag &=self.click_cart()
        result_flag &=self.check_redirect_cart()

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_most_expensive_moisturizer(self):
        "get the most expensive item"
        list_price_most_expensive_moisturizer =[]
        min_price =10000000
        self.wait(5)
        result_flag = False
        number_of_items= self.get_elements(self.price_tag)
        for element in number_of_items:
            split_price = element.text
            new_price = re.findall(r'\b\d+\b', split_price)
            new_price = int(new_price[0])
            if(new_price >= min_price):
                min_price = new_price
            list_price_most_expensive_moisturizer.append(new_price)
            result_flag = True
        self.conditional_write(result_flag,
            positive='Most expensive item array is created',
            negative='Could not create array of most expenvie items',
            level='debug')    

        return list_price_most_expensive_moisturizer

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_add_expensive_moisturizer(self,list_price_most_expensive_moisturizer):
        "Click on add for expensive item"
        max_value = max(list_price_most_expensive_moisturizer)
        print(max_value)
        max_value_str = str(max_value)
        result_flag = self.click_element(self.add_most_expensive%max_value_str)
        self.conditional_write(result_flag,
            positive='Clicked on add of most expensive moisturizer',
            negative='Could not click expensive moisturizer ',
            level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def select_expensive_moisturizer(self):
        "Add all items to the cart and verify if added successfully"
        list_price_most_expensive_moisturizer =self.get_most_expensive_moisturizer()
        result_flag =self.click_add_expensive_moisturizer(list_price_most_expensive_moisturizer)
        result_flag &=self.click_cart()
        result_flag &=self.check_redirect_cart()
        return result_flag