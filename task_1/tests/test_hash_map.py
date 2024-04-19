import unittest
from ..main import HashMap


class TestHashMap(unittest.TestCase):

    def setUp(self) -> None:
        self.hash_map = HashMap()
        self.hash_map.add('Tom', 'Hello!')
        self.hash_map.add('Bob', 'Hi there!')
        self.hash_map.add('Kate', 'Good morning!')
        self.hash_map.add('Jane', 'Good afternoon!')
        self.hash_map.put('Bob', 'Aloha!')

    def test_add(self) -> None:
        self.hash_map.add('Alice', 'Good evening!')
        self.assertEqual(self.hash_map.get('Alice'), 'Good evening!')

    def test_put(self) -> None:
        self.hash_map.put('Tom', 'Hey!')
        self.assertEqual(self.hash_map.get('Tom'), 'Hey!')

    def test_get_existing_key(self) -> None:
        self.assertEqual(self.hash_map.get('Tom'), 'Hello!')

    def test_get_non_existing_key(self) -> None:
        self.assertIsNone(self.hash_map.get('John'))

    def test_get_default_value(self) -> None:
        self.assertEqual(self.hash_map.get('John', 'Value not exists'), 'Value not exists')

    def test_get_with_default(self) -> None:
        self.assertEqual(self.hash_map.get('John', 'Oops!'), 'Oops!')

    def test_delete_existing_key(self) -> None:
        self.assertTrue(self.hash_map.delete('Kate'))
        self.assertIsNone(self.hash_map.get('Kate'))

    def test_delete_non_existing_key(self) -> None:
        self.assertFalse(self.hash_map.delete('John'))
