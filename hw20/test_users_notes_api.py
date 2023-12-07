"""1 -
Find public API with several endpoints (Can use Notes(https://practice.expandtesting.com/notes/api/api-docs/)
 or Gorest API (https://gorest.co.in/))
Add API testing to your test framework (BaseAPI, API collection)
Write several API tests (minimum 10)"""
from http import HTTPStatus
from api_collections.users_api_notes import UsersApi


# 1
def test_post_new_user(get_fake_user_payload):
    payload = get_fake_user_payload
    resp = UsersApi().post_new_users_register(user_data=payload)
    assert resp.status_code == HTTPStatus.CREATED, f'Request fail! ({resp.text})'
    user_data = resp.json()['data']
    assert user_data['name'] == payload['name']


# 2
def test_post_new_user_with_invalid_password(get_fake_invalid_user_payload_invalid_password):
    payload = get_fake_invalid_user_payload_invalid_password
    resp = UsersApi().post_new_users_register(user_data=payload)
    assert resp.status_code == HTTPStatus.BAD_REQUEST, f'Request fail! ({resp.text})'


# 3
def test_post_new_user_with_invalid_email(get_fake_user_payload_invalid_email):
    payload = get_fake_user_payload_invalid_email
    resp = UsersApi().post_new_users_register(user_data=payload)
    assert resp.status_code == HTTPStatus.BAD_REQUEST, f'Request fail! ({resp.text})'


# 4
def test_users_login(get_user_payload_for_login):
    payload = get_user_payload_for_login
    resp = UsersApi().post_login_users(user_data=payload)
    assert resp.status_code == HTTPStatus.OK, f'Request fail! ({resp.text})'


# 5
def test_users_login_invalid_email(get_invalid_user_email_for_login):
    payload = get_invalid_user_email_for_login
    resp = UsersApi().post_login_users(user_data=payload)
    assert resp.status_code == HTTPStatus.BAD_REQUEST, f'Request fail! ({resp.text})'


# 6
def test_users_login_invalid_password(get_invalid_user_password_for_login):
    payload = get_invalid_user_password_for_login
    resp = UsersApi().post_login_users(user_data=payload)
    assert resp.status_code == HTTPStatus.BAD_REQUEST, f'Request fail! ({resp.text})'


# 7
def test_get_users_profile(authenticated_user_api):
    users_api, headers = authenticated_user_api

    resp = users_api.get_users_profile(headers=headers)
    data = resp.json()

    assert data
    assert resp.status_code == HTTPStatus.OK, f'Request fail! ({resp.text})'


# 8
def test_missing_auth_token():
    users_api = UsersApi()
    resp = users_api.get_users_profile(headers={'Cookie': 'express:sess=...'})
    assert resp.status_code == HTTPStatus.UNAUTHORIZED, f'Missing x-auth-token should result in 401 Unauthorized'


# # 9
# def test_patch_user_profile(authenticated_user_api, updated_profile_data):
#     users_api, headers = authenticated_user_api

#     response = users_api.patch_user_profile(data=updated_profile_data, headers=headers)
#     data = response.json()

#     assert data
#     assert response.status_code == HTTPStatus.OK, f'Request fail! ({response.text})'


# 10
def test_patch_user_profile_without_name(authenticated_user_api, updated_profile_data_without_name):
    users_api, headers = authenticated_user_api

    updated_profile_data_without_name.pop('name', None)
    response = users_api.patch_user_profile(data=updated_profile_data_without_name, headers=headers)
    print(response.text)
    assert response.status_code == 400, f"Unexpected response code: {response.status_code}. Response content: {response.text}"

    expected_error_message = {"message": "User name must be between 4 and 30 characters", "status": 400,
                              "success": False}
    assert response.json().items() >= expected_error_message.items(), f"Expected error message not found in response"
