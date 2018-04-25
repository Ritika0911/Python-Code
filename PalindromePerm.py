################################################
#################Palindrome Permutation#########
################################################

def palPerm(string):
    string = string.lower()
    string = string.replace(' ','')
    dict1={}
    count = 0
    for i in range(0,len(string)):
        if string[i] not in dict1:
            dict1[string[i]]=1
        elif string[i] in dict1:
            dict1[string[i]]=dict1[string[i]] + 1
    for i in dict1.values():
        if i % 2 != 0:
            count +=1
    if count == 0 or count ==1:
        print "Palindrome Permutation"
    else:
        print "Sorry."
if __name__ == '__main__':
    palPerm('Tact Coa')
