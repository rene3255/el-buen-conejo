from unittest import TestCase
    
    
class TestFormattedNumber(TestCase):
  
    def setUp(self):
        print("Testing IdFormattedTestCase")
        number = 3
    
    def test_id_formatted(self):
        self.assertEqual(self.number,"003")
        