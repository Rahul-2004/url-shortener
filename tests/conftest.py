import pytest
from app.main import app as flask_app

@pytest.fixture()
def client():
    with flask_app.test_client() as c:
        yield c
