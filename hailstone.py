"""
File: hailstone.py
Name:
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    TODO:
    """
    n1 = int(input('Enter a number: '))



    while n1 > 1:
        """
        judge the number is even or not
        """
        if n1 % 2 == 0:

            print(n1, " is even,so i take half: ", int(n1/2))
            n1 /= 2



        else:
            print(n1, 'is odd,so I make 3n+1: ', int((n1 * 3) + 1))
            n1 = (n1 * 3) + 1



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
