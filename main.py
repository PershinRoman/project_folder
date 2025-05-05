from src.api.hh_api import HeadHunterAPI
from src.models.vacancy import Vacancy
from src.storage.json_server import JSONserver


def user_interaction():
    hh_api = HeadHunterAPI()
    json_server = JSONserver()

    search_query = input("ВВедите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    hh_vacancies = hh_api.get_vacancies(search_query)

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    for vacancy in vacancies_list:
        json_server.add_vacancy(vacancy)

    sorted_vacancies = sorted(vacancies_list)[:top_n]

    for v in sorted_vacancies:
        print(f"{v.title} - {v.salary} - {v.url}")


if __name__ == '__main__':
    user_interaction()
