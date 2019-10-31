"""
This is an example automated test to help you learn Qxf2's framework
SCOPE:
1) Launch Browser
2) Navigate to weather shopper's sunscreens page
3) Select the least expensive sunscreen that is SPF-50 and For your second sunscreen, 
select the least expensive sunscreen that is SPF-30
4) click on cart and verify if cart page is loaded
5) Close the browser
"""

import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.example_form_conf as conf
import conf.testrail_caseid_conf as testrail_file

def test_select_2_least_expensive_sunscreens(base_url,browser,browser_version,os_version,os_name,remote_flag,testrail_flag,tesults_flag,test_run_id,remote_project_name,remote_build_name):

    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #1. Create a test object and load the sunscreens page.
        test_obj = PageFactory.get_page_object("Sunscreens",base_url=base_url)

        #2. Setup and register a driver and start the timer
        start_time = int(time.time())
        test_obj.register_driver(remote_flag,os_name,os_version,browser,browser_version,remote_project_name,remote_build_name)
               
        #3. Select least expensive sunscreens, one each from SPF-50 and SPF-30
        result_flag = test_obj.select_2_least_expensive_sunscreens() 
        test_obj.log_result(result_flag,
                            positive="Selected 2 least expensive sunscreens\n",
                            negative="Failed to select 2 least expensive sunscreens\nOn")
        
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
                
        #4. Print out the results
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
       
    
#---START OF SCRIPT   
if __name__=='__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()
                
    #Run the test only if the options provided are valid
    if options_obj.check_options(options): 
        #Run the test only if the options provided are valid
        test_select_2_least_expensive_sunscreens(browser=options.browser,
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
