import pytest

from app.calculator import Person, ValidationError

@pytest.fixture
def persons():
    p = Person(weight=70, gender="M", height=170, age=19, activity=1.55)
    p2 = Person(weight=57, gender="f", height=157, age=22, activity=1.55)
    p3 = Person(weight=70, gender="m", height=170, age=19, activity=1.55, goal='cutting')

    return p, p2, p3 

def test_valid_persons(persons):
    assert all(isinstance(person, Person) for person in persons)


def test_bmr_calc(persons):
    p, p2, p3 = persons

    assert p.bmr_calc() == 2592
    assert p2.bmr_calc() == 1984
    assert p3.bmr_calc() == 2592

    with pytest.raises(ValidationError, match="Peso fora do intervalo permitido"):
        Person(weight=301, gender="m", height=170, age=19, activity=1.55)

    with pytest.raises(ValidationError, match="Peso fora do intervalo permitido"):
        Person(weight=-1, gender="m", height=170, age=19, activity=1.55)

def test_water_calc(persons):
    p, p2, p3 = persons

    assert p.water_calc() == 2450
    assert p2.water_calc() == 1995
    assert p3.water_calc() == 2450
    
    with pytest.raises(ValidationError, match="Idade fora do intervalo permitido"):
        Person(weight=57, gender="f", height=158, age=121, activity=1.55)

    with pytest.raises(ValidationError, match="Idade fora do intervalo permitido"):
        Person(weight=57, gender="f", height=158, age=-1, activity=1.55)

def test_summary(persons):
    p, p2, p3 = persons

    assert p.summary() == {
        "bmr": {"base": 2592, "goal": 2592},
        "nutrients": {"proteins": 194, "fat": 101, "carbs": 227},
        "water": {"ml": 2450, "l": 2.45},
        "bmi": {"index": 24.2, "health": "Peso ideal"},
    }
    assert p2.summary()["bmr"] == {"base": 1984, "goal": 1984}
    assert p3.summary()["bmr"] == {"base": 2592, "goal": 1992}

    with pytest.raises(ValidationError, match="Objetivo inválido"):
        Person(weight=70, gender="m", height=170, age=19, activity=1.55, goal="cortando")


@pytest.mark.parametrize("activity", [0, 1.0, 2.0])
def test_rejects_unknown_activity_factor(activity):
    with pytest.raises(ValidationError, match="Atividade inválida"):
        Person(weight=70, gender="m", height=170, age=19, activity=activity)
