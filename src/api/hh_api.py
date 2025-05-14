import requests
from typing import List, Dict


class HeadHunterAPI:
    """Класс для взаимодействия с апи ххру"""

    __slots__ = ()

    def __init__(self):
        pass

    def connect(self) -> requests.Session:
        session = requests.Session()
        return session

    BASE_URL = "http://api.hh.ru/vacancies"

    def get_vacancies(self, query: str) -> List[Dict]:
        session = self.__connect()
        response = requests.get(self.BASE_URL, params={"text": query})
        response.raise_for_status()
        return response.json().get('items', [])
