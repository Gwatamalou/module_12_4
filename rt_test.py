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
            logging.error(msg='Неверная скорость для Runner', exc_info=True)

    # def test_run(self):
    #     r2 = r.Runner('name2')
    #     for _ in range(10):
    #         r2.run()
    #     self.assertEqual(r2.distance, 100)
    #
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
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        format='%(asctime)s | %(levelname)s | %(message)s')