def merge_dicts(dict1, dict2):
    dict1_copy = dict1.copy()  # Start with a copy of dict1
    for key, value in dict2.items():
        if key in dict1_copy:
            dict1_copy[key] += value  # Sum the values if the key exists in both dicts
        else:
            dict1_copy[key] = value  # Add the key-value pair if it doesn't exist
    return dict1_copy