#coding:utf-8
# from base import demo
import time
import unittest
import json
import HTMLTestRunner
import base.base_request

from base.base_request import RunMain

class TestMethod(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     print('类执行之前的方法')
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print('类执行之后的方法')

    def setUp(self):
        self.run = RunMain()
        # print('setup每次方法之前执行')

    # def tearDown(self):
    #     print('teardown每次方法之后执行')

    # @unittest.skip
    def test_01(self):
        url = 'http://172.16.191.250/opscenter/script/script_page/'
        aaa = json.dumps({'para': {'page': 1, 'per_page': 10}})
        data = {"json": aaa}
        res = self.run.run_main(url,'POST',data)
        # self.assertEqual(res['name'],2,"测试失败")
        # a = json.loads(res)
        print(res)
    # @unittest.skip

    def test_02(self):
        url = 'http://172.16.191.250/opscenter/script/check_script_name/'
        data = {
            'create_script_name':'3',
            'name':'3'
        }
        res = self.run.run_main(url, 'POST', data)
        # self.assertTrue(True, "测试失败")
        print(res)

    # @unittest.skip
    def test_03(self):
        url = 'http://172.16.191.250/app_center/application/check_create_ticket_bt?app_id=49'
        res = self.run.run_main(url, 'GET')
        self.assertTrue(res['success'],"测试失败")
        # globals()
        print(res)

    # @unittest.skip
    def test_04(self):
        url = 'http://172.16.191.250/app_center/application/check_create_ticket_bt?app_id=49'
        res = self.run.run_main(url, 'GET')
        # self.assertTrue('data',"测试失败")
        self.assertEqual(res['data'],{'is_create': False},"测试失败")
        print(res)

if __name__ == '__main__':
    # unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='example_dir'))
    # now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    # filename = "E:\\py\\" + now + "_result.html"
    # fp = open(filename, 'wb')
    # suite = unittest.TestSuite()
    # suite.addTest(TestMethod,'test_03')
    # suite.addTest(TestMethod,'test_04')
    # runner = HTMLTestRunner.HTMLTestRunner(
    # stream = fp,
    # title = u'搜索功能测试报告',
    # description = u'用例执行情况：')
    # runner.run(suite)
    # fp.close()


    # filepath = "../test/htmlreport.html"
    # fp = open(filepath,'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestMethod,'test_03')
    suite.addTest(TestMethod,'test_04')
    unittest.TextTestRunner().run(suite)
    # runer = HTMLTestRunner.HTMLTestRunner(stream=fp,title='report')
    # runer.run(suite)

    # suite = unittest.makeSuite(TestMethod, "test")

    # unittest.main()


