from common.Base import Base
from selenium import webdriver

class LogInPage(Base):
    loc_user = ("id", "account")
    loc_psw = ("name", "password")
    loc_submit = ("id", "submit")

    def log_in_page(self, user, psw):
        self.driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
        self.sendKeys(self.loc_user, user)
        self.sendKeys(self.loc_psw, psw)
        self.click(self.loc_submit)
    
if __name__ == "__main__":
    driver=webdriver.Firefox()
    a = LogInPage(driver)
    a.log_in_page()
