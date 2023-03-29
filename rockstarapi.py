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

rs = RockstarApi() # can take url default is "https://rockstarapi-production.up.railway.app/"
rock=rs.getRock(0) # calls  https://rockstarapi-production.up.railway.app/rock/0 

assert rs.getRock(0) == {"papa":[175,1533],"x":[2],"my_array":[{"0":"foo"},{"0":"foo","1":"bar"},{"0":"foo","1":"bar","2":"baz"},{"0":"foo","1":"bar","2":"baz","key":"value"}], "output":["Hello World",2,"foo","bar","baz","value",3]}