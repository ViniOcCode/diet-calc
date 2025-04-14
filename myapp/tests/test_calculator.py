import pytest
from myapp.models.calculator import Person

@pytest.fixture
def persons():
    p = Person(weight=70, gender="M", height=170, age=19, activity=1.55)
    p2 = Person(weight=57, gender="f", height=157, age=22, activity=1.55)
    p3 = Person(weight=70, gender="m", height=170, age=19, activity=1.55, goal='cutting')

    return p, p2, p3 

def test_valid_persons(persons):
    for i in persons:
        assert isinstance(i, Person)

    # testing null values
    with pytest.raises(ValueError, match="All fields need values."):
        Person()

    # testing 1 null value
    with pytest.raises(ValueError, match="All fields need values."):
        Person(weight=57, gender="f", age=22, activity=1.55)


def test_tmb_calc(persons):
    p, p2, p3 = persons

    assert p.bmr_calc() == 2706
    assert p2.bmr_calc() == 2141
    assert p3.bmr_calc() == 2706

    # Testing weight value 
    with pytest.raises(ValueError, match="Weight value is not allowed."):
        Person(weight=301, gender="m", height=170, age=19, activity=1.55).tmb_calc()

    with pytest.raises(ValueError, match="Weight value is not allowed."):
        Person(weight=-1, gender="m", height=170, age=19, activity=1.55).tmb_calc()

def test_water_calc(persons):
    p, p2, p3 = persons

    assert p.water_calc() == 2450
    assert p2.water_calc() == 1995
    assert p3.water_calc() == 2450
    
    # testing ages value
    with pytest.raises(ValueError, match="Age value is not allowed."):
        Person(weight=57, gender="f", height=158, age=121, activity=1.55).water_calc()

    with pytest.raises(ValueError, match="Age value is not allowed."):
        Person(weight=57, gender="f", height=158, age=-1, activity=1.55).water_calc()

def test_summary(persons):

    p, p2, p3 = persons
    assert p.summary()["bmr_goal"] == 2706
    assert p2.summary()["bmr_goal"] == 2141
    assert p3.summary()["bmr_goal"] == 2106

    with pytest.raises(ValueError, match="Given goal is not allowed."):
        Person(weight=70, gender="m", height=170, age=19, activity=1.55, goal='cortando')       