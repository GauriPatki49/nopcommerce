import time

from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.custom_loggerfile import Log_Maker

from utilities.readproperties import Read_Config


class Test_01_Admin_Login:
    url = Read_Config.get_admin_page_url()
    email = Read_Config.get_email()
    password = Read_Config.get_password()
    invalid_email = Read_Config.get_invalid_email()
    logger = Log_Maker.log_gen()
    
    def test_title_verification_page(self, setup):
        self.logger.info("*****Test_01_Admin_Login*****")
        self.logger.info("*****title verification of page*****")
        self.driver = setup
        self.driver.get(self.url)
        act_title = self.driver.title
        exp_title = "Your store. Login "
        if act_title == exp_title:
            self.logger.info("*****title verification of page matched*****")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshot\\test_title_verification_page.png")
            self.logger.info("*****title verification of page not matched*****")
            self.driver.close()
            assert False
    
    def test_invalid_email_id(self, setup):
        self.logger.info("*****test invalid email id*****")
        self.driver = setup
        self.driver.get(self.user_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_user_invalid_email(self.user_invalid_email)
        self.admin_lp.enter_user_password(self.user_password)
        self.admin_lp.click_login()
        act_error_text = self.driver.find_element(By.XPATH, "//li").text
        exp_error_text = "No customer account found"
        if act_error_text == exp_error_text:
            self.logger.info("*****invalid email of error message matched*****")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshot\\test_invalid_email.png")
            assert False
