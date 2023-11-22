import json
from api_collections.base_api import BaseApi


class UsersApi(BaseApi):
    def __init__(self, base_url='https://practice.expandtesting.com/notes/api'):
        super().__init__(base_url)
        self.__headers = {
            'Content-Type': 'application/json',
            'x-auth-token': 'None'
        }

    def post_new_users_register(self, user_data: dict):
        return self._post(url='/users/register', data=json.dumps(user_data), headers=self.__headers)

    def post_login_users(self, user_data: dict):
        return self._post(url='/users/login', data=json.dumps(user_data), headers=self.__headers)

    def get_users_profile(self, headers=None):
        return self._get(url='/users/profile', headers=headers or self.__headers)

    def get_headers(self):
        return self.__headers

    def update_headers(self, new_headers):
        self.__headers.update(new_headers)

    def patch_user_profile(self, data=None, headers=None):
        url = '/users/profile'
        return self._patch(url=url, data=json.dumps(data), headers=headers or self.__headers)

    def get_body(self):
        url = '/users/login'
        response = self._get(url)

        if response.status_code == 200:
            response_dict = response.json()  # Отримати JSON-тіло відповіді у вигляді словника
            return response_dict
        else:
            return 'Request error:', response.status_code
