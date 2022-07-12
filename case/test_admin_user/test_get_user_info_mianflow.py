'''
测试目的：测试获取用户信息接口
测试思路：
   获取17000000000的用户信息》检查返回的信息时否有误
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
        1.获取用户信息并检查用户信息是否正确
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

