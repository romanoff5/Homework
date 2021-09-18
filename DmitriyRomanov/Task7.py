"""Task 1.7
Write a program which makes a pretty print of a part of the multiplication table. Examples: ``` Input: a = 2 b = 4 c = 3 d = 7
Output:
  3 4 5 6 7
2 6 8 10 12 14
3 9 12 15 18 21
4 12 16 20 24 28
 """

a = 2
b = 4
c = 3
d = 7


def multiply_input(a: int, b: int, c: int, d: int):
    listForPrint = list()
    # print segment for multiplication
    for k in range(c, d + 1):
        print(f"{'':<3}{k:0}", end='')
    print(end='\n')
    for i in range(a, b + 1):
        for k in range(c, d + 1):
            listForPrint.append(i * k)
        # print column for multiplication and the result
        print(i, *(f"{i * k:3}" for k in range(c, d + 1)))
        listForPrint = list()


def main():
    # function calling
    multiply_input(a, b, c, d)


# main function calling
if __name__ == "__main__":
    main()