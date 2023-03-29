from genericpath import exists
import urllib.request

class RockstarApi():
    def __init__(self, url = "https://rockstarapi-production.up.railway.app/"):
        self.url = url
        pass

    def getRock(self, id):
        return Rock(self.url, id)


class Rock():
    cache   = None
    stringParse = None
    flatten = True
    def __init__(self, url, id):
        self.url = url+"rock/"+str(id)
        self.load()

    def load(self):
        self.contents = urllib.request.urlopen(self.url).read()
        print (self.contents)

        #de-json it into dictionary
        #parse strings to numbers, or filter out
        #print out the keys of log

        #cache the log with output as a entry in it.
        self.cache = {} #stuff

    def _get(self, key):
        if self.cache == None:
            self.load()
        if self.cache != None and key in self.cache:
            return self.cache[key]
        return None

    def P(self, key):
        value = self._get(key)
        return value

    def values(self):
        if self.cache == None:
            self.load()
        return self.cache

    def P(self, key):
        values = self.get(key)
        pattern = []
        # if self.flatten
            # flatten
        # map to pattern
        return pattern


    def PBase(self, key):
        values = self.get(key)
        patterns = []
        # Pbase the numbers
        # if self.flatten
            # flatten
        # map to patterns
        return patterns

rs = RockstarApi() # can take url default is "https://rockstarapi-production.up.railway.app/"
rock=rs.getRock(0) # calls  https://rockstarapi-production.up.railway.app/rock/0 

assert rock.contents == {"papa":[175,1533],"x":[2],"my_array":[{"0":"foo"},{"0":"foo","1":"bar"},{"0":"foo","1":"bar","2":"baz"},{"0":"foo","1":"bar","2":"baz","key":"value"}], "output":["Hello World",2,"foo","bar","baz","value",3]}
assert rock.values() == {"papa":[175,1533],"x":[2],"my_array":[[3],[3,3],[3,3,3],[3,3,3,5]], "output":[55,2,3,3,3,5,3]}


assert rock.get("papa") ==  [175,1533]
assert rock.P("papa") ==  P([175,1533])
assert rock.PBase("papa", 10) == P([1,7,5,1,5,3,3])
