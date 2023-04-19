import pytest
from rockstarapi import *
from FoxDot import *

@pytest.fixture
def rockzero():
    rs = RockstarApi() # can take url default is "https://rockstarapi-production.up.railway.app/"
    rock=rs.getRock(0, debug=True) # calls  https://rockstarapi-production.up.railway.app/rock/0 
    return rock

def test_poeticNumericLiteral():
    assert poeticNumericLiteral("a rolling stone") ==  175
    assert poeticNumericLiteral("a rolling . stone") ==  17.5

def test_rock_default(rockzero):
    assert rockzero.values() == {"papa":[175,1533],"x":[2],"my_array":[[3],[3,3],[3,3,3],[3,3,3,5]], "output":[55,2,3,3,3,5,3]}
    assert rockzero.get("papa") ==  [175,1533]

def test_rock_p(rockzero):
    assert rockzero.P("papa") ==  P[175,1533]


def test_rock_pbase(rockzero):
    assert rockzero.PBase("papa", 10) ==  P[P[1,7,5],P[1,5,3,3]]
    assert rockzero.PBase("papa", 10, 4) == P[P[0,1,7,5],P[1,5,3,3]]

def test_rock_filter(rockzero):
    rockzero.stringParse = RockstarApi.FILTER
    rockzero.load()
    assert rockzero.values() == {"papa":[175,1533],"x":[2], "output":[2,3]}

    assert rockzero.get("papa") ==  [175,1533]
    assert rockzero.P("papa") ==  P[175,1533]
    assert rockzero.PBase("papa", 10) ==  P[P[1,7,5],P[1,5,3,3]]

def test_rock_ignore(rockzero):
    rockzero.stringParse = RockstarApi.IGNORE
    rockzero.load()
    assert rockzero.values() == {'papa': [175, 1533], 'x': [2], 'my_array': [['foo'], ['foo', 'bar'], ['foo', 'bar', 'baz'], ['foo', 'bar', 'baz', 'value']], 'output': ['Hello World', 2, 'foo', 'bar', 'baz', 'value', 3]}

    assert rockzero.get("papa") ==  [175,1533]
    assert rockzero.P("papa") ==  P[175,1533]
    assert rockzero.PBase("papa", 10) ==  P[P[1,7,5],P[1,5,3,3]]
