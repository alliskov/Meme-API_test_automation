import pytest
import allure


# @allure.suite('Meme API')
# @allure.feature('User authorization')
# @allure.story('Positive')
# @allure.title('Authorize user with valid data')
# @allure.severity('Critical')
# def test_authorize_user(user_authorization_endpoint, user_name):
#     user_authorization_endpoint.authorize_new_user(user_name)
#     user_authorization_endpoint.check_response_status_code(200)
#     user_authorization_endpoint.check_response_user_name(user_name)
#     user_authorization_endpoint.check_response_json_schema()
#
#
# @allure.suite('Meme API')
# @allure.feature('User authorization')
# @allure.story('Negative')
# @allure.title('Authorize user with invalid data')
# @allure.severity('Major')
# @pytest.mark.parametrize('user_name', ['invalid'], indirect=True)
# def test_authorize_user_with_invalid_payload(user_authorization_endpoint, user_name):
#     user_authorization_endpoint.authorize_new_user(user_name)
#     user_authorization_endpoint.check_response_status_code(400)
#
#
# @allure.suite('Meme API')
# @allure.feature('User authorization')
# @allure.story('Negative')
# @allure.title('Authorize user without any data')
# @allure.severity('Minor')
# @pytest.mark.parametrize('user_name', ['null'], indirect=True)
# def test_authorize_user_without_payload(user_authorization_endpoint, user_name):
#     user_authorization_endpoint.authorize_new_user(user_name)
#     user_authorization_endpoint.check_response_status_code(400)
#
#
@allure.suite('Meme API')
@allure.feature('Check token status')
@allure.story('Positive')
@allure.title('Check existent token status')
@allure.severity('Major')
def test_get_status_of_valid_token(get_token_status_endpoint, first_user_token, first_user_name):
    get_token_status_endpoint.get_token_status(first_user_token)
    get_token_status_endpoint.check_response_status_code(200)
    get_token_status_endpoint.check_token_user_name(first_user_name)


@allure.suite('Meme API')
@allure.feature('Check token status')
@allure.story('Negative')
@allure.title('Check nonexistent token status')
@allure.severity('Minor')
@pytest.mark.parametrize('token', ['АбвГдЕ', '!@#$%^&*(){}<>:;,', '  `  '])
def test_get_status_of_invalid_token(get_token_status_endpoint, token):
    get_token_status_endpoint.get_token_status(token)
    get_token_status_endpoint.check_response_status_code(404)


@allure.suite('Meme API')
@allure.feature('Check token status')
@allure.story('Negative')
@allure.title('Check status without token')
@allure.severity('Minor')
def test_get_status_without_token(get_token_status_endpoint):
    get_token_status_endpoint.get_token_status()
    get_token_status_endpoint.check_response_status_code(404)


@allure.suite('Meme API')
@allure.feature('Get memes list')
@allure.story('Positive')
@allure.title('Get all memes using valid token')
@allure.severity('Critical')
def test_get_all_memes_with_valid_token(get_all_memes_endpoint, first_user_token):
    get_all_memes_endpoint.get_all_memes(first_user_token)
    get_all_memes_endpoint.check_response_status_code(200)
    get_all_memes_endpoint.check_response_json_schema()
    get_all_memes_endpoint.check_presence_of_existing_meme_in_list(first_user_token)


@allure.suite('Meme API')
@allure.feature('Get memes list')
@allure.story('Negative')
@allure.title('Get all memes using invalid token')
@allure.severity('Major')
def test_get_all_memes_with_invalid_token(get_all_memes_endpoint, random_user_token):
    get_all_memes_endpoint.get_all_memes(random_user_token)
    get_all_memes_endpoint.check_response_status_code(401)


@allure.suite('Meme API')
@allure.feature('Get memes list')
@allure.story('Negative')
@allure.title('Get all memes using empty token')
@allure.severity('Major')
def test_get_all_memes_with_empty_token(get_all_memes_endpoint, empty_token):
    get_all_memes_endpoint.get_all_memes(empty_token)
    get_all_memes_endpoint.check_response_status_code(401)


@allure.suite('Meme API')
@allure.feature('Get memes list')
@allure.story('Negative')
@allure.title('Get all memes using no token')
@allure.severity('Critical')
def test_get_all_memes_without_token(get_all_memes_endpoint, no_token):
    get_all_memes_endpoint.get_all_memes(no_token)
    get_all_memes_endpoint.check_response_status_code(401)


@allure.suite('Meme API')
@allure.feature('Get meme by id')
@allure.story('Positive')
@allure.title('Get meme by existent id using valid token')
@allure.severity('Critical')
def test_get_one_meme_by_existent_id(get_one_meme_endpoint, first_user_token, existent_meme_id):
    get_one_meme_endpoint.get_one_meme(first_user_token, existent_meme_id)
    get_one_meme_endpoint.check_response_status_code(200)
    get_one_meme_endpoint.check_response_json_schema()
    get_one_meme_endpoint.compare_request_and_response_meme_id()


@allure.suite('Meme API')
@allure.feature('Get meme by id')
@allure.story('Negative')
@allure.title('Get meme by nonexistent id')
@allure.severity('Minor')
def test_get_one_meme_by_nonexistent_id(get_one_meme_endpoint, first_user_token, nonexistent_id):
    get_one_meme_endpoint.get_one_meme(first_user_token, nonexistent_id)
    get_one_meme_endpoint.check_response_status_code(404)


@allure.suite('Meme API')
@allure.feature('Get meme by id')
@allure.story('Negative')
@allure.title('Get meme by invalid id')
@allure.severity('Minor')
@pytest.mark.parametrize('meme_id', ['АбвГдЕ', '!@#$%^&*(){}<>:;,', '  `  '])
def test_get_one_meme_by_invalid_id(get_one_meme_endpoint, first_user_token, meme_id):
    get_one_meme_endpoint.get_one_meme(first_user_token, meme_id)
    get_one_meme_endpoint.check_response_status_code(404)


@allure.suite('Meme API')
@allure.feature('Get meme by id')
@allure.story('Negative')
@allure.title('Get meme by empty id')
@allure.severity('Minor')
def test_get_one_meme_by_empty_id(get_one_meme_endpoint, first_user_token, empty_meme_id):
    get_one_meme_endpoint.get_one_meme(first_user_token, empty_meme_id)
    get_one_meme_endpoint.check_response_status_code(404)


@allure.suite('Meme API')
@allure.feature('Get meme by id')
@allure.story('Negative')
@allure.title('Get meme using invalid token')
@allure.severity('Minor')
def test_get_one_meme_with_invalid_token(get_one_meme_endpoint, random_user_token, existent_meme_id):
    get_one_meme_endpoint.get_one_meme(random_user_token, existent_meme_id)
    get_one_meme_endpoint.check_response_status_code(401)


@allure.suite('Meme API')
@allure.feature('Get meme by id')
@allure.story('Negative')
@allure.title('Get meme using no token')
@allure.severity('Minor')
def test_get_one_meme_without_token(get_one_meme_endpoint):
    get_one_meme_endpoint.get_one_meme()
    get_one_meme_endpoint.check_response_status_code(401)


@allure.suite('Meme API')
@allure.feature('Delete meme')
@allure.story('Positive')
@allure.title('Delete own meme using valid token')
@allure.severity('Critical')
def test_delete_existent_meme(new_meme, delete_meme_endpoint, get_one_meme_endpoint, first_user_token):
    delete_meme_endpoint.delete_meme(first_user_token, new_meme)
    delete_meme_endpoint.check_response_status_code(200)
    delete_meme_endpoint.check_response_text_id()
    get_one_meme_endpoint.check_meme_after_deletion(new_meme)


@allure.suite('Meme API')
@allure.feature('Delete meme')
@allure.story('Negative')
@allure.title('Delete other user\'s meme using valid token')
@allure.severity('Major')
def test_delete_meme_added_by_other_user(new_meme, delete_meme_endpoint, get_one_meme_endpoint, second_user_token):
    delete_meme_endpoint.delete_meme(second_user_token, new_meme)
    delete_meme_endpoint.check_response_status_code(403)


@allure.suite('Meme API')
@allure.feature('Delete meme')
@allure.story('Negative')
@allure.title('Delete nonexistent meme using valid token')
@allure.severity('Minor')
def test_delete_nonexistent_meme(delete_meme_endpoint, first_user_token, nonexistent_id):
    delete_meme_endpoint.delete_meme(first_user_token, nonexistent_id)
    delete_meme_endpoint.check_response_status_code(404)


@allure.suite('Meme API')
@allure.feature('Delete meme')
@allure.story('Negative')
@allure.title('Delete request without meme_id')
@allure.severity('Major')
def test_delete_without_meme_id(delete_meme_endpoint, first_user_token):
    delete_meme_endpoint.delete_meme(first_user_token)
    delete_meme_endpoint.check_response_status_code(404)


@allure.suite('Meme API')
@allure.feature('Delete meme')
@allure.story('Negative')
@allure.title('Delete own meme using invalid token')
@allure.severity('Major')
def test_delete_meme_with_invalid_token(delete_meme_endpoint, random_user_token):
    delete_meme_endpoint.delete_meme(random_user_token)
    delete_meme_endpoint.check_response_status_code(401)


@allure.suite('Meme API')
@allure.feature('Delete meme')
@allure.story('Negative')
@allure.title('Delete own meme using no token')
@allure.severity('Major')
def test_delete_meme_without_token(delete_meme_endpoint):
    delete_meme_endpoint.delete_meme()
    delete_meme_endpoint.check_response_status_code(401)


@allure.suite('Meme API')
@allure.feature('Add meme')
@allure.story('Positive')
@allure.title('Add new meme using valid data')
@allure.severity('Critical')
def test_add_meme(add_meme_endpoint, payload, first_user_token, first_user_name):
    add_meme_endpoint.add_meme(payload, first_user_token)
    add_meme_endpoint.check_response_status_code(200)
    add_meme_endpoint.check_response_json_schema()
    add_meme_endpoint.compare_payload_and_meme_data()
    add_meme_endpoint.check_meme_got_id_after_creation()
    add_meme_endpoint.check_author_name(first_user_name)
    add_meme_endpoint.clear_test_data()


@allure.suite('Meme API')
@allure.feature('Add meme')
@allure.story('Negative')
@allure.title('Add new meme using invalid payload')
@allure.severity('Major')
@pytest.mark.parametrize('payload', [{"one": "two"}], indirect=True)
def test_add_meme_with_invalid_payload(new_meme, payload, add_meme_endpoint):
    add_meme_endpoint.check_response_status_code(400)


@allure.suite('Meme API')
@allure.feature('Add meme')
@allure.story('Negative')
@allure.title('Add new meme using no payload')
@allure.severity('Major')
@pytest.mark.parametrize('payload', ['no_payload'], indirect=True)
def test_add_meme_without_payload(new_meme, payload, add_meme_endpoint):
    add_meme_endpoint.check_response_status_code(400)


@allure.suite('Meme API')
@allure.feature('Add meme')
@allure.story('Negative')
@allure.title('Add new meme using invalid token')
@allure.severity('Major')
@pytest.mark.parametrize("first_user_token", ['invalid_token'], indirect=True)
def test_add_meme_with_invalid_token(new_meme, add_meme_endpoint, first_user_token):
    add_meme_endpoint.check_response_status_code(401)


@allure.suite('Meme API')
@allure.feature('Add meme')
@allure.story('Negative')
@allure.title('Add new meme using no token')
@allure.severity('Major')
@pytest.mark.parametrize("first_user_token", ['no_token'], indirect=True)
def test_add_meme_without_token(new_meme, add_meme_endpoint, first_user_token):
    add_meme_endpoint.check_response_status_code(401)


@allure.suite('Meme API')
@allure.feature('Update meme')
@allure.story('Positive')
@allure.title('Update own meme using valid data')
@allure.severity('Critical')
def test_update_own_existent_meme(new_meme, update_meme_endpoint, update_payload, first_user_token, first_user_name):
    update_meme_endpoint.update_meme(update_payload, new_meme, first_user_token)
    update_meme_endpoint.check_response_status_code(200)
    update_meme_endpoint.check_response_json_schema()
    update_meme_endpoint.check_response_body_equal_to_payload(update_payload)
    update_meme_endpoint.check_author_name_after_update(first_user_name)


@allure.suite('Meme API')
@allure.feature('Update meme')
@allure.story('Negative')
@allure.title('Update other user\'s meme using valid data')
@allure.severity('Major')
def test_update_other_users_existent_meme(new_meme, update_meme_endpoint, update_payload, second_user_token):
    update_meme_endpoint.update_meme(update_payload, new_meme, second_user_token)
    update_meme_endpoint.check_response_status_code(403)
    update_meme_endpoint.check_unauthorized_update_response_text()


@allure.suite('Meme API')
@allure.feature('Update meme')
@allure.story('Negative')
@allure.title('Update nonexistent meme')
@allure.severity('Minor')
def test_update_nonexistent_meme(nonexistent_id, update_meme_endpoint, update_payload, first_user_token):
    update_meme_endpoint.update_meme(update_payload, nonexistent_id, first_user_token)
    update_meme_endpoint.check_response_status_code(404)


@allure.suite('Meme API')
@allure.feature('Update meme')
@allure.story('Negative')
@allure.title('Update meme using no token')
@allure.severity('Major')
@pytest.mark.parametrize("user_token", ['no_token'])
def test_update_meme_without_token(new_meme, update_meme_endpoint, update_payload, user_token):
    update_meme_endpoint.update_meme(update_payload, new_meme, user_token)
    update_meme_endpoint.check_response_status_code(401)


@allure.suite('Meme API')
@allure.feature('Update meme')
@allure.story('Negative')
@allure.title('Update meme using invalid payload')
@allure.severity('Major')
@pytest.mark.parametrize('update_payload', [{"one": "two"}], indirect=True)
def test_update_own_meme_with_invalid_payload(new_meme, update_meme_endpoint, update_payload, first_user_token):
    update_meme_endpoint.update_meme(update_payload, new_meme, first_user_token)
    update_meme_endpoint.check_response_status_code(400)
