def merge_sorted_list(list1, list2):
    m = len(list1)
    n = len(list2)
    i = 0
    j = 0
    k = 0
    list3_len = m + n
    list3 = [None] * list3_len
    
    while k < list3_len:
        if i == m or list1[i] > list2[j]:
            list3[k] = list2[j]
            j += 1
        elif j == n or list1[i] < list2[j]:
            list3[k] = list1[i]
            i += 1
        k += 1  
    return list3

if __name__ == '__main__':
    sorted_list1 = [2,3,4,5]
    sorted_list2 = [1,6,7,9]
    print merge_sorted_list(sorted_list1, sorted_list2)
