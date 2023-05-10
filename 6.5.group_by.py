def group_by(func, iterable):
    """
    Groups the elements of an iterable based on the value returned by a given function for each element.
    :param func: The function used to determine the grouping key for each element.
    :param iterable: The iterable to group.
    :return: A dictionary with the grouping key as the key and a list of elements that match the key as the value.
    """
    result = {}
    for item in iterable:
        key = func(item)
        result.setdefault(key, []).append(item)
    return result


if __name__ == '__main__':
    # Group a list of strings by their length
    result = group_by(len, ["hi", "bye", "yo", "try"])
    print(result)  # Output: {2: ["hi", "yo"], 3: ["bye", "try"]}

    # Group a list of numbers by their parity
    result = group_by(lambda x: x % 2, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(result)  # Output: {1: [1, 3, 5, 7, 9], 0: [2, 4, 6, 8]}

    # Group a list of words by their first letter
    result = group_by(lambda x: x[0], ["apple", "banana", "bnan", "cherry", "date", "fig"])
    print(result)  # Output: {'a': ['apple'], 'b': ['banana'], 'c': ['cherry'], 'd': ['date'], 'f': ['fig']}
