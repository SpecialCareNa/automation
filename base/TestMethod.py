#coding:utf-8
# from base import demo
import time
import unittest
import json
import HTMLTestRunner
import mock
import base.base_request

from base.base_request import RunMain
uri = 'http://172.16.134.133/:8000'
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
        self.assertEqual(res['data']['data'][0],
                         {'update_time': None,
                          'publish_time': None,
                          'create_user__name': 'admin',
                          'description': '',
                          'is_current_user': True,
                          'name': '5',
                          'update_user__name': None,
                          'create_time': '2019-11-07 11:28:22',
                          'all_os_version': 'centos 7.4',
                          'create_user_id': 1,
                          'is_published': False,
                          'id': 139,
                          'uuid': 'd465b1e2-d5e8-4702-8aef-a61fcec9594a'
                          },"测试失败")
        print(res)

    # @unittest.skip
    def test_02(self):
        url = 'http://172.16.191.250/opscenter/script/script_page/'
        aaa = json.dumps({'para': {'page': 1, 'per_page': 10}})
        data = {"json": aaa}
        mock_data = mock.Mock()
        res = self.run.run_main(url, 'POST', data)
        self.assertEqual(res['data']['data'][0],
                         {'update_time': None,
                          'publish_time': None,
                          'create_user__name': 'admin',
                          'description': '',
                          'is_current_user': True,
                          'name': '5',
                          'update_user__name': None,
                          'create_time': '2019-11-07 11:28:22',
                          'all_os_version': 'centos 7.4',
                          'create_user_id': 1,
                          'is_published': False,
                          'id': 139000000000,
                          'uuid': 'd465b1e2-d5e8-4702-8aef-a61fcec9594a'
                          }, "测试失败")
        print(res)

    # @unittest.skip
    def test_03(self):
        url = 'http://172.16.191.250/app_center/application/check_create_ticket_bt?app_id=49'
        res = self.run.run_main(url, 'GET')
        #断言，对比数据一致性
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


    def test_05(self):
        url = uri + '/containercloud/api/clusters/'
        res = self.run.run_main(url,'GET')
        self.assertEqual(res['results'][0]['cluster_name'], '123', "测试失败")

        print(res['results'][0])

if __name__ == '__main__':
    #云管url前缀


    #生成测试报告

    # now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    # filepath = "../report/" + now + "htmlreport.html"
    # fp = open(filepath,'wb')
    # suite = unittest.TestSuite()
    # suite.addTest(TestMethod('test_01'))
    # suite.addTest(TestMethod('test_02'))
    # suite.addTest(TestMethod('test_03'))
    # suite.addTest(TestMethod('test_04'))
    # runer = HTMLTestRunner.HTMLTestRunner(stream=fp,title='report')
    # runer.run(suite)

    #容器的方式运行case
    suite = unittest.TestSuite()
    # suite.addTest(TestMethod('test_01'))
    # suite.addTest(TestMethod('test_02'))
    # suite.addTest(TestMethod('test_03'))
    # suite.addTest(TestMethod('test_04'))
    suite.addTest(TestMethod('test_05'))
    unittest.TextTestRunner().run(suite)


    # unittest.main()


