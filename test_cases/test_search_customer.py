import time

import pytest

from base_pages.Add_Customer_Page import Add_Customer_Page
from base_pages.Login_Admin_Page import Login_Admin_Page
from base_pages.Search_Customer_Page import Search_Customer_Page
from utilities.custom_loggerfile import Log_Maker
from utilities.readproperties import Read_Config


class Test_04_Search_Customer:
    user_url = Read_Config.get_admin_page_url()
    email = Read_Config.get_email()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()
    
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_search_customer_by_email(self, setup):
        self.logger.info("****Test_04_search_customer_started****")
        self.driver = setup
        
        self.driver.implicitly_wait(20)
        self.driver.get(self.user_url)
        self.driver.maximize_window()
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_user_email(self.email)
        self.admin_lp.enter_user_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("****login completed****")
        
        self.logger.info("****clicking customer option****")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_link_customer_menu_xpath()
        self.add_customer.click_link_customer_subOption_xpath()
        
        self.logger.info("****started search customer by an email****")
        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.customer_email_id("arthur_holmes@nopCommerce.com")
        self.search_customer.click_search_button()
        time.sleep(3)
        is_email_present = self.search_customer.search_customer_by_email("arthur_holmes@nopCommerce.com")
        if is_email_present == True:
            assert True
            self.logger.info("****Test_04_search_customer_by_email_test_passed****")
            self.driver.close()
        else:
            self.logger.info("****Test_04_search_customer_by_email_test_failed")
            self.driver.save_screenshot("//screenshot//test_search_customer_by_email.png")
            self.driver.close()
            assert False
        self.logger.info("****Test_04_search_customer_by_email_test_completed****")
        
    @pytest.mark.regression
    def test_search_customer_by_name(self, setup):
        self.logger.info("****Test_04_search_customer_started****")
        self.driver = setup
        
        self.driver.implicitly_wait(20)
        self.driver.get(self.user_url)
        self.driver.maximize_window()
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_user_email(self.email)
        self.admin_lp.enter_user_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("****login completed****")
        
        self.logger.info("****clicking customer option****")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_link_customer_menu_xpath()
        self.add_customer.click_link_customer_subOption_xpath()
        
        self.logger.info("****started search customer by name****")
        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.enter_customer_Firstname("Virat")
        self.search_customer.enter_customer_Lastname("Kohli")
        self.search_customer.click_search_button()
        time.sleep(3)
        is_name_present = self.search_customer.search_customer_by_name("Virat Kohli")
        if is_name_present == True:
            assert True
            self.logger.info("****Test_04_search_customer_by_email_test_passed****")
            self.driver.close()
        else:
            self.logger.info("****Test_04_search_customer_by_email_test_failed****")
            self.driver.save_screenshot("//screenshot//test_search_customer_by_name.png")
            self.driver.close()
            assert False
    
    @pytest.mark.regression
    def test_search_customer_by_CompanyName(self, setup):
        self.logger.info("****Test_04_search_customer_started****")
        self.driver = setup
        
        self.driver.implicitly_wait(20)
        self.driver.get(self.user_url)
        self.driver.maximize_window()
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_user_email(self.email)
        self.admin_lp.enter_user_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("****login completed****")
        
        self.logger.info("****clicking customer option****")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_link_customer_menu_xpath()
        self.add_customer.click_link_customer_subOption_xpath()
        
        self.logger.info("****Test_04_search_customer_by_CompanyName****")
        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.enter_company_name("Indian Cricket Team")
        self.search_customer.click_search_button()
        time.sleep(3)
        is_company_name = self.search_customer.search_customer_by_CompanyName("Indian Cricket Team")
        if is_company_name == True:
            assert True
            self.logger.log("****Test_04_search_customer_by_CompanyName_test_passed****")
            self.driver.close()
        else:
            self.logger.info("****Test_04_search_customer_by_CompanyName_test_failed****")
            self.driver.save_screenshot(".//screenshot//test_search_customer_by_CompanyName.png")
            self.driver.close()
            assert False
