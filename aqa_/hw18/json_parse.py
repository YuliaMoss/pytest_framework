import json

import requests


class UserData:
    def __init__(self):
        self.user_name = 'Admin'
        self.user_password = 'Admin123'
        self.is_active = True
        self.pin = None

    def get_dict(self):
        return self.__dict__

    def get_json(self):
        return json.dumps(self.get_dict())


if __name__ == '__main__':
    user = UserData()
    # print(user.get_dict())
    # print(user.get_json())
    # my_json = '{"user_name": "Admin", "user_password": "Admin123", "is_active": true, "pin": null}'
    # print(json.loads(my_json))  # from json to dict
    # resp = requests.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    # pet_data = resp.json()
    # pet_python_object = json.loads(resp.text)
    # for i in pet_python_object:
    #     print(i)
    # assert pet_data == pet_python_object
