import urllib.request
        

class RockstarApi():
    def __init__(self, url = "https://rockstarapi-production.up.railway.app/"):
        self.url = url
        pass

    def getRock(self, id):
        url = self.url+"rock/"+str(id)
        contents = urllib.request.urlopen(url).read()
        print (contents)
        #de json it
        #print out the keys of log
        return

rs = RockstarApi() # can take url default is "https://rockstarapi-production.up.railway.app/"
rock=rs.getRock(0) # calls  https://rockstarapi-production.up.railway.app/rock/0 

assert rs.getRock(0) == {"id":0,"status":"success","code":"Shout \"Hello World\"!\npapa was a rolling stone\npapa was a brand new bag\nx is 2\nShout x\nLet my array at 0 be \"foo\"\nLet my array at 1 be \"bar\"\nLet my array at 2 be \"baz\"\nLet my array at \"key\" be \"value\"\nShout my array at 0\nShout my array at 1\nShout my array at 2\nShout my array at \"key\"\nShout my array\nGive back 1\n","log":{"papa":[175,1533],"x":[2],"my_array":[{"0":"foo"},{"0":"foo","1":"bar"},{"0":"foo","1":"bar","2":"baz"},{"0":"foo","1":"bar","2":"baz","key":"value"}]},"output":["Hello World",2,"foo","bar","baz","value",3]}