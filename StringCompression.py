#############################################
##############String Compression#############
#############################################

def stringCompression(string):
    count=1
    string2=''
    for i in range(1,len(string)):
        if string[i-1] == string[i]:
            count = count + 1
        else:
            string2 = string2+str(string[i-1])+str(count)
            count = 1
    string2 = string2+str(string[i])+str(count)
    if len(string2)<len(string):
        print string2
    else:
        print string

if __name__ =='__main__':
    stringCompression('abcddd')
