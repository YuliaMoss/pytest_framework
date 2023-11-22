import random
import pytest
from faker import Faker
from api_collections.dataclasses.notes_dataclass import NotesData
from api_collections.notes_api import NotesApi
from api_collections.users_api_notes import UsersApi

fake = Faker()


def generate_random_password():
    while True:
        password = str(fake.random_number(digits=10))
        if 6 <= len(password) <= 30:
            return password


@pytest.fixture()
def get_fake_user_payload():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "password": generate_random_password()
    }


@pytest.fixture()
def get_fake_invalid_user_payload_invalid_password():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "password": random.randint(0, 99999)
    }


@pytest.fixture()
def get_fake_user_payload_invalid_email():
    return {
        "name": fake.name(),
        "email": fake.word(),
        "password": generate_random_password()
    }


@pytest.fixture()
def get_user_payload_for_login():
    return {
        "email": "justinrios@example.net",
        "password": "7813909141"
    }


@pytest.fixture()
def get_invalid_user_email_for_login():
    return {
        "email": "justinrios",
        "password": "7813909141"
    }


@pytest.fixture()
def get_invalid_user_password_for_login():
    return {
        "email": "justinrios@example.net",
        "password": random.randint(0, 99999)
    }


@pytest.fixture
def updated_profile_data():
    return {
        "phone": str(random.randint(0, 99999999)),
        "name": fake.name(),
        "company": fake.word()
    }


@pytest.fixture
def updated_profile_data_without_name():
    # Створіть фікстуру з даними користувача, де відсутнє поле 'name'
    return {
        "phone": str(random.randint(0, 99999999)),
        "company": fake.word()
    }


@pytest.fixture
def authenticated_user_api(get_user_payload_for_login):
    payload = get_user_payload_for_login
    resp = UsersApi().post_login_users(user_data=payload)
    new_headers_info = resp.json()
    assert new_headers_info

    users_api = UsersApi()
    current_headers = users_api.get_headers()

    new_token = new_headers_info['data'].get('token', None)
    assert new_token, "Token not found in new_headers_info"

    updated_headers = {**current_headers, 'x-auth-token': new_token}
    users_api.update_headers(updated_headers)

    return users_api, updated_headers


@pytest.fixture()
def get_fake_note_payload():
    return {
        "title": fake.sentence(5),
        "description": fake.sentence(15),
        "category": random.choice(['Home', 'Work', 'Personal'])
    }


@pytest.fixture()
def get_new_note_id(get_fake_note_payload):
    resp = NotesApi().post_new_note(note_data=get_fake_note_payload)
    return resp.json().get('data')['id']


@pytest.fixture()
def get_mock_note_by_id():
    def __inner(note_id):
        resp = NotesApi().get_note_by_id(note_id=note_id)  # like data from DB
        return NotesData(**resp.json().get('data'))

    return __inner
