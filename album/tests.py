from django.test import TestCase
from .models import Category,Location,Image

class CategoryTestClass(TestCase):
    def setUp(self):
        self.Football = Category(name='Football')

    def test_new_category_isinstance_of_category(self):
        self.assertTrue(isinstance(self.Football, Category))

class LocationTestClass(TestCase):
    def setUp(self):
        self.Umo = Location('Umo')

    def test_new_location_isinstance_of_location(self):
        self.assertTrue(isinstance(self.Umo, Location))

class ImageTestClass(TestCase):

    def setUp(self):
        self.new_location = Location(name='Umo')
        self.new_location.save()

        self.new_category = Category(name = 'Football')
        self.new_category.save()


      

    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    

    