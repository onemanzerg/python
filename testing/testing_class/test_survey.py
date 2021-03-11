import unittest
from survey import AnonymousSurvey

class TestAnonmySurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvey"""

    def test_store_single_response(self):
        """Проверяем, что один ответ попал в список"""
        question = "Какой язык программирования для вас наиболее интересен?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('Java')

        self.assertIn('Java', my_survey.responses)

if __name__ == '__name__':
    unittest.main()