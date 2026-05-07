import requests
from utils.config import BASE_URL
from utils.helper_functions import ( create_teacher,  get_all_teachers, delete_teacher)

def create_sample_teacher(auth_headers, teacher_payload):
    """Helper: safely create teacher and return response + id"""
    response = create_teacher(BASE_URL, teacher_payload, auth_headers)
    assert response.status_code in [200, 201], \
        f"Teacher creation failed: {response.text}"

    data = response.json()
    return data, data.get("_id") or data.get("teacherId")

# ---------------- CREATE TESTS ---------------- #
def test_create_teacher(auth_headers, teacher_payload):
    data, teacher_id = create_sample_teacher(auth_headers, teacher_payload)

    assert data["name"] == teacher_payload["name"]
    assert data["email"] == teacher_payload["email"]
    assert data["department"] == teacher_payload["department"]
    assert data["designation"] == teacher_payload["designation"]
    if teacher_id:
        delete_teacher(BASE_URL, teacher_id, auth_headers)


def test_created_teacher_exists_in_list(auth_headers, teacher_payload):
    data, teacher_id = create_sample_teacher(auth_headers, teacher_payload)
    get_response = get_all_teachers(BASE_URL, auth_headers)
    assert get_response.status_code == 200, \
        f"GET failed: {get_response.text}"

    emails = [t["email"] for t in get_response.json()]

    assert data["email"] in emails, \
        "Created teacher not found in list"
    if teacher_id:
        delete_teacher(BASE_URL, teacher_id, auth_headers)

# ---------------- NEGATIVE TESTS ---------------- #
def test_create_teacher_missing_name(auth_headers, teacher_payload):
    payload = teacher_payload.copy()
    payload.pop("name", None)
    response = create_teacher(BASE_URL, payload, auth_headers)
    assert response.status_code in [400, 422], \
        f"Expected validation error, got {response.status_code}"


def test_create_teacher_invalid_email(auth_headers, teacher_payload):
    payload = teacher_payload.copy()
    payload["email"] = "invalid@@email"
    response = create_teacher(BASE_URL, payload, auth_headers)

    assert response.status_code in [400, 422], \
        f"Expected validation error, got {response.status_code}"


def test_create_teacher_without_token(teacher_payload):
    response = requests.post(f"{BASE_URL}/api/teacher", json=teacher_payload)
    assert response.status_code in [401, 403], \
        f"Expected 401/403, got {response.status_code}"