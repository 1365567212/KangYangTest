'''
测试目的：测试用户注册接口
测试思路：
   1.正常注册》注册后查看时否有该用户
   2.注册的异常流程
        2.1 注册时手机号小于11位
        2.2 注册时手机号大于11位
        2.3 注册时手机验证码输入有问题
'''

import pytest

from config.admin_user import AdminUser
from utils.common import Common


class TestGetUserInfo():
    def setup(self):
        # 测试准备 获取令牌
        self.au = Common().login('13000000000', '123456')

    @pytest.mark.parametrize('user_id', [10])
    def test_get_user_info_mainflow01(self, user_id):
        '''
        1.获取用户信息
        :return:
        '''

        res = AdminUser().user_info(au=self.au, user_id=user_id)
        self.check_get_user_info_mainflow01(res=res)

    def check_get_user_info_mainflow01(self, res):
        assert res["status"] == 200
        assert res["message"] == "操作成功"
        assert res["data"]["userId"] == 10
        assert res["data"]["account"] == "13000000000"
        assert res["data"]["autoChangeFamily"] == 1

    def teardown(self):
        pass


if __name__ == '__main__':
    pytest.main(["-s", "test_get_user_info_mianflow.py"])
