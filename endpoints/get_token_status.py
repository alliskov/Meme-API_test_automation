import requests
from endpoints.endpoint import Endpoint


class GetToken(Endpoint):

    def get_token_status(self, token=None):
        token = token if token else self.first_user_token
        self.response = requests.get(f'{self.url}/authorize/{token}')
        return self.response

    def check_token_user_name(self, user_name):
        assert self.response.text.split()[-1] == user_name, \
            f'Returned user name {self.response.text.split()[-1]} while expected {user_name}'
