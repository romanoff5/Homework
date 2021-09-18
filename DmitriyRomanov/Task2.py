# Task 1.2
"""Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters). Examples: Input: 'Oh, it
is python' Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1} """


# function calling
def dictionairy():
    mystring = (input('Enter your string: ')).lower()

    result = dict()

    for i in mystring:
        if i not in result:
            # create a new key value in the dictionary
            result.update({i: '1'})
        else:
            counter = 1
            counter += int(result[i])
            # else we increase a number of the particular character
            result[i] = counter
    print('The calculation of characters is:', result)
    result = {k: result[k] for k in sorted(result)}
    print('The sorted dictionary is:', result)


def main():
    # function calling
    dictionairy()


# main function calling
if __name__ == "__main__":
    main()
