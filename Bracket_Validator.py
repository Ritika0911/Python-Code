def bracket_validator(string):
    list_v = []
    for i in range(0, len(string)):
        if string[i] == '(' or string[i] == '{' or string[i] == '[':
            list_v.append(string[i])
            print list_v
        elif string[i] == ')' and string[i-1] == '(':
            list_v.remove(string[i-1])
            print list_v
        elif string[i] == '}' and string[i-1] == '{':
            list_v.remove(string[i-1])
            print list_v
        elif string[i] == ']' and string[i-1] == '[':
            list_v.remove(string[i-1])
            print list_v
    print list_v
    return len(list_v) == 0 
            
if __name__ == '__main__':
    print bracket_validator('[{((()))}}]')
    
    
