import unittest
from logic import measure_ping

class TestPingFunction(unittest.TestCase):
    def test_successful_ping(self):
        # Проверяем, возвращает ли функция значение пинга (не None)
        result = measure_ping()
        self.assertIsNotNone(result)
        self.assertGreater(result, 0)

    def test_failed_ping(self):
        # Проверяем, что функция возвращает None при ошибке
        result = measure_ping(host='invalid_host', port=80)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

