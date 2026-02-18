from django.core.management.base import BaseCommand
from faker import Faker
import random
import io
from django.core.files.images import ImageFile
from apps.shop.models import Product, Category

faker = Faker()
Status = ['sold', 'new', 'in_stock']
Size = ['small', 'medium', 'large', 'extra_large']
category = list(Category.objects.all())


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in shop_items_data:
            Title = i.get('Title').replace('.', '')
            Slug = '-'.join(Title.split())
            preview_bytes = io.BytesIO(i.get('Preview'))
            Image = ImageFile(preview_bytes, f'{Slug}.jpg')

            new_products = Product.objects.create(
                Title=i['Title'],
                Price=i['Price'],
                Sale_percent=i['Sale_percent'],
                Preview=Image,
                Status=i['Status'],
                Quantity=i['Quantity'],
                Short_description=i['Short_description'],
                Slug=Slug,
                Size=i['Size'],
                Sold=i['Sold']
            )
            new_products.category.set(i['Category'])
            new_products.save()


shop_items_data = [
    {'Title': faker.sentence(2),
     'Price': random.randint(20, 1200),
     'Short_description': faker.sentence(20),
     'Sale_percent': round(random.uniform(0, 80), 0),
     'Preview': faker.image(),
     'Quantity': random.randint(0, 900),
     'Sold': random.randint(0, 100),
     'Status': random.choice(Status),
     'Category': {random.choice(category), random.choice(category)},
     'Size': random.choice(Size)
     } for _ in range(15)
]
