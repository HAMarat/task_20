import pytest
from unittest.mock import MagicMock

from dao.model.genre import Genre
from dao.genre import GenreDAO
from service.genre import GenreService


@pytest.fixture
def genre_dao():
    genre_dao = GenreDAO(None)

    g1 = Genre(id=1, name='First')
    g2 = Genre(id=2, name='Second')
    g3 = Genre(id=3, name='Third')


