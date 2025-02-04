import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    client = APIClient(base_url="https://seeu-apiqa.takamulstg.com/api/")
    yield client
    client.close()