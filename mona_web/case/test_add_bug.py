import unittest
from selenium import webdriver
from common.logIn import LogInPage
from common.addBug import AddBug
import time

class Test_CR(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        LogInPage(cls.driver).log_in_page("admin", "123456")
        cls.a = AddBug(cls.driver)

    def test01(self):

        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        title = "test BUG"+timestr
        self.a.add_bug(title)
        result = self.a.is_save_success(title)
        print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
