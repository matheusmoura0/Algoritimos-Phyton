def is_anagram(first_string, second_string):
    list1 = list(first_string.lower())
    list2 = list(second_string.lower())

    if len(list1) != len(list2):
        return False


    for i in list1:
        if i in list2:
            list2.remove(i)
        else:
            return False
    return True