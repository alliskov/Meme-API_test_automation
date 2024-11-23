from jsonschema import validate, ValidationError


class Endpoint:
    url = 'http://167.172.172.115:52355'
    headers = {'Content-Type': 'application/json'}
    payload = None
    response = None
    status_code = None
    first_user_token = None
    response_json_schema = None
    meme_id = None

    def check_response_status_code(self, status_code):
        assert self.response.status_code == status_code, \
            f'Returned status code {self.response.status_code} while expected {status_code}'

    def check_response_json_schema(self):
        try:
            validate(instance=self.response.json(), schema=self.response_json_schema)
            assert True
        except ValidationError as error:
            assert False, f'JSON schema validation failed: {error.message}'
