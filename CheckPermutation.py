########################################################################
##########Check if one string is a permutation of another###############
########################################################################

def checkPermutation(string1,string2):
    if len(string1) != len(string2):
        return False
    else:
        for i in range(0,len(string2)):
            if string2[i] not in string1:
                return False
        return True

##def checkPermDict(string1,string2):
##    dict1={}
##    if len(string1) != len(string2):
##        return False
##    else:
##        for i in range(0,len(string1)):
##            if string1[i] not in dict1:
##                dict1[string[i]] = 1

if __name__ == '__main__':
    print checkPermutation('abcd', 'dcba')
