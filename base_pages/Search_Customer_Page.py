from selenium.webdriver.common.by import By


class Search_Customer_Page:
    text_email_id = "SearchEmail"
    text_Firstname_id = "SearchFirstName"
    text_Lastname_id = "SearchLastName"
    button_search_id = "search-customers"
    text_company_id = "SearchCompany"
    
    row_table_xpath = "//table[@id='customers-grid']/tbody//tr"
    column_table_xpath = "//table[@id='customers-grid']/tbody//td"
    
    def __init__(self, driver):
        self.driver = driver
    
    def customer_email_id(self, email):
        self.driver.find_element(By.ID, self.text_email_id).clear()
        self.driver.find_element(By.ID, self.text_email_id).send_keys(email)
    
    def enter_customer_Firstname(self, Firstname):
        self.driver.find_element(By.ID, self.text_email_id).clear()
        self.driver.find_element(By.ID, self.text_email_id).send_keys(Firstname)
    
    def enter_customer_Lastname(self, Lastname):
        self.driver.find_element(By.ID, self.text_email_id).clear()
        self.driver.find_element(By.ID, self.text_email_id).send_keys(Lastname)
    
    def click_search_button(self):
        self.driver.find_element(By.ID, self.button_search_id).click()
    
    def enter_company_name(self, CompanyName):
        self.driver.find_element(By.ID, self.text_company_id).clear()
        self.driver.find_element(By.ID, self.text_company_id).send_keys()
    
    def get_result_row_table(self):
        return len(self.driver.find_elements(By.XPATH, self.row_table_xpath))
    
    def get_result_column_table(self):
        return len(self.driver.find_elements(By.XPATH, self.column_table_xpath))
    
    def search_customer_by_email(self, email):
        email_present_flag = False
        for r in range(1, self.get_result_row_table() + 1):
            cus_email = self.driver.find_element(By.XPATH,
                                                 "//table[@id='customers-grid']/tbody//tr[" + str(r) + "]//td[2]").text
            
            if cus_email == "email":
                email_present_flag = True
                break
        return email_present_flag
    
    def search_customer_by_name(self, name):
        name_present_flag = False
        for r in range(1, self.get_result_row_table() + 1):
            cus_name = self.driver.find_element(By.XPATH,
                                                "//table[@id='customers-grid']/tbody//tr[" + str(r) + "]//td[3]").text
            
            if cus_name == "name":
                name_present_flag = True
                break
        return name_present_flag
    
    def search_customer_by_CompanyName(self, CompanyName):
        CompanyName_present_flag = False
        for r in range(1, self.get_result_row_table() + 1):
            cus_CompanyName = self.driver.find_element(By.XPATH,
                                                       "//table[@id='customers-grid']/tbody//tr[" + str(
                                                           r) + "]//td[5]").text
            
            if cus_CompanyName == "CompanyName":
                CompanyName_present_flag = True
                break
        return CompanyName_present_flag
