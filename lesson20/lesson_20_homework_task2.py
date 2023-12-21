import json
from lesson11 import lesson_11_homework
import unittest
from unittest.mock import patch



class Test(unittest.TestCase):

    def test_open_phonebook(self):
        with open('lesson11/Phonebook_homework.json', 'r') as file:
            phonebook = json.load(file)
        self.assertEqual(phonebook, lesson_11_homework.open_phonebook())

    @patch('builtins.input', side_effect=['Karl', 'Smith', 'California', '+3809873216541745']) # mock-об'єкти замість 4 інпутів
    def test_add_new_contakt(self, input):
        with open('lesson11/Phonebook_homework.json', 'r') as file:
            phonebook = json.load(file)
        add_list = [{'first_name': 'KARL', 'last_name': 'SMITH', 'city': 'CALIFORNIA', 'phone': '+3809873216541745'}]
        self.assertEqual(lesson_11_homework.add_new(phonebook), phonebook + add_list)

    @patch('builtins.input', return_value='Illia')
    def test_find_firstname(self, input):
        contact = [{"first_name": "ILLIA", "last_name": "KOCHUROV", "city": "KREMENCHUK", "phone": "+3801234569"}]
        self.assertEqual(lesson_11_homework.find_first_name(), contact)

    @patch('builtins.input', return_value='+380987654321') # Ця перевірка спрацює тільки перший раз,
                                                            # бо замінюю інпут мок-об'єктом. Джейсон файл перезапишеться
                                                            # і з нього зникне оцей контакт, що я даю на інпут, в наступні перевірки треба міняти телефон в мок-об'єкті
    def test_del_contact(self, input):
        with open('lesson11/Phonebook_homework.json', 'r') as file:
            phonebook = json.load(file)
        for i in phonebook:
            if i.get('phone') == '+380987654321':
                a = i
        phonebook.remove(a)

        lesson_11_homework.delete_contact()
        with open('lesson11/Phonebook_homework.json', 'r') as file:
            phonebook_new = json.load(file)

        self.assertEqual(phonebook, phonebook_new)


if __name__ == "__main__":
    unittest.main()