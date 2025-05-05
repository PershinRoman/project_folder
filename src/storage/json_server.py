import json


class JSONserver:
    def __init__(self, filename='data/vacancies.json'):
        self.filename = filename

    def add_vacancy(self, vacancy):
        with open(self.filename, 'a') as f:
            json.dump(vacancy.__dict__, f)
            f.write('/n')

    def load_vacancies(self):
        with open(self.filename) as f:
            return [json.loads(line) for line in f]
