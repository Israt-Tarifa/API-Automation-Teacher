import requests
from utils.config import BASE_URL
from utils.helper_functions import create_teacher, get_all_teachers, update_teacher, delete_teacher
def test_update_teacher(auth_headers, teacher_payload):
    post = create_teacher(BASE_URL, teacher_payload, auth_headers)

    assert post.status_code in [200, 201]

    teacher_id = post.json()["teacherId"]

    updated_payload = teacher_payload.copy()
    updated_payload["name"] = "Updated Teacher"

    # IMPORTANT FIX
    updated_payload.pop("teacherId", None)
    updated_payload.pop("id", None)

    response = requests.put(
        f"{BASE_URL}/api/teacher/{teacher_id}",
        json=updated_payload,
        headers=auth_headers
    )
    print(response.status_code)
    print(response.text)

    assert response.status_code == 200