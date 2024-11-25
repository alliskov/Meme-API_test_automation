import requests
import json_schemas
from endpoints.endpoint import Endpoint


class AuthorizeUser(Endpoint):
    user_name = None
    response_json_schema = json_schemas.authorize_response_json_schema

    def authorize_new_user(self, user_name):
        try:
            self.payload = user_name
            self.response = requests.post(
                url=f'{self.url}/authorize',
                headers=self.headers,
                json=self.payload
            )
            self.user_name = self.response.json()['user']
            self.token = self.response.json()['token']
            return self.response
        except requests.exceptions.JSONDecodeError as error:
            print(f'\n Authorize error: {error.response}')
            return self.response

    def check_response_user_name(self, user_name):
        assert self.user_name == user_name['name'], \
            f'Returned user name {self.user_name} while expected {user_name["name"]}'
