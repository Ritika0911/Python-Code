def string_palindrome(string):
    if len(string) == 1:
        return True
    start_index = 0
    end_index = len(string) - 1
    while start_index < end_index:
        if string[start_index] == string[end_index]:
            start_index += 1
            end_index -= 1
        else:
            return False
    return True
            
if __name__ == '__main__':
    print string_palindrome('civil')
