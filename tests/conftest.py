import copy
import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def isolate_activities():
    """Deep-copy and restore the in-memory `activities` between tests."""
    orig = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(orig)
