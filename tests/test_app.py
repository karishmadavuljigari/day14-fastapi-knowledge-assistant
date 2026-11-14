
import re

from fastapi.testclient import TestClient

from src.main import app, templates


client = TestClient(app)


def get_csrf_token():
    """Open the homepage and extract its CSRF token."""
    response = client.get("/")

    match = re.search(
        r'name="csrf_token"\s+value="([^"]+)"',
        response.text,
    )

    assert match is not None, "CSRF token was not found"

    return match.group(1)


def test_homepage_loads():
    response = client.get("/")

    assert response.status_code == 200
    assert "Knowledge Assistant" in response.text
    assert 'name="csrf_token"' in response.text


def test_valid_csrf_token_allows_question():
    token = get_csrf_token()

    response = client.post(
        "/ask",
        data={
            "question": "What is the leave policy?",
            "csrf_token": token,
        },
    )

    assert response.status_code == 200
    assert "What is the leave policy?" in response.text
    assert "Answer" in response.text


def test_invalid_csrf_token_is_rejected():
    get_csrf_token()

    response = client.post(
        "/ask",
        data={
            "question": "Test question",
            "csrf_token": "invalid-token",
        },
    )

    assert response.status_code == 403


def test_script_tag_is_escaped():
    token = get_csrf_token()

    payload = '<script>alert("XSS")</script>'

    response = client.post(
        "/ask",
        data={
            "question": payload,
            "csrf_token": token,
        },
    )

    assert response.status_code == 200
    assert "&lt;script&gt;" in response.text
    assert "<script>" not in response.text


def test_css_file_loads():
    response = client.get("/static/css/style.css")

    assert response.status_code == 200
    assert ":focus-visible" in response.text


def test_security_headers_and_autoescaping():
    response = client.get("/")

    assert "Content-Security-Policy" in response.headers
    assert templates.env.autoescape("answer.html") is True
