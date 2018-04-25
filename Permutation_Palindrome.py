def has_palindrome_permutation(string):
    unpaired_characters = set()
    for char in string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    return len(unpaired_characters) <= 1

if __name__== '__main__':
    print has_palindrome_permutation('aabbccddeeeffff')
