"""
This is an example automated test to help you learn Qxf2's framework
SCOPE:
1) Launch Browser
2) Navigate to weather shopper page
4) Read the temperature and redirect to moisturizer or sunscreen depending on the temperature.
3) Select all items from the landed screen and add to cart
5) Verify the amount and numbers in cart page
6) Close the browser

"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.checkout_payment_form_conf as conf
import conf.testrail_caseid_conf as testrail_file
import random
import time
import string

def test_add_all_items_to_cart_and_checkout(base_url,browser,browser_version,os_version,os_name,remote_flag,testrail_flag,tesults_flag,test_run_id,remote_project_name,remote_build_name):

    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #1. Create a test object
        test_obj = PageFactory.get_page_object("Main Page",base_url=base_url)

        #2. Setup and register a driver and Set start_time with current time
        start_time = int(time.time())	
        test_obj.register_driver(remote_flag,os_name,os_version,browser,browser_version,remote_project_name,remote_build_name)
        
        #3.  get values from conf
        emailid = "aq"+randomStringwithDigitsAndSymbols()+ "@a.com"
        credit_card = conf.credit_card
        cvv=conf.cvv
        mmyy=conf.mmyy
        phone=conf.phone
        zip_code =conf.zip_code_text

        #3. Check the temperature and based on the temperature click on buy button of moiturizer or sunscreen 
        result_flag = test_obj.check_temp_and_click_product_category() 
        test_obj.log_result(result_flag,
                            positive="Successfully clicked on right button\n",
                            negative="Failed to click right button\nOn")
        
        #4. Add all items to the cart and checkout with payment
        result_flag = test_obj.add_all_items_and_verify_cart() 
        test_obj.log_result(result_flag,
                            positive="All items added successfully to the cart\n",
                            negative="Failed to add all items to the cart\nOn")

        #5.Checkout with payment
        result_flag = test_obj.do_checkout(emailid,credit_card,cvv,zip_code,mmyy,phone) 
        test_obj.log_result(result_flag,
                            positive="Successfully checkout is completed\n",
                            negative="Failed to checkout\nOn")
        
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))        
                
        #6. Print out the results
        test_obj.write_test_summary()

        #Teardown
        test_obj.wait(3)
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter
        test_obj.teardown()
        
    except Exception as e:
        print("Exception when trying to run test:%s"%__file__)
        print("Python says:%s"%str(e))

    assert expected_pass == actual_pass, "Test failed: %s"%__file__
       
#function to create random string values which will be appended to email id to make it unique everytime
def randomStringwithDigitsAndSymbols(stringLength=10):
    """Generate a random string of letters, digits and special characters """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

#---START OF SCRIPT   
if __name__=='__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()
                
    #Run the test only if the options provided are valid
    if options_obj.check_options(options): 
        #Run the test only if the options provided are valid
        test_add_all_items_to_cart_and_checkout(browser=options.browser,
                    base_url=options.url,
                    test_run_id=options.test_run_id,
                    testrail_flag=options.testrail_flag,
                    tesults_flag=options.tesults_flag,
                    remote_flag=options.remote_flag,
                    os_version=options.os_version,
                    browser_version=options.browser_version,
                    os_name=options.os_name,
                    remote_project_name=options.remote_project_name,
                    remote_build_name=options.remote_build_name)
    else:
        print('ERROR: Received incorrect input arguments')
        print(options_obj.print_usage())
