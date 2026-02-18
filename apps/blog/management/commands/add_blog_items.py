from django.core.management.base import BaseCommand
from faker import Faker
from apps.blog.models import BlogTag, BlogItem, Category
import random
from django.core.files.images import ImageFile
import io

faker = Faker()

blog_tags = BlogTag.objects.all()
category = Category.objects.all()


class Command(BaseCommand):
    def handle(self, *args, **options):
        for item in blog_items_data:
            Title = item.get('Title').replace('.', '')
            Slug = '-'.join(Title.split())
            preview_bytes_slider = io.BytesIO(item['Slider'])
            preview_bytes_image = io.BytesIO(item['Image'])
            preview_slider = ImageFile(preview_bytes_slider, f'{Slug}.jpg')
            preview_image = ImageFile(preview_bytes_image, f'{Slug}.jpg')
            new_post = BlogItem.objects.create(
                Title=Title,
                Short_description=item['Short_description'],
                Author=item['Author'],
                Slug=Slug,
                Slider=preview_slider,
                Image=preview_image,
                Full_description=item['Full_description']
            )
            new_post.Tag.add(*item['Tag'])
            new_post.Category.add(*item['Category'])
            new_post.save()


blog_items_data = [{
    'Title': faker.sentence(6),
    'Short_description': faker.sentence(10),
    'Full_description': faker.sentence(20),
    'Author': faker.name(),
    'Slider': faker.image(),
    'Image': faker.image(),
    'Tag': [random.choice(blog_tags) for _ in range(random.randint(1, len(blog_tags)-1))],
    'Category': [random.choice(category) for _ in range(random.randint(0, len(category)-1))]
    }
    for _ in range(10)
]

