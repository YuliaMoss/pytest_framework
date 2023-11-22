from api_collections.base_api import BaseApi
import json


# from utilities.deco import auto_step
#
#
# @auto_step
class NotesApi(BaseApi):
    def __init__(self, base_url='https://practice.expandtesting.com/notes/api'):
        super().__init__(base_url)
        self.__url = '/notes'
        self.__headers = {
            'Content-Type': 'application/json',
            'x-auth-token': 'f0a4fb1919774a53a2e5707209cc600acacda12b21fe4c8c96fa86142f27f1e5'
        }

    def get_all_notes(self):
        return self._get(url=self.__url, headers=self.__headers)

    def get_note_by_id(self, note_id: str):
        return self._get(url=f'{self.__url}/{note_id}', headers=self.__headers)

    def post_new_note(self, note_data: dict):
        return self._post(self.__url, data=json.dumps(note_data), headers=self.__headers)
