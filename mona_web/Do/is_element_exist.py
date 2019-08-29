from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from common.logIn import LogInPage
from selenium import webdriver

POLL_FREQUENCY = 0.5  # How long to sleep inbetween calls to the method
IGNORED_EXCEPTIONS = (NoSuchElementException,)  # exceptions ignored during calls to the method

driver = webdriver.Firefox()
class is_Correct():

    def __init__(self, driver:webdriver.Firefox):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def is_text(self):
       ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(("xpath", ".//*[@id='userMenu']/a"), "admin"))
       return ele

if __name__ == "__main__":
    LogInPage(driver).log_in_page()
    a = is_Correct(driver)
    result = a.is_text()
    print(result)
