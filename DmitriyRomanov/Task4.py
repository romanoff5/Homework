# Task 1.4
# Write a Python program to sort a dictionary by key.

# sorting dictionary
def sorting(mydict):
    print('Your dictionary for sorting is: ', mydict)
    # create the new sorted dictionary
    sortedDict = dict()
    for key in sorted(mydict):
        sortedDict[key] = mydict[key]
    print(sortedDict)


mydict = {'alyaska': '123213',
          'texas': '121321',
          'alabama': '32143243',
          'chicago': '666662'}


def main():
    # function calling
    sorting(mydict)


# main function calling
if __name__ == "__main__":
    main()
