from django.test import TestCase
import random
# Create your tests here.

def formatted_id_number(number):
    number_length = len(number)
    my_number = list(str(number))
    my_new_list = ['0','0','0']

    if number_length ==1:
        my_new_list[2] = my_number[0]
        
    if number_length == 2:
        my_new_list[2] = my_number[1]
        my_new_list[1] = my_number[0]
    if number_length == 3:
        my_new_list[0] = my_number[0]
        my_new_list[1] = my_number[1]
        my_new_list[2] = my_number[2]
        
    result = "".join(my_new_list) 
    
    return result
class RabbitTestCase(TestCase):
    
    def setUp(self):
        print("Testing Rabbit tag string format")
    
    def test_formatted_id_number(self):    
        num = str(random.randint(1,101))
        print("ALEATORY:", num)
        self.assertTrue(isinstance(formatted_id_number(num),str))
        print("TEST PASSED:", formatted_id_number(num))
        self.assertEqual(len(formatted_id_number(num)),3) 
    def test_correct_status_and_page_content(self):
        response = self.client.get("//add-rabbit")
        self.assertEqual(response.status_code, 200)
        
        