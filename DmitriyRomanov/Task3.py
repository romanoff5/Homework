# Task 1.3
"""Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form. Examples:
Input: ['red', 'white', 'black', 'red', 'green', 'black'] Output: ['black', 'green', 'red', 'white'] """

mystring = ['red', 'white', 'black', 'red', 'green', 'black']


def sorting(mystring):
    print('Your list is: ', mystring)
    # convert to list and exclude duplicates
    ask = input('The list will be sorted. Do you want to remove duplicates (y for yes/any other)? ')
    if ask == 'y':
        mystring = tuple(set(mystring))
    else:
        pass
    mystring = list(mystring)
    words = list()
    # sort the list.
    mystring.sort()

    # display the sorted words.
    for word in mystring:
        words.append(word)
    print(words)


def main():
    # function calling
    sorting(mystring)


# main function calling
if __name__ == "__main__":
    main()
