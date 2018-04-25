def which_appears_twice(list1):
    sum_of_all = sum(list1)
    len_of_list = len(list1)
    sum_in_range = (len_of_list *(len_of_list - 1))/2
    number = sum_of_all - sum_in_range
    return number

if __name__ == '__main__':
    list1 = [1,2,3,4,5,6,7,7,8,9,10]
    print which_appears_twice(list1)
