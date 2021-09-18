# Task 1.5
"""Write a Python program to print all unique values of all dictionaries in a list. Examples: Input: [{"V":"S001"}, {"V": "S002"}, {"VI":
"S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}] Output: {'S005', 'S002', 'S007', 'S001',
'S009'} """

# adding unique values to a list
def sorting(mylistIni):
    print('Your initial list is: ', mylistIni)
    #create the list for values
    mylist = list()
    #go through the dictionaries in the lest
    for item in mylistIni:
        for value in item.values():
            if value not in mylist:
                #adding a unuqe value to the list
                mylist.append(value)
    print("List of unique values from the initial list: ", mylist)


mylistIni = [{"V": "S001"},
          {"V": "S002"},
          {"VI": "S001"},
          {"VI": "S005"},
          {"VII": "S005"},
          {"V": "S009"},
          {"VIII": "S007"}]


def main():
    # function calling
    sorting(mylistIni)


# main function calling
if __name__ == "__main__":
    main()
