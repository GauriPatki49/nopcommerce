import time


from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities import excel_utils
from utilities.custom_loggerfile import Log_Maker
from utilities.readproperties import Read_Config


class Test_02_Admin_Login_data_driven:
    url = Read_Config.get_admin_page_url()
    logger = Log_Maker.log_gen()
    path = ".\\test_data\\admin_login_data.xlsx"
    status_list = []
    
    def test_valid_admin_login_data_driven(self, setup):
        self.logger.info("*****test_valid_admin_login_data_driven_started*****")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.rows = excel_utils.get_row_count(self.path, "sheet1")
        print("num of rows", self.rows)
        
        for r in range(2, self.rows + 1):
            self.username = excel_utils.read_data(self.path, "sheet1", r, 1)
            self.password = excel_utils.read_data(self.path, "sheet1", r, 2)
            self.exp_login = excel_utils.read_data(self.path, "sheet1", r, 3)
            self.admin_lp.enter_user_email(self.username)
            self.admin_lp.enter_user_password(self.password)
            self.admin_lp.click_login()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp_login == "yes":
                    self.logger.info("test data is pass")
                    self.status_list.append("pass")
                    self.admin_lp.click_logout()
                elif self.exp_login == "no":
                    self.logger.info("test data is failed")
                    self.status_list.append("fail")
                    self.admin_lp.click_logout()
            elif act_title != exp_title:
                if self.exp_login == "yes":
                    self.logger.info("test data is failed")
                    self.status_list.append("fail")
                elif self.exp_login == "no":
                    self.logger.info("test data is failed")
                    self.status_list.append("fail")
        print("status list is", self.status_list)
        if "fail" in self.status_list:
            self.logger.info("test admin data driven test is failed")
            assert False
        else:
            self.logger.info("test admin data driven test is passed")
            assert True
            
        