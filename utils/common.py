from config.admin_user import AdminUser


class Common():
    def login(self, account, password):
        res = AdminUser().user_login(account=account, password=password)
        token = res['data']['token']
        return token
