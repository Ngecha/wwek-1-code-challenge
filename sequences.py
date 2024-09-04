def sort_by_age(list_tuple):
    # sorts the list of tuples by age which is the second element.
    return sorted(list_tuple, key=lambda person: person[1])