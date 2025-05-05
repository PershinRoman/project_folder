class Vacancy:
    def __init__(self, title: str, url: str, salary: str, description: str):
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description

    def __lt__(self, other):
        return self.salary < other.salary

    @classmethod
    def cast_to_object_list(cls, vacancies_data):
        return [cls(item['name'], item['alternature_url'], item.get('salary', {}).get('from', 0),
                    item['snippet']['requirement']) for item in vacancies_data]
