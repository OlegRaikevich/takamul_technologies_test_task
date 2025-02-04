import pytest

@pytest.mark.api
def test_create_form(api_client):
    payload = {
        "title": "Test Form",
        "description": "This is a test form",
        "questions": [
            {"id": "123", "type": "text", "question": "What is your name?"},
            {"id": "124", "type": "email", "question": "Enter your email"},
        ]
    }
    
    response = api_client.post("/forms", data=payload, headers={"Content-Type": "application/json"})
    
    assert response.status == 201, f"Unexpected status code: {response.status}"
    assert response.json()["id"] is not None