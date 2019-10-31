"""
This class models the cart and payment pages
"""
from .Base_Page import Base_Page
import conf.weather_shopper_conf as locators
from utils.Wrapit import Wrapit
import re


class Sunscreens_Moisturizers_Object:
    "Page Object for the cart and payment"
    
    #locators
    page_title = locators.page_title
    add_button = locators.add_moisturizer_sunscreen_button
    cart_count = locators.cart_count
    cart_button = locators.cart_button
    add_most_expensive = locators.add_item
    price_tag = locators.price_tag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_add_button(self,page_title):
        "Click add button"
        result_flag = self.click_element(self.add_button)
        self.conditional_write(result_flag,
            positive='Clicked on add button',
            negative='Could not click add button',
            level='debug')    

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_all_add_button(self):
        "Click all add buttons"
        result_flag =False
        number_of_items= self.get_elements(self.add_button)
        for element in number_of_items:
            result_flag = self.click_element(self.add_button)
            self.conditional_write(result_flag,
            positive='Clicked on add button',
            negative='Could not click on add button',
            level='debug')    
        return result_flag

    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_added_count(self):
        "Check the count of added items to the card with the number of add button. They should be same"
        result_flag =False
        number_of_items= self.get_elements(self.add_button)
        number_of_add_button = len(number_of_items)
        cart_cnt = self.get_text(self.cart_count)
        cart_cnt = cart_cnt.decode('utf-8')
        
        if(number_of_add_button == int(cart_cnt[0])):
            result_flag=True
            self.conditional_write(result_flag,
            positive='All items added to the cart',
            negative='Some items are not added to the cart',
            level='debug')    
        
        return result_flag
"""
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
    def get_most_expensive_sunscreen(self):
        "get the most expensive sunscreen"
        list_price_most_expensive =[]
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
            list_price_most_expensive.append(new_price)
            result_flag = True
        self.conditional_write(result_flag,
            positive='Most expensive item array is created',
            negative='Could not create array of most expenvie items',
            level='debug')    

        return list_price_most_expensive
        
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_most_expensive_moisturizer(self):
        "get the most expensive item"
        list_price_most_expensive =[]
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
            list_price_most_expensive.append(new_price)
            result_flag = True
        self.conditional_write(result_flag,
            positive='Most expensive item array is created',
            negative='Could not create array of most expenvie items',
            level='debug')    

        return list_price_most_expensive
        

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_add_expensive_item(self,list_price_most_expensive):
        "Click on add for expensive item"
        max_value = max(list_price_most_expensive)
        print(max_value)
        max_value_str = str(max_value)
        result_flag = self.click_element(self.add_most_expensive%max_value_str)
        current_url = self.get_current_url()
        sunscreen_text ='sunscreen'
        if sunscreen_text in current_url:
            self.conditional_write(result_flag,
            positive='Clicked on add of most expensive sunscreen',
            negative='Could not click expensive sunscreen button',
            level='debug')    
        else :
            self.conditional_write(result_flag,
            positive='Clicked on add of most expensive moisturizer',
            negative='Could not click expensive moisturizer ',
            level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def add_all_items_and_verify_cart(self):
        "Add all items to the cart and verify if added successfully"
        result_flag =self.click_all_add_button()
        result_flag &=self.check_added_count()   
        result_flag &=self.click_cart() 
        result_flag &=self.check_redirect_cart()

        return result_flag

    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def select_expensive_sunscreen(self,list_price_most_expensive):
        "Add all items to the cart and verify if added successfully"
        #result_flag =self.get_most_expensive_sunscreen()
        result_flag =self.click_add_expensive_item(list_price_most_expensive)
        return result_flag
    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def select_expensive(self,list_price_most_expensive):
        "Add all items to the cart and verify if added successfully"
        #result_flag =self.get_most_expensive_sunscreen()
        result_flag =self.click_add_expensive_moisturizer(list_price_most_expensive)
        return result_flag
    """