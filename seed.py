from django_seed import Seed
from blog.models import Tag

seeder = Seed.seeder()

class TagSeeder:
    def __init__(self):
        self.count = 5  # Number of instances to create

    def run(self):
        seeder.add_entity(Tag, self.count, {
            'name': lambda x: seeder.faker.word()
        })

TagSeeder().run()
