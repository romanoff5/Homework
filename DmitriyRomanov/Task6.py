"""Task 1.6
Write a Python program to convert a given tuple of positive integers into an integer. Examples: Input: (1, 2, 3, 4) Output: 1234
 """


# adding unique values to a tuple
def sorting(mytupleIni):
    print('Your initial tuple is: ', mytupleIni)
    mylist = list()

    for item in mytupleIni:
        print(item)
        mylist.append(item)
    myMergedtuple = ''.join(map(str, mylist))

    print("Integer values from the initial tuple: ", myMergedtuple)


mytupleIni = (1, 2, 3, 4)


def main():
    # function calling
    sorting(mytupleIni)


# main function calling
if __name__ == "__main__":
    main()
