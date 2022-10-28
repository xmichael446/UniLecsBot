import requests
from config import *
from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["X-ACCESS-KEY"] = DATA_ACCESS_KEY

class InfoService:
    def __init__(self, data=None, version=None):
        self.data = data
        self.version = version

    def get_info_data(self):
        if self.data is None or self.version != TASKS_URL_VERSION:
            response = requests.get(INFO_URL, headers=headers)
            self.version = TASKS_URL_VERSION
            self.data = (
                response.json()["record"]
                if response and response.status_code == 200
                else None
            )
        return self.data

    def get_books_message(self):
        books_message = self.get_info_data()["books"]
        return books_message

    def get_all_tasks_link(self):
        books_message = self.get_info_data()["all_tasks"]
        return books_message

    def get_categories_dict(self):
        categories_dict = self.get_info_data()["categories"]
        return categories_dict