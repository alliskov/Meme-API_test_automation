import requests
from endpoints.endpoint import Endpoint


class AddMeme(Endpoint):
    response_json_schema = {
        "type": "object",
        "properties": {
            "id": {"type": ["integer", "string"]},
            "info": {
                "type": "object",
                "additionalProperties": True
            },
            "tags": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "text": {
                "type": "string"
            },
            "updated_by": {
                "type": "string"
            },
            "url": {
                "type": "string",
                "format": "uri"
            },
        },
        "required": ["id", "info", "tags", "text", "updated_by", "url"],
        "additionalProperties": False
    }

    def add_meme(self, payload, token=None):
        self.headers.pop('Authorization', None)
        self.payload = payload
        if token:
            authorization = {"Authorization": token}
            self.headers.update(authorization)
        try:
            self.response = requests.post(
                url=f'{self.url}/meme',
                json=payload,
                headers=self.headers
            )
            print(f'\nTest meme created with ID {self.response.json()["id"]}')
            self.meme_id = self.response.json()['id']
            return self.response
        except requests.exceptions.JSONDecodeError as error:
            self.meme_id = None
            print(f'\n Test meme creation failed {error.response}')
        finally:
            self.status_code = self.response.status_code

    def check_meme_got_id_after_creation(self):
        assert self.response.json()['id'], \
            f'Failed finding ID {self.response.json()["id"]} in response body'

    def check_author_name(self, author_name):
        assert self.response.json()['updated_by'] == author_name, \
            f'Returned author name {self.response.json()["updated_by"]} while expected {author_name}'
