from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

POLL_FREQUENCY = 0.5  # How long to sleep inbetween calls to the method
IGNORED_EXCEPTIONS = (NoSuchElementException,)  # exceptions ignored during calls to the method
class Base():
    POLL_FREQUENCY = 0.5
    IGNORED_EXCEPTIONS = (NoSuchElementException,)

    def __init__(self, driver:webdriver.Firefox):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def FindElement(self, locator):
       ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
       return ele

    def sendKeys(self, locator, text):
        ele = self.FindElement(locator)
        ele.send_keys(text)

    def click(self, locator):
        ele = self.FindElement(locator)
        ele.click()

    def alertExist(self):
        a = self.driver.switch_to.alert
        text = a.text
        a.accept()
        return text

    def is_title(self, title):
        result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
        return result

    def is_title_contains(self, _title):
        result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
        return result

    def is_value_exist(self,locator, text):
        result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator, text))
        return result

    def is_text_exist(self, locator, text):
        try:
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, text))
            return ele
        except:
            return False

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
    loc_user = ("id", "account")
    loc_pas = ("name", "password")
    loc_submit = ("id", "submit")
    a = Base(driver)
    a.sendKeys(loc_user, "admin")
    a.sendKeys(loc_pas, "123456")
    a.click(loc_submit)
