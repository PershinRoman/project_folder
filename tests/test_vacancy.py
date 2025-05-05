import unittest
from src.models.vacancy import Vacancy

class TestVacancy(unittest.TestCase):

    def test_initializate(self):
        vacancy = Vacancy("Python Developer", "http://example.com", "100000", "Требование: опыт работы от 3 лет.")

        self.assertEqual(vacancy.title, "Python Developer")
        self.assertEqual(vacancy.url, "http://example.com")
        self.assertEqual(vacancy.salary, "100000")
        self.assertEqual(vacancy.description, "Требование: опыт работы от 3 лет.")

if __name__ == '__main__':
    unittest.main()
