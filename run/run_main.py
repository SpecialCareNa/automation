#coding:utf-8
import sys
import os

base_path = os.getcwd()
sys.path.append(base_path)
from util.handle_excel import excel_data
from base.base_request import request
from util.handle_init import handle_ini

#['teamsun001', '获取集群列表', 'yes',    None,       '/containercloud/api/clusters',             'get', None, 'yes', 'cluster_name', None]
#['teamsun002', '获取集群详情', 'yes', 'cluster_id', '/containercloud/api/clusters/{cluster_id}', 'get', None, 'yes', 'memory',       None]
class RunMain:
    def run_case(self):
        rows = excel_data.get_rows()
        for i in range(rows):
            data = excel_data.get_rows_value(i+2)
            is_run = handle_ini.get_value("is_run")
            is_run == data[2]
            if is_run == 'yes':
                method = data[5]
                url = data[4]
                data1 = data[6]
                res = request.run_main(url,method,data1)
                print(res)


if __name__ == '__main__':
    run = RunMain()
    run.run_case()