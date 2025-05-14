import requests
from typing import List, Dict
from src.api.hh_api import HeadHunterAPI
from src.models.vacancy import Vacancy
from src.storage.json_server import JSONserver


def user_interaction():
    """Основная функция взаимодействия с пользователем"""
    hh_api = HeadHunterAPI()
    json_server = JSONserver()

    search_query = input("ВВедите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    try:
        hh_vacancies: List[Dict] = hh_api.get_vacancies(search_query)

        vacancies_list: List[Dict] = Vacancy.cast_to_object_list(hh_vacancies)

        for vacancy in vacancies_list:
            json_server.add_vacancy(vacancy)

        sorted_vacancies: List[Vacancy] = sorted(vacancies_list)[:top_n]

        for v in sorted_vacancies:
            print(f"{v.title} - {v.salary} - {v.url}")
    except requests.RequestException as e:
        print(f"Ошибка при получении данных от API: {e}")
    except ValueError as e:
        print(f"Неккоректный ввод числа: {e}")

if __name__ == '__main__':
    user_interaction()
