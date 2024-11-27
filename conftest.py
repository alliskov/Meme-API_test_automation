import pytest
import random
import allure
import json
import os
import jsonschema
import json_schemas
from faker import Faker
from endpoints.authorize_user import AuthorizeUser
from endpoints.get_token_status import GetToken
from endpoints.get_all_memes import GetAllMemes
from endpoints.get_one_meme import GetOneMeme
from endpoints.add_meme import AddMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.update_meme import UpdateMeme

fake_latin = Faker('en_US')
fake_cyrillic = Faker('ru_RU')
token = []


@pytest.fixture()
def get_token_status_endpoint():
    return GetToken()


@pytest.fixture()
def user_authorization_endpoint():
    return AuthorizeUser()


@pytest.fixture()
def get_all_memes_endpoint():
    return GetAllMemes()


@pytest.fixture()
def get_one_meme_endpoint():
    return GetOneMeme()


@pytest.fixture()
def add_meme_endpoint():
    return AddMeme()


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()


@pytest.fixture()
def update_meme_endpoint():
    return UpdateMeme()


@pytest.fixture()
def random_user_name_latin():
    return fake_latin.first_name()


@pytest.fixture()
def random_user_name_cyrillic():
    return fake_cyrillic.first_name()


@pytest.fixture()
def user_name(request):
    name = getattr(request, 'param', None)
    if name == 'null':
        name = {"name": None}
    elif name == 'invalid':
        name = {"one": "two"}
    else:
        name = {"name": fake_latin.user_name()}
    return name


@pytest.fixture()
def random_user_token():
    for _ in range(15):
        token.append(random.choice([''.join(fake_latin.random_letters(1)),
                                    str(fake_cyrillic.random_number(1)),
                                    '!', '@', '#', '$', '%', '^', '&']))
    return ''.join(token)


@pytest.fixture()
def existent_meme_id():
    return random.randint(1, 50)


@pytest.fixture()
def nonexistent_id():
    nonexistent_id = fake_latin.random_number(15)
    return nonexistent_id


@pytest.fixture()
def empty_meme_id():
    return ' '


@pytest.fixture()
def first_user_name(authorize_user):
    user1, _ = authorize_user
    name = user1['user']
    return name


@pytest.fixture()
def second_user_name(authorize_user):
    _, user2 = authorize_user
    name = user2['user']
    return name


@pytest.fixture()
def first_user_token(authorize_user, request):
    custom_token = getattr(request, 'param', None)
    if custom_token:
        token = None if custom_token == 'no_token' else custom_token
    else:
        user1, _ = authorize_user
        token = user1["token"]
    return token


@pytest.fixture()
def second_user_token(authorize_user):
    _, user2 = authorize_user
    token = user2["token"]
    return token


@pytest.fixture()
def empty_token():
    return ' '


@pytest.fixture()
def no_token():
    return None


@pytest.fixture()
def payload(request):
    custom_payload = getattr(request, 'param', None)
    if not custom_payload:
        payload = {
            "info": {
                "colors": [
                    "white",
                    "blue",
                    "brown"
                ],
                "objects": [
                    "picture",
                    "text"
                ]
            },
            "tags": [
                "eyes",
                "doctor"
            ],
            "text": "-Eye doctor: Your results just came back! -Me: Can i see them? -Eye doctor: Probably not...",
            "url": "https://cdn.memes.com/up/71558571535638926/i/1731960140440.jpg"
        }
    elif custom_payload == 'no_payload':
        payload = None
    else:
        payload = custom_payload
    return payload


@pytest.fixture()
def update_payload(request, new_meme):
    custom_payload = getattr(request, 'param', None)
    new_meme_id = new_meme.json()['id']
    if not custom_payload:
        payload = {
            "id": new_meme_id,
            "info": {
                "colors": [
                    "green",
                    "yellow",
                    "orange"
                ],
                "objects": [
                    "text",
                    "gif"
                ]
            },
            "tags": [
                "dog",
                "fire",
                "coffee"
            ],
            "text": "It's fine",
            "url": "https://media.tenor.com/5ety3Lx3QccAAAAe/its-fine-dog-fine.png"
        }
    elif custom_payload == 'no_payload':
        payload = None
    else:
        payload = custom_payload
    return payload


@pytest.fixture()
def new_meme(payload, add_meme_endpoint, delete_meme_endpoint, first_user_token):
    with allure.step('Create meme'):
        add_meme_endpoint.add_meme(payload=payload, token=first_user_token)
        yield add_meme_endpoint.response
    with allure.step('Delete object'):
        delete_meme_endpoint.delete_meme(meme=add_meme_endpoint.response, token=first_user_token)


@pytest.fixture(scope='session')
def read_user_config(file_name=None):
    file_name = file_name if file_name else 'user_config.json'
    user_config_file = os.path.join(os.path.dirname(__file__), 'user_config.json')
    try:
        with open(file=user_config_file, mode='r') as user_config:
            config_data = json.load(user_config)
            jsonschema.validate(config_data, json_schemas.user_config_json_schema)
            return config_data
    except FileNotFoundError:
        print('File not found')
        return
    except json.JSONDecodeError:
        print('Read JSON error')
        return
    except jsonschema.exceptions.ValidationError:
        print('Invalid JSON file structure')
        return


def write_user_config(*args, file_name=None):
    file_name = file_name if file_name else 'user_config.json'
    user_config_file = os.path.join(os.path.dirname(__file__), 'user_config.json')
    try:
        with open(file=user_config_file, mode='w') as user_config:
            json.dump([*args], user_config, indent=4)
    except FileNotFoundError:
        print('File not found')
        return
    except PermissionError:
        print('No permission to edit file')
        return


@pytest.fixture()
def authorize_user(read_user_config,
                   user_authorization_endpoint,
                   get_token_status_endpoint,
                   ):
    try:
        if (not read_user_config or
                (get_token_status_endpoint.get_token_status(read_user_config[0]['token']).status_code != 200 or
                 get_token_status_endpoint.get_token_status(read_user_config[1]['token']).status_code != 200)):
            first_user_name = {"name": fake_latin.first_name()}
            second_user_name = {"name": fake_latin.first_name()}
            first_user = user_authorization_endpoint.authorize_new_user(first_user_name).json()
            second_user = user_authorization_endpoint.authorize_new_user(second_user_name).json()
            write_user_config(first_user, second_user)
            return first_user, second_user
        elif (get_token_status_endpoint.get_token_status(read_user_config[0]['token']).status_code == 200 and
              get_token_status_endpoint.get_token_status(read_user_config[1]['token']).status_code == 200):
            return read_user_config[0], read_user_config[1]
    except TypeError as error:
        print(f'Error while reading file: {error}')
