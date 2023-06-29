# Next-Happy-Number
A Happy Number is a non-negative integer that leads to 1 after repeatedly computing the sum of squares of its digits. 

## Theory
To find the next smallest Happy Number, we can start by checking the number N+1 and continue checking subsequent numbers until we find a Happy Number.

To check if a number is Happy, we can follow the process described in the prompt. We start by computing the sum of squares of its digits, and then repeat the process with the resulting number until we either reach 1 (which means the number is Happy) or we enter a cycle (which means the number is not Happy).

For example, let's say we want to check if the number 19 is Happy:

We compute the sum of squares of its digits: 1^2 + 9^2 = 82
We repeat the process with 82: 8^2 + 2^2 = 68
We repeat the process with 68: 6^2 + 8^2 = 100
We repeat the process with 100: 1^2 + 0^2 + 0^2 = 1
Since we reached 1, we can conclude that 19 is a Happy Number.

We can implement a function that takes a non-negative integer N as input and returns the next smallest Happy Number as follows:

Increment N by 1 to get the first number to check.
Repeat the following steps until we find a Happy Number:
Compute the sum of squares of its digits.
If we reach 1, return the number as the next smallest Happy Number.
If we enter a cycle, move on to the next number to check.

## Approach
The code begins by defining a class named Solution. This class will contain the methods to solve the problem.

The first method inside the Solution class is hn(self, n). This method takes a number n as input and calculates the sum of the squares of its digits. Here's how it works:

The variable a is initialized to 0, which will store the sum of the squares of the digits.
The method iterates over each character i in the string representation of n. By converting n to a string, we can access each digit individually.
For each digit, it is converted to an integer using int(i), squared using int(i)**2, and added to the variable a.
After iterating through all the digits, the method checks if the resulting sum a is not a single-digit number. If a has more than one digit, it indicates that the calculation needs to continue. In that case, the method recursively calls itself with a as the input.
If the sum a is a single-digit number, the method returns that value.
The next method is nextHappy(self, n). This method aims to find the next smallest happy number greater than or equal to n. Here's how it works:

The method takes a number n as input.
It checks if the result of calling the hn method with n+1 as the input is either 1 or 7. These are the only two single-digit happy numbers.
If hn(n+1) returns 1 or 7, it means that n+1 is a happy number, so the method returns n+1 as the next smallest happy number.
If hn(n+1) is not 1 or 7, it means that n+1 is not a happy number. In this case, the method recursively calls itself with n+1 as the input to check the next number.
This process continues until a happy number is found.
The code then proceeds to the main block, starting with the line if __name__ == '__main__':. This block is executed when the Python script is run directly (not imported as a module).

Inside the main block, the number of test cases t is read from the input using t = int(input()).

A for loop is used to iterate t times, which represents the number of test cases.

For each test case, the value of N is read from the input using N = int(input()).

An instance of the Solution class is created as ob using ob = Solution().

The nextHappy method of the ob object is called with N as the input, and the resulting next smallest happy number is printed using print(ob.nextHappy(N)).

This process repeats for all the test cases.

The code follows a recursive approach to determine the next smallest happy number based on the provided hn and nextHappy methods. It utilizes recursion to iterate through numbers until a happy number is found.
