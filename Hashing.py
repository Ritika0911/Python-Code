class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def calculate(self, string):
        hv = (ord(string[0])*100 + ord(string[1]))
        return hv

    def store(self, string):
        hv = self.calculate(string)
        if hv != -1:
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
             self.table[hv] == [string]

    def lookup(self, string):
        hv = self.calculate(string)
        if hv != -1:
            if self.table[hv] != None:
                if string in self.table[hv]:
                    return hv
        return -1
