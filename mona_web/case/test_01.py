import unittest
from selenium import webdriver
from common.logIn import LogInPage
from selenium.webdriver.support import expected_conditions as EC
from common.Base import Base
import time

data1 = {"user":"admin", "psw":"123456", "expect":True}
data2 = {"user":"admin11", "psw":"123456", "expect":False}

class Test_CR(unittest.TestCase):
    loc_current_user = ("xpath", ".//*[@id='userMenu']/a")

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.a = Base(cls.driver)

    def setUp(self):
        self.driver.delete_all_cookies()

    def Log_case(self, user="admin", psw="123456", expect=True):
        LogInPage(self.driver).log_in_page(user, psw)
        result = self.a.is_text_exist(self.loc_current_user, user)
        print(result)
        expect_result = expect
        self.assertEqual(result, expect_result)


    def test_01(self):
        self.Log_case(data1["user"], data1["psw"], data1["expect"])

    def test_02(self):
        self.Log_case(data2["user"], data2["psw"], data2["expect"])

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
