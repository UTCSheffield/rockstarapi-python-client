from genericpath import exists
import json
import requests
from FoxDot import *

try:
  PBase(5)
except NameError:
    # Would Prefer to use our version of FoxDot that includes this
    @loop_pattern_func
    def PBase(n, b=2, l=1):
        ''' Returns the 'n' number in base 'b' split into digits.
            e.g. `PBase(5)` will return `P[1,0,1]`
            and  `PBase(5,4)` will return `P[1,1]`
            and  `PBase(5,4,4)` will return `P[0,0,1,1]`
        '''
        number = 0+n

        from_base10_to_anybase_num = [] # Initialize the number in any base
        while number > 0: # Iterate while the number is greater than zero
            remainder = int(number % b) # change remainder in integer
            #from_base10_to_anybase_num.append( remainder )
            from_base10_to_anybase_num.insert(0, remainder )
            number //= b # take the integer part after division
        
        number_list = [int(i) for i in from_base10_to_anybase_num]
        
        while(len(number_list) < l):
            number_list.insert(0, 0)
        
        #print("from_10_to_anybase("+str(num)+","+str(base)+")", number_list)
        
        return Pattern( number_list )

print('''***** RockstarApi Loaded : Usage *****
rs = RockstarApi() # can take url, default is "https://rockstarapi-production.up.railway.app/"
rock=rs.getRock(0)''')

class RockstarApi():
    IGNORE      = "IGNORE"
    FILTER      = "FILTER"
    ROCKSTAR    = "ROCKSTAR"

    def __init__(self, url = "https://rockstarapi-production.up.railway.app/"):
        self.url = url
        

    def getRock(self, id):
        return Rock(self.url, id)
    
def lenOrDot(a):
    if a == ".":
        return a
    return str(len(a))

def poeticNumericLiteral(text):
    if type(text) in [int, float]:
        return text

    words=text.split(' ')
    number = "".join(list(map(lenOrDot, words)))

    if "." in number :
        return float(number)
    return int(number)

class Rock():
    cache   = None
    stringParse = RockstarApi.ROCKSTAR
    flatten = True
    def __init__(self, url, id):
        self.id = id
        self.url = url+"rock/"+str(id)
        self.load()

    def parseOrFilter(self, item):
        #print("type(item)", type(item), item)

        if(len(item) and type(item[0]) == dict):
            valueList = list(map(lambda a : list(a.values()), item))
            processed = list(map(self.parseOrFilter , valueList))
            #print("self.stringParse",self.stringParse,"processed", processed)
            filtered = list(filter(len , processed))
            return filtered

        if self.stringParse == RockstarApi.FILTER:
            filtered = list(filter(lambda a : type(a) in [int, float] , item))
            return filtered

        if self.stringParse == RockstarApi.ROCKSTAR:
            parsed = list(map(poeticNumericLiteral , item))
            return parsed

        ##RockstarApi.IGNORE:
        return item

    def load(self):
        #contents = urllib.request.urlopen(self.url).read()
        contents = requests.get(self.url).json()
        self.contents = contents
        #print (self.contents)
        self.cache = {} #stuff

        #print("self.contents['log']", self.contents['log'])
        #cache the log 
        
        for key in self.contents['log']:
            item = self.contents['log'][key]
            #print out the keys and contents of log
            #print(key, item)
            #parse strings to numbers, or filter out
            self.cache[key] = self.parseOrFilter(self.contents['log'][key])

        # with output as a entry in it.
        self.cache['output'] = self.parseOrFilter(self.contents['output'])
 
        print("Loaded Rock",self.id, "with",self.stringParse ,"available keys = ", list(self.cache.keys()))

    def _get(self, key):
        if self.cache == None:
            self.load()
        if self.cache != None and key in self.cache:
            print("_getting", key, self.cache[key])
            return self.cache[key]
        return None
    
    def get(self, key):
        return self._get(key)

    def values(self):
        if self.cache == None:
            self.load()
            #print("values", self.cache)
        return self.cache

    def _P(self, values):
        print("_P values", values)
        if type(values) == list:
            if(len(values) and type(values[0]) == list):
                return PGroup(map(lambda a : self._P(a), values))
            else:
                return P[values]
        else:
            return P(values)

    def P(self, key):
        values = self.get(key)
        returned =  self._P(values)
        print("returned", returned)
        return returned
    
    def _PBase(self, values, base=10, l=1):
        print("_PBase values", values)
        if type(values) == list:
            if(len(values) and type(values[0]) == list):
                return P[list(map(lambda a : self._PBase(a, base, l), values))]
            else:
                return P[list(map(lambda a : PBase(a, base, l), values))]
        else:
            return PBase(values, base, l)

    def PBase(self, key, base=10, l=1):
        values = self.get(key)
        returned =  self._PBase(values, base, l)
        print("PBase returned", returned)
        return returned
