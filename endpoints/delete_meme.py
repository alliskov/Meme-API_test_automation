import requests
from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):
    meme_id = None

    def delete_meme(self, token=None, meme=None):
        try:
            self.headers.pop('Authorization', None)
            if not meme:
                self.meme_id = None
            elif type(meme) is int:
                self.meme_id = meme
            else:
                self.meme_id = meme.json()['id']
            if token:
                authorization = {"Authorization": None} if token == ' ' else {"Authorization": token}
                self.headers.update(authorization)
            self.response = requests.delete(
                url=f'{self.url}/meme/{self.meme_id}',
                headers=self.headers
            )
            if self.response.status_code == 200:
                print(f'\nTest meme ID {self.meme_id} deleted')
            else:
                print(f'\nDeletion failed with status code {self.response.status_code}')
            return self.response
        except requests.exceptions.JSONDecodeError:
            print('Failed parsing JSON')

    def check_response_text_id(self):
        assert self.response.text.split()[3] == str(self.meme_id), \
            f'Returned id {self.response.text.split()[3]} while expected {self.meme_id}'
