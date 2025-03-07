# locators from add new page
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Add_Customer_Page:
    def __init__(self, driver):
        self.driver = driver
    
    link_customer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_subOption_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    button_add_new_xpath = "//a[@class='btn btn-primary']"
    text_email_id = "Email"
    text_password_id = "Password"
    text_first_name_id = "FirstName"
    text_last_name_id = "Last name"
    radio_gender_male_id = "Gender_Male"
    radio_gender_female_id = "Gender_Female"
    text_dob_id = "DateOfBirth"
    text_company_name_id = "Company"
    checkbox_text_tax_exempt_id = "IsTaxExempt"
    newsletter_cursor_role_xpath = "//input[@type='search']"
    cursor_role_registered_xpath = "//li[contains(text(),'Registered')]"
    cursor_role_vendors_xpath = "//li[contains(text(),'Vendors')]"
    cursor_role_Guests_xpath = "//li[contains(text(),'Guests')]"
    cursor_role_Forum_Moderators_xpath = "//li[contains(text(),'Forum Moderators')]"
    cursor_role_Administrators_xpath = "//li[contains(text(),'Administrators')"
    drpdwn_manarvendr_id = "VendorId"
    checkbox_active_id = "Active"
    text_admincmet_id = "AdminComment"
    btn_save_xpath = "//button[@name='save']"
    
    def click_link_customer_menu_xpath(self):
        self.driver.find_element(By.XPATH, self.link_customer_menu_xpath).click()
    
    def click_link_customer_subOption_xpath(self):
        self.driver.find_element(By.XPATH, self.link_customer_subOption_xpath).click()
    
    def click_button_add_new_xpath(self):
        self.driver.find_element(By.XPATH, self.button_add_new_xpath).click()
    
    def enter_email(self, email):
        self.driver.find_element(By.ID, self.text_email_id).send_keys(email)
    
    def enter_password(self, password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)
    
    def enter_firstname(self, firstname):
        self.driver.find_element(By.ID, self.text_first_name_id).send_keys(firstname)
    
    def enter_lastname(self, lastname):
        self.driver.find_element(By.ID, self.text_last_name_id).send_keys(lastname)
    
    def select_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.radio_gender_male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.radio_gender_female_id).click()
        else:
            self.driver.find_element(By.ID, self.radio_gender_female_id).click()
    
    def enter_dob(self, dob):
        self.driver.find_element(By.ID, self.text_dob_id).send_keys(dob)
    
    def enter_companyName(self, companyName):
        self.driver.find_element(By.ID, self.text_company_name_id).send_keys(companyName)
    
    def click_taxExempt(self):
        self.driver.find_element(By.ID, self.checkbox_text_tax_exempt_id).click()
    
    def select_newsletter(self, value):
        elements = self.driver.find_elements(By.ID, self.newsletter_cursor_role_xpath)
        newsletter_field = elements[0]
        newsletter_field.click()
        time.sleep(3)
        if value == "Your Store Name":
            self.driver.find_element(By.XPATH, "//li[contains(text(),'Your store name')]").click()
        elif value == "//li[contains(text(),'Test store 2')]":
            self.driver.find_element(By.XPATH, "//li[contains(text(),'//li[contains(text(),'Test store 2')]").click()
        else:
            self.driver.find_element(By.XPATH, "//li[contains(text(),'Your store name')]").click()
    
    def select_customer_role(self, role):
        elements = self.driver.find_elements(By.XPATH, self.newsletter_cursor_role_xpath)
        customer_role = elements[0]
        customer_role.click()
        time.sleep(3)
        if role == "Administrators":
            self.driver.find_element(By.XPATH, self.cursor_role_Administrators_xpath).click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//span[@class='select2-selection__choice__remove']").click()
            customer_role.click()
            time.sleep(3)
        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH, self.cursor_role_Forum_Moderators_xpath).click()
        elif role == "Registered":
            self.driver.find_element(By.XPATH, self.cursor_role_registered_xpath).click()
        elif role == "Guests":
            self.driver.find_element(By.XPATH, self.cursor_role_Guests_xpath).click()
        elif role == "Vendors":
            self.driver.find_element(By.XPATH, self.cursor_role_vendors_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.cursor_role_registered_xpath).click()
            
    def select_drodwn_vendors(self,value):
        drodwn = Select(self.driver.find_element(By.ID, self.drpdwn_manarvendr_id))
        drodwn.select_by_visible_text(value)
    
    def click_active_id(self):
        self.driver.find_element(By.ID, self.checkbox_active_id).click()
        
    def enter_cmment_id(self, Admincomment):
        self.driver.find_element(By.ID, self.text_admincmet_id).send_keys(Admincomment)
    
    def click_button_xpath(self):
        self.driver.find_element(By.ID, self.btn_save_xpath).click()