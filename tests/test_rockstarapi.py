from rockstarapi import *
from FoxDot import *

def test_poeticNumericLiteral():
    assert poeticNumericLiteral("a rolling stone") ==  175
    assert poeticNumericLiteral("a rolling . stone") ==  17.5

def test_rock_default():
    rs = RockstarApi() # can take url default is "https://rockstarapi-production.up.railway.app/"
    rock=rs.getRock(0) # calls  https://rockstarapi-production.up.railway.app/rock/0 

    assert rock.PBase("papa", 10) == P([1,7,5,1,5,3,3])
    assert rock.values() == {"papa":[175,1533],"x":[2],"my_array":[[3],[3,3],[3,3,3],[3,3,3,5]], "output":[55,2,3,3,3,5,3]}

    assert rock.get("papa") ==  [175,1533]
    assert rock.P("papa") ==  P([175,1533])
    assert rock.PBase("papa", 10) == P([1,7,5,1,5,3,3])
    assert rock.PBase("papa", 10,8) == P([0,1,7,5,1,5,3,3])

    rock.stringParse = RockstarApi.FILTER
    rock.load()
    assert rock.values() == {"papa":[175,1533],"x":[2],"my_array":[], "output":[2,3]}

    assert rock.get("papa") ==  [175,1533]
    assert rock.P("papa") ==  P([175,1533])
    assert rock.PBase("papa", 10) == P([1,7,5,1,5,3,3])

    rock.stringParse = RockstarApi.IGNORE
    rock.load()
    assert rock.values() == {'papa': [175, 1533], 'x': [2], 'my_array': [['foo'], ['foo', 'bar'], ['foo', 'bar', 'baz'], ['foo', 'bar', 'baz', 'value']], 'output': ['Hello World', 2, 'foo', 'bar', 'baz', 'value', 3]}

    assert rock.get("papa") ==  [175,1533]
    assert rock.P("papa") ==  P([175,1533])
    assert rock.PBase("papa", 10) == P([1,7,5,1,5,3,3])
