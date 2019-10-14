"""
Author:Michael Harmon
Date: 10/13/2019
Description: This program will use a dictionary to act like a switch statement
to locate a key and return the value.
"""


def switch_average(key_to_find):
    """
    use a dictionary to act like a switch to find key
    :param key_to_find: key that is passed in
    :return: value of key if found, if not found return message
    """
    key_not_found = 'Value not found for ' + str(key_to_find) + '.'
    try:
        return {
            'A': 100,
            'B': 89,
            'C': 79,
            'D': 69,
            'F': 59,
        }[key_to_find]
    except KeyError:
        return key_not_found


if __name__ == '__main__':
    key = '$'
    print(switch_average(key))
