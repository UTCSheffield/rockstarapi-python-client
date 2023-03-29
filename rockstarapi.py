import urllib.request

class RockstarApi():
    def __init__(self, url = "https://rockstarapi-production.up.railway.app/"):
        self.url = url
        pass

    def getRock(self, id):
        url = self.url+"rock/"+str(id)
        contents = urllib.request.urlopen(url).read()
        print (contents)
        #de-json it into dictionary

        #print out the keys of log 
        return  # log with output as a entry in it.

    def getPRock(self, id, base=None, flatten=False):
        values = self.getRock(id)
        #filter the values so its only numbers
        #map to patterns
        patterns = {}
        return patterns

rs = RockstarApi() # can take url default is "https://rockstarapi-production.up.railway.app/"
rock=rs.getRock(0) # calls  https://rockstarapi-production.up.railway.app/rock/0 

assert rs.getRock(0) == {"papa":[175,1533],"x":[2],"my_array":[{"0":"foo"},{"0":"foo","1":"bar"},{"0":"foo","1":"bar","2":"baz"},{"0":"foo","1":"bar","2":"baz","key":"value"}], "output":["Hello World",2,"foo","bar","baz","value",3]}

assert rs.getPRock(0) ==  {"papa":P([175,1533]),"x":P([2]),"my_array":P([]), "output":P([2 , 3])}

#Not sure whether to go with every pattern as a pattern
assert rs.getPRock(0, base=10) ==                 {"papa":P([P([1,7,5]),P([1,5,3,3])]),"x":P(P([2])),"my_array":P([]), "output":P[P([2]) , P([3])]}
assert rs.getPRock(0, base=10, flatten=False) ==  {"papa":P([P([1,7,5]),P([1,5,3,3])]),"x":P(P([2])),"my_array":P([]), "output":P[P([2]) , P([3])]}
#or flatten them??
assert rs.getPRock(0, base=10, flatten=True) ==  {"papa":P([1,7,5,1,5,3,3]),"x":P([2]),"my_array":P([]), "output":P([2,3])}
