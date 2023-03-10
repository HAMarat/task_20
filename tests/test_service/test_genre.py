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

    genre_dao.get_one = MagicMock(return_value=g1)
    genre_dao.get_all = MagicMock(return_value=[g1, g2, g3])
    genre_dao.create = MagicMock(return_value=g1)
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock(return_value=g1)

    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert len(genres) > 0
        assert len(genres) == 3

    def test_create(self):
        genre_d = {
            'id': 1,
            'name': 'First',
        }
        genre = self.genre_service.create(genre_d)

        assert genre is not None

    def test_delete(self):
        genre = self.genre_service.delete(1)

        assert genre is None

    def test_partially_update(self):
        genre_d = {
            'id': 1,
            'name': 'First',
        }

        genre = self.genre_service.get_one('bid')
        if 'name' in genre_d:
            genre.name = genre_d.get("name")

        assert genre.name == 'First'

    def test_update(self):
        genre_d = {
            'id': 1,
            'name': 'First',
        }

        genre = self.genre_service.update(genre_d)

        assert genre_d.get('id') == genre.id
