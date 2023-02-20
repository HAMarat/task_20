from unittest.mock import MagicMock
import pytest

from dao.model.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService


@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name='First')
    d2 = Director(id=2, name='Second')
    d3 = Director(id=3, name='Third')

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2, d3])
    director_dao.create = MagicMock(return_value=d1)
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock(return_value=d3)

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0
        assert len(directors) == 3

    def test_create(self):
        director_d = {
            'id': 1,
            'name': 'First',
        }
        director = self.director_service.create(director_d)

        assert director is not None

    def test_delete(self):
        director = self.director_service.delete(1)

        assert director is None

    def test_partially_update(self):
        director_d = {
            'id': 1,
            'name': 'First',
        }

        director = self.director_service.get_one('bid')
        if 'name' in director_d:
            director.name = director_d.get("name")

        assert director.name == 'First'

    def test_update(self):
        director_d = {
            'id': 1,
            'name': 'First'
        }

        self.director_service.update(director_d)
        director = self.director_service.get_one(1)

        assert director_d.get('id') == director.id
