from selenium.webdriver.common.by import By


class Login_Admin_Page:
    def __init__(self, driver):
        self.driver = driver
# locators from login page
    email = "//input[@id='Email']"
    password = "//input[@id='Password']"
    login = "//button[@type='submit']"
    invalid_email = "//input[@id='Email']"
    logout = "Logout"
    
    def enter_user_email(self, email):
        self.driver.find_element(By.XPATH, self.email).clear()
        self.driver.find_element(By.XPATH, self.email).send_keys(email)
    
    def enter_user_password(self, password):
        self.driver.find_element(By.XPATH, self.password).clear()
        self.driver.find_element(By.XPATH, self.password).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(By.XPATH, self.login).click()
    
    def enter_user_invalid_email(self, invalid_email):
        self.driver.find_element(By.XPATH, self.invalid_email).clear()
        self.driver.find_element(By.XPATH, self.invalid_email).send_keys(invalid_email)
    
    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout).click()
