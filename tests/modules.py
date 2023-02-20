from core.modules.modules import read_config, read_json
from unittest import TestCase


class TestModules(TestCase):

    def test_read_config(self) -> None:
        self.assertEqual(first=read_config('data', 'GS'),
                         second=r'C:\Users\evgenyp\PycharmProjects\FlightComputer\core\data\data.json')

    def test_read_json(self) -> None:
        json_data = read_json('data', 'GS')
        expected = set(json_data)
        self.assertEqual(first=expected,
                         second={'distance', 'speed', 'GS'})
