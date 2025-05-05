import requests
from .abstract_api import AbstractAPI


class HeadHunterAPI(AbstractAPI):
    BASE_URL = "http://api.hh.ru/vacancies"

    def get_vacancies(self, query: str):
        response = requests.get(self.BASE_URL, params={"text": query})
        response.raise_for_status()
        return response.json().get('items', [])
