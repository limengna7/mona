from common import HTMLTestRunner_cn
import unittest

casepath = "C:\\Users\\LMN\\PycharmProjects\\Web_Auto"
rule = "test*.py"
discover = unittest.defaultTestLoader.discover(start_dir=casepath, pattern=rule)
print(discover)

reportpath = "C:\\Users\\LMN\\PycharmProjects\\Web_Auto\\report\\"+"report.html"
fp = open(reportpath, "wb")

runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                          title="报告的title",
                                          description="执行case的结果")
runner.run(discover)