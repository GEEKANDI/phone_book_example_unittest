import unittest
from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):

    def test_creat_phonebook(self):
        phonebook = Phonebook()

    def test_lookup_entry_by_name(self):
        phonebook = Phonebook()
        phonebook.add('Bob', '12345')
        self.assertEqual('12345', phonebook.lookup('Bob'))

    def test_missing_entry_raises_keyError(self):
        phonebook = Phonebook()
        with self.assertRaises(KeyError):
            phonebook.lookup('missing')

    @unittest.skip('WIP')
    def test_consistency(self):
        self.assertTrue(phonebook.is_consistent)


