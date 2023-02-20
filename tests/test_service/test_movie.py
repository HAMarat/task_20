import pytest
from unittest.mock import MagicMock

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(id=1, title='text_1', description='text_1',
               trailer='link', year=2001, rating=10, genre_id=1, director_id=1)
    m2 = Movie(id=2, title='text_2', description='text_2',
               trailer='link', year=2002, rating=10, genre_id=2, director_id=2)
    m3 = Movie(id=3, title='text_3', description='text_3',
               trailer='link', year=2003, rating=10, genre_id=3, director_id=3)

    movie_dao.get_one = MagicMock(return_value=m1)
    movie_dao.get_all = MagicMock(return_value=[m1, m2, m3])
    movie_dao.create = MagicMock(return_value=m1)
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock(return_value=m3)

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            'id': 1,
            'title': 'text_1',
            'description': 'text_1',
            'trailer': 'link',
            'year': 2001,
            'rating': 10,
            'genre_id': 1,
            'director_id': 1
        }

        movie = self.movie_service.create(movie_d)

        assert movie is not None

    def test_delete(self):
        movie = self.movie_service.delete(1)

        assert movie is None

    def test_partially_update(self):
        movie_d = {
            'id': 1,
            'title': 'text_1',
            'description': 'text_1',
            'trailer': 'link',
            'year': 2001,
            'rating': 10,
            'genre_id': 1,
            'director_id': 1
        }

        movie = self.movie_service.get_one('mid')
        if 'name' in movie_d:
            movie.title = movie_d.get("title")

        assert movie.title == 'text_1'

    def test_update(self):
        movie_d = {
            'id': 1,
            'title': 'text_1',
            'description': 'text_1',
            'trailer': 'link',
            'year': 2001,
            'rating': 10,
            'genre_id': 1,
            'director_id': 1
        }

        self.movie_service.update(movie_d)
