from pymouse import PyMouse
from pykeyboard import PyKeyboard
from selenium import webdriver
from common.Base import Base
from common.logIn import LogInPage
import time

class AddBug(Base):
    loc_text = ("link text", "测试")
    loc_bug = ("link text","Bug")
    loc_add_bug = ("xpath", ".//*[@id='createActionMenu']/a")
    loc_click_trunck = ("xpath", ".//*[@id='openedBuild_chosen']/ul")
    loc_add_trunck = ("xpath", ".//*[@id='openedBuild_chosen']/div/ul/li")
    loc_title = ("id", "title")
    loc_upload = ("xpath", ".//*[@id='dataform']/table/tbody/tr[6]/td/div[2]/div[1]/span[18]/span")
    loc_view = ("css selector", ".ke-inline-block.ke-upload-button")
    loc_name = ("xpath", ".//*[@id='bugList']/tbody/tr[1]/td[4]/a")
    loc_sure = ("xpath", "html/body/div[3]/div[1]/div[3]/span[1]/input")

    def add_bug(self, title="test BUG"):

        self.click(self.loc_text)
        time.sleep(3)
        self.click(self.loc_bug)
        # time.sleep(2)
        self.click(self.loc_add_bug)
        # self.click(self.loc_click_trunck)
        # self.click(self.loc_add_trunck)
        # self.sendKeys(self.loc_title, title)
        # js = 'document.getElementsByClassName("ke-edit-iframe")[0].contentWindow.document.body.innerHTML="Hello World"'
        # self.driver.execute_script(js)
        self.click(self.loc_upload)
        self.click(self.loc_view)


    # def is_save_success(self, text):
    #     return self.is_text_exist(self.loc_name, text)

if __name__ == "__main__":
    driver = webdriver.Firefox()
    LogInPage(driver).log_in_page("admin", "123456")
    a = AddBug(driver)
    # timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
    # title = "test BUG"+timestr
    a.add_bug()
    time.sleep(5)
    k = PyKeyboard()

    k.type_string('c:\hello.txt')

    time.sleep(2)
    k.tap_key(k.enter_key)
    k.tap_key(k.enter_key)
    time.sleep(2)
    su = driver.find_element_by_xpath("html/body/div[3]/div[1]/div[3]/span[1]/input")
    su.click()
