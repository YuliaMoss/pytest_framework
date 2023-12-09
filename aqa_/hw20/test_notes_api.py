from http import HTTPStatus
from api_collections.dataclasses.notes_dataclass import NotesData
from api_collections.notes_api import NotesApi


def test_get_all_notes():
    resp = NotesApi().get_all_notes()
    assert resp.status_code == HTTPStatus.OK, f'Request fail! ({resp.text})'
    data = resp.json()
    assert isinstance(data, dict)


# def test_post_new_note(get_fake_note_payload):
#     payload = get_fake_note_payload
#     resp = NotesApi().post_new_note(note_data=payload)
#     assert resp.status_code == HTTPStatus.OK, f'Request fail! ({resp.text})'
#     data = resp.json().get('data')
#     assert data['title'] == payload['title']
#
#
# def test_get_note_by_id(get_new_note_id, get_mock_note_by_id):
#     _id = get_new_note_id
#     # resp = NotesApi().get_note_by_id(note_id=_id)
#     resp = NotesApi().get_note_by_id(note_id=_id)
#     assert resp.status_code == HTTPStatus.OK, f'Request fail! ({resp.text})'
#     note_data = NotesData(**resp.json().get('data'))
#     actual_data_from_db = get_mock_note_by_id(_id)
#     assert note_data.get_dict() == actual_data_from_db.get_dict()


def test_post_new_note_without_title():
    payload = NotesData.get_fake_note_payload()
    payload.pop('title')
    resp = NotesApi().post_new_note(note_data=payload)
    assert resp.status_code == 400
