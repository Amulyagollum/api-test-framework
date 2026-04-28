from utils.api_client import get

def test_get_posts_status_code():
    response = get('posts')

    assert response.status_code ==200


def test_invalid_posts_status_code():
    response = get("invalid-posts")

    assert response.status_code == 404

def test_response_structure_posts():
    response = get("posts")
    data = response.json()

    assert "userId" in data[0]
    assert "title"  in data[0]