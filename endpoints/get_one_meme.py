import requests
import json_schemas
from endpoints.endpoint import Endpoint


class GetOneMeme(Endpoint):
    response_json_schema = json_schemas.get_one_meme_response_json_schema

    def get_one_meme(self, token=None, meme_id=None):
        self.meme_id = meme_id if meme_id else self.meme_id
        self.headers.pop('Authorization', None)
        if token:
            authorization = {"Authorization": None} if token == ' ' else {"Authorization": token}
            self.headers.update(authorization)
        self.response = requests.get(
            url=f'{self.url}/meme/{self.meme_id}',
            headers=self.headers
        )
        return self.response

    def compare_request_and_response_meme_id(self):
        assert self.response.json()['id'] == self.meme_id, \
            (f'Returned meme ID {self.response.json()["id"]} {type(self.response.json()["id"])}'
             f' while expected {self.meme_id} {type(self.meme_id)}')

    def check_meme_after_deletion(self, meme=None):
        self.meme_id = meme.json()['id'] if meme else None
        actual_status_code = requests.get(f'{self.url}/meme/{self.meme_id}', headers=self.headers).status_code
        assert actual_status_code == 404, f'Returned status code {actual_status_code} while expected 404'

    def check_meme_by_id_after_creation(self, meme_id=None):
        meme_id = meme_id if meme_id else self.meme_id
        response = requests.get(f'{self.url}/meme/{self.meme_id}', headers=self.headers)
        assert meme_id in response.json()['id'], f'Failed to find {meme_id} in memes list {response.json()["id"]}'
