import pytest
from jsonplaceholder_api_client import JsonPlaceholderApiClient

@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def api_client(base_url):
    return JsonPlaceholderApiClient(base_url=base_url)