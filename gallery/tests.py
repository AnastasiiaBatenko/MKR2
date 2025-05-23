from django.test import TestCase
from .models import Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime

class CategoryModelTest(TestCase):
    def test_str(self):
        category = Category.objects.create(name='Nature')
        self.assertEqual(str(category), 'Nature')


class ImageModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Portrait')

    def test_image_creation(self):
        test_image = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
        image = Image.objects.create(
            title="Sample",
            image=test_image,
            created_date=datetime.date.today(),
            age_limit=18
        )
        image.categories.add(self.category)
        self.assertEqual(str(image), "Sample")
        self.assertEqual(image.categories.count(), 1)
