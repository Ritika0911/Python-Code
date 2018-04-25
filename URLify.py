###########################################
###############URLify a string#############
###########################################

def urlify(string):
    string = string.strip()
    string = string.replace(' ','%20')
    print string

if __name__ == '__main__':
    urlify("Ms. Ritika Chowdri")
