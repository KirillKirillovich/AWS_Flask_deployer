import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_return_content(client):
    rv = client.get('/')
    assert rv.status_code == 200 or rv.status_code == 404


def test_return_logs(client):
    rv = client.get('logs')
    assert rv.status_code == 200


def test_return_status(client):
    rv = client.get('/status')
    assert rv.status_code == 200
