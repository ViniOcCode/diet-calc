import pytest
from app.models.calculator import Person

@pytest.fixture
def persons():
    p = Person(weight=70, sex="M", height=170, year=19, activity=1.55)
    p2 = Person(weight=57, sex="f", height=157, year=22, activity=1.55)
    p3 = Person(weight=70, sex="m", height=170, year=19, activity=1.55, goal='cutting')

    return p, p2, p3 

def test_valid_persons(persons):
    for i in persons:
        assert isinstance(i, Person)

    with pytest.raises(ValueError):
        Person()

    with pytest.raises(ValueError):
        Person(weight=57, sex="f", year=22, activity=1.55)


def test_tmb_calc(persons):
    p, p2, p3 = persons

    assert p.tmb_calc() == 2706
    assert p2.tmb_calc() == 2141
    assert p3.tmb_calc() == 2706

    with pytest.raises(ValueError):
        Person().tmb_calc()

def test_water_calc(persons):
    p, p2, p3 = persons

    assert p.water_calc() == 2450
    assert p2.water_calc() == 1995
    assert p3.water_calc() == 2450
    

    with pytest.raises(ValueError):
        Person().water_calc()

def test_summary(persons):

    p, p2, p3 = persons
    assert p.summary()["tmb"] == 2706
    assert p2.summary()["tmb"] == 2141
    assert p3.summary()["tmb"] == 2106


