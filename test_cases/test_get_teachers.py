import requests
from utils.config import BASE_URL
from utils.helper_functions import create_teacher

def test_get_all_teachers(auth_headers):
    response = requests.get(f"{BASE_URL}/api/teacher", headers=auth_headers)

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_teacher_by_id(auth_headers, teacher_payload):
    post = create_teacher(BASE_URL, teacher_payload, auth_headers)

    data = post.json()
    print("CREATE RESPONSE:", data)

    teacher_id = data["teacherId"]   # ✅ correct ID

    response = requests.get(
        f"{BASE_URL}/api/teacher/{teacher_id}",
        headers=auth_headers
    )

    assert response.status_code == 200, response.text