##########################################
#############Rotate Matrix################
##########################################

def rotateMatrix(foo):
    for i in range(len(foo[0]),0):
        for j in range(0,len(foo)):
            foo[i][j] = foo[j][i] 
    return foo

if __name__ == '__main__':
    data = [[1, 2],
            [3, 4]]
    print rotateMatrix(data)
