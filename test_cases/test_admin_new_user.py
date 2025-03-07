import random
import string
import time

from selenium.webdriver.common.by import By

from base_pages.Add_Customer_Page import Add_Customer_Page
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities import excel_utils
from utilities.custom_loggerfile import Log_Maker
from utilities.readproperties import Read_Config


class Test_03_Admin_New_User:
    user_url = Read_Config.get_admin_page_url()
    email = Read_Config.get_email()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()
    
    def test_admin_new_user(self, setup):
        self.logger.info("*****Test_03_Admin_new_customer_started*****")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.user_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_user_email(self.email)
        self.admin_lp.enter_user_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("****login completed****")
        
        self.logger.info("****started admin new user****")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_link_customer_menu_xpath()
        self.add_customer.click_link_customer_subOption_xpath()
        self.add_customer.button_add_new_xpath()
        
        self.logger.info("****proving customer info")
        email = generate_random_email()
        self.add_customer.enter_email(email)
        self.add_customer.enter_password("Test@123")
        self.add_customer.enter_firstname("Gauri")
        self.add_customer.enter_lastname("Mahurkar")
        self.add_customer.select_gender("Female")
        self.add_customer.enter_dob("2/2/2025")
        self.add_customer.enter_companyName("MyCompany")
        self.add_customer.click_taxExempt()
        self.add_customer.select_newsletter("Your store name")
        self.logger.info("****Your store name")
        self.add_customer.select_customer_role("Guests")
        self.add_customer.drpdwn_manarvendr_id("vendor1")
        self.add_customer.click_active_id()
        self.add_customer.enter_cmment_id("test admin comment")
        self.add_customer.btn_save_xpath()
        time.sleep(3)
        
        customer_add_success_text = "The new customer has been added successfully"
        success_text = self.driver.find_element(By.XPATH, "//div[@class='content-wrapper']/div[1]")
        success_text.text()
        if customer_add_success_text in success_text:
            assert True
            self.logger.info("****customer_add_success_text passed")
            self.driver.close()
        else:
            self.logger.info("****customer_add_success_text failed")
            self.driver.save_screenshot(".//screenshot//test_admin_new_user.png")
            self.driver.close()
            assert False


def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))  # 8 characters username
    domain = random.choices(['gmail.com', 'yahoo.com', 'outlook.com', 'example.com'])
    return f'{username}@{domain}'
