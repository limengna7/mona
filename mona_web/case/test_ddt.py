# coding:utf-8
import ddt
import unittest
from selenium import webdriver
from common.logIn import LogInPage
from common.Base import Base
from common.read_excel import ExcelRead

'''
1.输入正确的用户名和密码
2.输入错误的用户名和正确的密码
3.输入正确的用户名和错误的密码
'''
#
# data =[{"user": "admin", "psw": "123456", "expect": True},
#        {"user": "adminxx", "psw": "123456", "expect": False},
#        {"user":"admin", "psw":"123456789", "expect":False}]
filepath = "C:\\Users\\LMN\\PycharmProjects\\Web_Auto\\common\\datas.xlsx"
data = ExcelRead(filepath)
d = data.dict_data()
print(d)

@ddt.ddt
class Test(unittest.TestCase):
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
        if expect == 'True':
            expect_result = True
        else:
            expect_result = False
        self.assertEqual(result, expect_result)

    @ddt.data(*d)
    def test_01(self, data):
        print("-----------开始测试-------------")
        print("测试数据：%s"%data)
        self.Log_case(data["user"], data["psw"], data["expect"])
        print("-----------测试结束-------------")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
