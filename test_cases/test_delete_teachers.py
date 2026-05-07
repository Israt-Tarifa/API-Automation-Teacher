import requests
from utils.config import BASE_URL
from utils.helper_functions import (
    create_teacher,
    get_teacher_by_id,
    delete_teacher
)

def create_sample_teacher(auth_headers, teacher_payload):
    response = create_teacher(BASE_URL, teacher_payload, auth_headers)
    assert response.status_code in [200, 201], \
        f"Teacher creation failed: {response.text}"

    return response.json()["teacherId"]


def test_delete_teacher_by_id(auth_headers, teacher_payload):
    teacher_id = create_sample_teacher(auth_headers, teacher_payload)
    print(f"Created teacher: {teacher_id}")

    delete_response = delete_teacher(BASE_URL, teacher_id, auth_headers)
    assert delete_response.status_code in [200, 204], \
        f"Delete failed: {delete_response.text}"

    print(f"Deleted teacher: {teacher_id}")

    get_response = get_teacher_by_id(BASE_URL, teacher_id, auth_headers)
    assert get_response.status_code in [400, 404], \
        f"Teacher still exists! Status: {get_response.status_code}"


def test_delete_nonexistent_teacher(auth_headers):
    fake_id = 999999999
    response = delete_teacher(BASE_URL, fake_id, auth_headers)
    assert response.status_code == 404, \
        f"Expected 404, got {response.status_code}"


def test_delete_teacher_twice(auth_headers, teacher_payload):
    teacher_id = create_sample_teacher(auth_headers, teacher_payload)

    first_delete = delete_teacher(BASE_URL, teacher_id, auth_headers)
    assert first_delete.status_code in [200, 204], \
        f"First delete failed: {first_delete.text}"

    second_delete = delete_teacher(BASE_URL, teacher_id, auth_headers)
    assert second_delete.status_code == 404, \
        f"Second delete should be 404, got {second_delete.status_code}"


def test_delete_teacher_without_token(auth_headers, teacher_payload):
    teacher_id = create_sample_teacher(auth_headers, teacher_payload)

    response = requests.delete(f"{BASE_URL}/api/teacher/{teacher_id}")

    assert response.status_code in [401, 403], \
        f"Expected 401/403, got {response.status_code}"

    delete_teacher(BASE_URL, teacher_id, auth_headers)