###########################################

#         ВНИМАНИЕ ВОПРОС
#
# логирование не работает если реализовать конструкцию
# внутри модуля rt_test, но если реализовать её в модуле
# rt_with_exceptions то всё работает. Для меня это выглядит
# максимально не логично, почему работает именно так?
#
# logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
#                         format='%(asctime)s | %(levelname)s | %(message)s')


###########################################




import rt_with_exceptions as r
import unittest
import logging


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            r1 = r.Runner('name1', -4)
            for _ in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except ValueError:
            logging.error(msg=f'Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            r2 = r.Runner(1)
            for _ in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100)
            logging.info(f'test_run" выполнен успешно')
        except:
            logging.error(msg=f'Неверный тип данных для объекта Runner', exc_info=True)




    # def test_challenge(self):
    #     r3 = r.Runner('name1')
    #     r4 = r.Runner('name2')
    #     for _ in range(10):
    #         r3.run()
    #         r4.walk()
    #
    #     self.assertNotEqual(r3.distance, r4.distance)


if __name__ == '__main__':
    unittest.main()