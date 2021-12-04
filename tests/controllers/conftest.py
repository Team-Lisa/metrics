import pytest
from api.repositories.track_repository import TrackRepository
from api.repositories.db import DataBase


@pytest.fixture
def init():
    DataBase()
    TrackRepository.delete_all_track()
    return 0
