from typing import Dict


class Vacancy:
    """Класс для предоставления вакансий"""

    __slots__ = ('_title', '_url', '_salary', '_description')

    def __init__(self, title: str, url: str, salary: str, description: str):
        self._title = title
        self._url = url
        self._salary = salary
        self._description = description

    @property
    def title(self) -> str:
        """Геттер для названия вакансии"""
        return self._title

    @property
    def salary(self) -> str:
        """Геттер для названия зарплаты"""
        return self._salary

    @property
    def url(self) -> str:
        """Геттер для ссылки на вакансию"""
        return self._url

    @property
    def description(self) -> str:
        """Геттер для описания вакансии"""
        return self._description

    def __lt__(self, other: 'Vacancy'):
        try:
            self._salary = self._parse_salary(self._salary)
        except ValueError:
            return self._salary < other._salary

    @classmethod
    def cast_to_object_list(cls, vacancies_data: list[Dict]) -> list['Vacancy']:
        """Преобразует список словарей в список объектов вакансий"""

        vacancies_list = []

        for item in vacancies_data:
            title = item.get('name', 'Нет названия')
            url = item.get('alternate_url', '')
            salary_info = item.get('salary')
            if salary_info and isinstance(salary_info, dict):
                salary_str = salary_info.get('from') or salary_info.get('to') or ''
                if salary_str and isinstance(salary_str, (int, float)):
                    salary_str = f"{salary_str} ₽"
                elif not salary_str:
                    salary_str = "Зарплата не указана"
            else:
                salary_str = "Зарплата не указана"
            description = item.get('snippet', {}).get('requirement', '')
            vacancy_obj = cls(title=title, url=url, salary=salary_str, description=description)
            vacancies_list.append(vacancy_obj)
        return vacancies_list
