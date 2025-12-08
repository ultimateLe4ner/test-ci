import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_route(client):
    """Test the hello route returns 'hello'."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'hello'


def test_hello_route_get_method_only(client):
    """Test that POST method is not allowed on the hello route."""
    response = client.post('/')
    assert response.status_code == 405  # Method Not Allowed
