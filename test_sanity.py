from dataclasses import dataclass
import pytest


@dataclass
class Person:

    name: str
    age: int
    id: str

    @property
    def get_name(self) -> str:
        return self.name

    @get_name.setter
    def get_name(self, new: str) -> None:
        self.name = new

    @property
    def get_age(self) -> int:
        return self.age

    @get_age.setter
    def get_age(self, new: int) -> None:
        self.age = new if new > 0 else Exception

    @property
    def get_id(self) -> str:
        return self.id

    def get_full_data(self) -> str:
        return f'persons name is {self.name}, age: {self.age}, id: {self.id}'


person = Person('jenia', 29, '123456')


@pytest.dummy
def test_person() -> None:
    assert person.get_name == 'jenia'


def test_person2() -> None:
    person.get_name = 'ilia'
    assert person.get_name == 'ilia'


def test_person_age() -> None:
    person.get_age = -5
    assert TypeError


def test_person_age2() -> None:
    person.get_age = 5
    assert person.get_age == 5


def test_data() -> None:
    assert person.get_full_data() == "persons name is ilia, age: 5, id: 123456"
