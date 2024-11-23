import requests
from endpoints.endpoint import Endpoint


class UpdateMeme(Endpoint):
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

    def update_meme(self, payload: dict, meme=None, token=None):
        try:
            self.headers.pop('Authorization', None)
            if not meme:
                self.meme_id = None
            elif type(meme) is int:
                self.meme_id = meme
            else:
                self.meme_id = meme.json()['id']
            if token:
                authorization = {"Authorization": token}
                self.headers.update(authorization)
            self.response = requests.put(
                url=f'{self.url}/meme/{self.meme_id}',
                json=payload,
                headers=self.headers
            )
            print(f'\nTest meme {self.response.json()["id"]} updated')
            self.meme_id = self.response.json()['id']
            return self.response
        except requests.exceptions.JSONDecodeError as error:
            self.meme_id = None
            print(f'\n Test meme update failed {error.response}')
        finally:
            self.status_code = self.response.status_code

    def check_response_body_equal_to_payload(self, payload):
        assert self.response.json() == payload, \
            f'Failed comparing response body and payload'

    def check_unauthorized_update_response_text(self):
        text = 'You are not the meme owner'
        assert text in self.response.text, 'Unexpected text message'

    def check_author_name_after_update(self, author_name):
        assert self.response.json()['updated_by'] == author_name, \
            f'Returned author name {self.response.json()["updated_by"]} while expected {author_name}'
