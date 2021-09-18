# Python Practice - Session 1
# Task 1.1
# Write a Python program to calculate the length of a string without using the len function.

def findLength(mystring):
    counter = 0
    for i in mystring:
        counter += 1
    print('Its length is:', counter)


mystring = input('Enter your string: ')


def main():
    # function calling
    findLength(mystring)


# main function calling
if __name__ == "__main__":
    main()
