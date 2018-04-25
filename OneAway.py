############################################
###################One Away#################
############################################

def oneAway(s1,s2):
    dict1={}
    ins = 0
    rem = 0
    rep = 0

    if (len(s2)-len(s1)==1):
        for i in range(0,len(s1)):
            if s1[i] not in dict1:
                dict1[s1[i]]=1
        for i in range(0,len(s2)):
            if s2[i] not in dict1:
                ins = ins + 1
    elif (len(s1)-len(s2)==1):
        for i in range(0,len(s2)):
            if s2[i] not in dict1:
                dict1[s2[i]]=1
        for i in range(0,len(s1)):
            if s1[i] not in dict1:
                rem = rem + 1
    elif (len(s1) == len(s2)):
        for i in range(0,len(s1)):
            if s1[i] not in dict1:
                dict1[s1[i]]=1
        for i in range(0,len(s2)):
            if s2[i] not in dict1:
                rep += 1

    if (ins == 1 and rem == 0 and rep == 0):
        return True
    elif (ins == 0 and rem == 1 and rep == 0):
        return True
    elif (ins == 0 and rem == 0 and rep == 1):
        return True
    else:
        return False

if __name__=='__main__':
    print oneAway('pale','ple')
    print oneAway('pale','pales')
    print oneAway('pale','bale')
    print oneAway('pale','ble')
