import requests
import random
import json_schemas
from endpoints.endpoint import Endpoint


class GetAllMemes(Endpoint):
    response_json_schema = json_schemas.get_memes_list_response_json_schema

    def get_all_memes(self, token=None):
        self.headers.pop('Authorization', None)
        if token:
            authorization = {"Authorization": None} if token == ' ' else {"Authorization": token}
            self.headers.update(authorization)
        self.response = requests.get(
            url=f'{self.url}/meme',
            headers=self.headers
        )
        return self.response

    def check_presence_of_existing_meme_in_list(self, token=None, meme_id=None):
        meme_id = meme_id if meme_id else random.randint(1, 50)
        token = token if token else self.first_user_token
        meme = requests.get(
            url=f'{self.url}/meme/{meme_id}',
            headers={'Authorization': token}
        ).json()
        print(f'response is {self.response}')
        assert meme in self.response.json()['data'], \
            f'Failed to find meme {meme} in meme list {self.response.json()["data"]}'
