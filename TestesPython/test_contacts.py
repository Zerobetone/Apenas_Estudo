import unittest
from contatos import Contact

class TesteContacts(unittest.TestCase):
    def setUp(self):
        self.contact = Contact("lucas", "santiago", "88999450948", "lucassantigo@gmail.com" )

    def test_get_full_name(self):
        self.assertEqual(self.contact.get_full_name(), "lucas santiago")
    
    def test_string_representation(self):
        expected_string = "Nome: lucas santiago, Phone: 88999450948, E-mail: lucassantigo@gmail.com"
        self.assertEquals(str(self.contact), expected_string)

if __name__ == '__main__':
    unittest.main()