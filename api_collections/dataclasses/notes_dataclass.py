import random
from faker import Faker

fake = Faker()


class NotesData:
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def get_dict(self):
        return self.__dict__

    @staticmethod
    def get_fake_note_payload():
        return {
            "title": fake.sentence(5),
            "description": fake.sentence(15),
            "category": random.choice(['Home', 'Work', 'Personal'])
        }
