"""
This class models the table on the Selenium tutorial page
"""
from .Base_Page import Base_Page
import conf.weather_shopper_conf as locators
from utils.Wrapit import Wrapit


class Checkout_Payment_Object:
    "Page Object for the weather shopper's checkout page objects"

    #locators
    pay_with_card = locators.pay_with_card
    email_text =locators.email_text
    card_number_text=locators.card_number_text
    mm_yy_text=locators.mm_yy_text
    cvc_text=locators.cvc_text
    remember_me_checkbox=locators.remember_me_checkbox
    pay_button = locators.pay_button
    zip_code_text=locators.zip_code_text
    phone_text=locators.phone_text
    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_pay_with_card(self):
        "Click on the pay with card button"
        result_flag = self.click_element(self.pay_with_card)
        self.conditional_write(result_flag,
            positive='Clicked on pay with card',
            negative='Could not click pay with card button',
            level='debug')    

        return result_flag 

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def switch_to_popup_iframe(self):
        "Switch to iframe"
        result_flag = False
        self.switch_frame("stripe_checkout_app")
        result_flag = True
        self.conditional_write(result_flag,
            positive='Switched to Iframe',
            negative='Could not switch to Iframe',
            level='debug')    

        return result_flag
    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def switch_out_from_popup_iframe(self):
        "Switch back from iframe"
        result_flag = False
        self.switch_frame()
        result_flag = True
        self.conditional_write(result_flag,
            positive='Switched back from Iframe',
            negative='Could not switch back from Iframe',
            level='debug')    

        return result_flag
 
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def set_email(self,email):
        "Set the email on the form"
        result_flag = self.set_text(self.email_text,email)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%email,
            negative='Failed to set the email in the form',
            level='debug')

        return result_flag
    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def set_credit_card(self,card_number):
        "Set the credit card number on the form"
        result_flag = self.set_text(self.card_number_text,card_number)
        self.conditional_write(result_flag,
            positive='Set the credit card number to: %s'%card_number,
            negative='Failed to set the credit card number in the form',
            level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def set_mm_yy(self,mmyy):
        "Set the credit card number on the form"
        result_flag = self.set_text(self.mm_yy_text,mmyy)
        self.conditional_write(result_flag,
            positive='Set the mm/yy number to: %s'%mmyy,
            negative='Failed to set the mm/yy  in the form',
            level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def set_cvc(self,cvv):
        "Set the cvv number on the form"
        result_flag = self.set_text(self.cvc_text,cvv)
        self.conditional_write(result_flag,
            positive='Set the cvc number to: %s'%cvv,
            negative='Failed to set the cvc  in the form',
            level='debug')

        return result_flag
    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def set_zipcode(self,zipcode):
        "Set the zip code number on the form"
        result_flag = self.set_text(self.zip_code_text,zipcode)
        self.conditional_write(result_flag,
            positive='Set the zip code number to: %s'%zipcode,
            negative='Failed to set the zip code  in the form',
            level='debug')

        return result_flag
    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_checkbox_remember_me(self):
        "select the remember me checkbox on the form"
        result_flag = self.select_checkbox(self.remember_me_checkbox)
        self.conditional_write(result_flag,
            positive='Set the remember me checkbox',
            negative='Failed to check remember me checkbox in the form',
            level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def set_phone(self,phone):
        "Set the phone number on the form"
        result_flag = self.set_text(self.phone_text,phone)
        self.conditional_write(result_flag,
            positive='Set the phone number to: %s'%phone,
            negative='Failed to set the phone in the form',
            level='debug')

        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_pay_button(self):
        "Click on the pay button"
        result_flag = self.click_element(self.pay_button)
        self.conditional_write(result_flag,
            positive='Clicked on pay button',
            negative='Could not click pay button',
            level='debug')    

        return result_flag 

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_redirect_confirmations(self):
        "Check on confirmation screen is loaded on redirect"
        result_flag = False
        url_landed = self.get_current_url()
        confirmation_word = 'confirmation'      
        if confirmation_word.lower() in url_landed.lower():
            result_flag = True
        self.conditional_write(result_flag,
            positive='Landed on confirmation screen',
            negative='Could not land on confirmation screen',
            level='debug')    

        return result_flag
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def do_checkout(self,emailid,credit_card,cvv,zipcode,mmyy,phone):
        "Make the payment for items added in the cart"
        result_flag =self.click_pay_with_card()
        result_flag &=self.switch_to_popup_iframe()  
        result_flag &=self.set_email(emailid)    
        result_flag &=self.set_credit_card(credit_card)  
        result_flag &=self.set_mm_yy(mmyy)
        result_flag &=self.set_cvc(cvv)
        result_flag &=self.set_zipcode(zipcode)
        result_flag &=self.check_checkbox_remember_me()
        result_flag &=self.set_phone(phone)
        result_flag &=self.click_pay_button()
        result_flag &=self.switch_out_from_popup_iframe()
        result_flag &=self.check_redirect_confirmations()
        

        return result_flag