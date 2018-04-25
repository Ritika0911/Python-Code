#########################################
########UniqueCharactersInAString########
#########################################

def isUnique(string):
    dict1 = {}
    if(len(string)>128):
        return False
    else:
        for i in range(0,len(string)):
            if string[i] not in dict1.keys():
                dict1[string[i]] = 1
            else:
                return False
        return True
        
if __name__ == '__main__':
    print isUnique("Ritika")
