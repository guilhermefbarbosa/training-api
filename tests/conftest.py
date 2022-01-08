import pytest
from application import app


@pytest.fixture(scope='function')
def test_client():
    flask_app = app
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client
