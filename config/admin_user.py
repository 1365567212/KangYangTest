import json

import requests


class AdminUser:

    def user_info(self, au, user_id=10):
        '''
        获取用户信息表
        :param au: 令牌
        :param user_id: int 用户id
        :return:
        '''

        # s = json.dumps({'userId': user_id})

        url = 'http://120.25.100.16:20050/admin/user/info'
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Authorization': au}
        params = {
            "userId": user_id
        }

        r = requests.get(url, params=params, headers=headers)
        res = r.json()
        return res

    def user_login(self, account, password):
        '''
        用户登录
        :param au: 令牌
        :param account: str 登录的账号
        :param password: str 登录密码
        :return:
        '''

        s = json.dumps({'account': account, 'password': password})

        url = 'http://120.25.100.16:20050/admin/user/login'
        headers = {'Content-Type': 'application/json'}

        r = requests.post(url, data=s, headers=headers)
        res = r.json()
        return res

    def user_register(self, account, password):
        '''
        用户注册
        :param au: 令牌
        :param account: str 登录的账号
        :param password: str 登录密码
        :return:
        '''

        s = json.dumps({'account': account, 'password': password})

        url = 'http://120.25.100.16:20050/admin/user/register'
        headers = {'Content-Type': 'application/json'}

        r = requests.post(url, data=s, headers=headers)
        res = r.json()
        return res

    def deviceinfo_delete(self, devices_id):
        '''
        删除设备
        :param devices_id: int 设备id
        :return:
        '''

        # s = json.dumps({'devices_id': devices_id})
        s = [1192]

        url = 'http://120.25.100.16:20050/admin/deviceinfo/delete'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'd057acf4-530f-43c4-a9a8-c28faac657ec'}

        r = requests.post(url, data=s, headers=headers)
        res = r.json()
        return res


if __name__ == '__main__':
    x = AdminUser().deviceinfo_delete(123)
    # print(type(x))
    print(x)
