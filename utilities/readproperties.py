import configparser

Config = configparser.RawConfigParser()
Config.read(".\\configuration\\config.ini")


class Read_Config:
    @staticmethod
    def get_admin_page_url():
        url = Config.get('admin login info', 'user_url')
        return url
    
    @staticmethod
    def get_email():
        email = Config.get('admin login info', 'email')
        return email
    
    @staticmethod
    def get_password():
        password = Config.get('admin login info', 'password')
        return password
    
    @staticmethod
    def get_invalid_email():
        invalid_email = Config.get('admin login info', 'invalid_email')
        return invalid_email
