from django.contrib.auth import get_user_model
from django.test import TestCase

class UsersControlTest(TestCase):
# Create your tests here
    def test_create_user(self):
        User = get_user_model()
        print("value of User: ", User)
        user = User.objects.create_user(email="demo@gmail.com",password="pwdtest")
        self.assertEqual(user.email, "demo@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertNotIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="pwdtest") 
    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="ebcadmin@gmail.com", password="ebc12345")
        self.assertEqual(admin_user.email,"ebcadmin@gmail.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertNotIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="ebcadmin@gmail.com", password="pwdebc", is_superuser=False)

            
                      