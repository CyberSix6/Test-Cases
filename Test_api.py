import pytest
import requests


def test_example_api_call():
    api_url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(api_url)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.headers['Content-Type'] == "application/json; charset=utf-8", \
        f"Expected Content-Type 'application/json; charset=utf-8', but got {response.headers['Content-Type']}"
        
    data = response.json()
    assert len(data) == 100, f"Expected 100 posts, but got {len(data)}"
    for post in data:
        assert all(key in post for key in ['id', 'userId', 'title', 'body']), \
            f"Post is missing some keys: {post}"

