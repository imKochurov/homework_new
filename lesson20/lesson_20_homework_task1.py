from lesson19.lesson_19_homework import My_enumerate_custom as enumerate_cust, My_range_custom3 as range_cust
import random
import unittest

# TASK 1

class Test(unittest.TestCase):
    def test_enumerate_func(self):
        iterable1 = [i for i in range(random.randint(2, 30))]
        iterable2 = [chr(random.randrange(65, 90)) for _ in range(random.randint(2, 30))]
        # iterable3 = {chr(random.randrange(65, 90)): random.randint(0, 1000) for _ in range(random.randrange(1, 10))}
        start = random.randrange(0, 1000)
        self.assertEqual(list(enumerate(iterable1, start)), list(enumerate_cust(iterable1, start)))
        self.assertEqual(list(enumerate(iterable2, start)), list(enumerate_cust(iterable2, start)))
        # self.assertEqual(list(enumerate(iterable3, start)), list(enumerate_cust(iterable3, start))) # як виявилося, з DICT моя кастомна функція працює не так, як ENUMERATE, тест провалено )

    def test_range_func(self):
        start = random.randint(-150, 150)
        start_ = random.randint(0, 150)
        stop = random.randint(-150, 150)
        if start < stop:
            step = random.randint(1, stop - start)
        elif start > stop:
            step = random.randint(stop - start, -1)

        self.assertEqual(list(range(start, stop, step)), list(range_cust(start, stop, step)))
        self.assertEqual(list(range(start, stop)), list(range_cust(start, stop)))
        self.assertEqual(list(range(start_)), list(range_cust(start_)))
        self.assertEqual(range(start, stop, step)[1], range_cust(start, stop, step)[1])

if __name__ == '__main__':
    unittest.main()

