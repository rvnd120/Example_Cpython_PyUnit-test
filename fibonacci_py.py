"""
This module contains conatins a class MyModuleTest.
The class encloses test menthods test_fibo & test_fibo_seq
to test correctness of fib_number & fib_sequence repectively
in the fibonacci module which is implemented in C

"""
import unittest
import fibonacci

# Look up table for fibonacci numbers till 46 #
# To test for the entire range between 0 to 47 in test_fibo #
lookup_fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
               55, 89, 144, 233, 377, 610, 987,
               1597, 2584, 4181, 6765, 10946,
               17711, 28657, 46368, 75025,
               121393, 196418, 317811, 514229,
               832040, 1346269, 2178309, 3524578,
               5702887, 9227465, 14930352, 24157817,
               39088169, 63245986, 102334155, 165580141,
               267914296, 433494437, 701408733, 1134903170,
               1836311903]


# Run some simple tests to make sure it works:
print("Running tests...")


class MyModuleTest(unittest.TestCase):
    """This class contains test cases to check fibonacci number
    and sequence of fibonacci impelementaion in C"""
    def test_fibo(self):
        """This method tests for correctness of fib_number
        module in the module fibonacci and also for specific
        cases when input number is -ve, floating point, &
        for the numbers that causes integer overflow"""
##        assert fibonacci.fib_number(0) == 0
##        assert fibonacci.fib_number(1) == 1
##        assert fibonacci.fib_number(2) == 1
##        assert fibonacci.fib_number(3) == 2
##        assert fibonacci.fib_number(4) == 3
##        assert fibonacci.fib_number(5) == 5
##        assert fibonacci.fib_number(6) == 8
##        assert fibonacci.fib_number(7) == 13
##        assert fibonacci.fib_number(8) == 21
##        assert fibonacci.fib_number(9) == 34
##        assert fibonacci.fib_number(10) == 55
##        assert fibonacci.fib_number(11) == 89
        for numbers in range(0, 47):
            assert fibonacci.fib_number(numbers) == lookup_fibo[numbers]
        
        # Check for floating point number failure  #
        assert fibonacci.fib_number(1.5) == -1, \
               'Floating point input not allowed'
        
        # Check for integer overflow failure #
        assert fibonacci.fib_number(47) == -2, \
               'Number 47 and numbers greater than 47 causes overflow'
        
        # Check for negative number failure #
        assert fibonacci.fib_number(-2) == -2, \
               'Negative numbers are not allowed'

    def test_fibo_seq(self):
        """This method tests for correctness of fib_sequence
        module in the module fibonacci and also for specific
        cases when input number is -ve, floating point, &
        for the numbers that causes integer overflow"""
        for number in range(0, 47):
            seq = fibonacci.fib_sequence(0)
            assert seq[0] == fibonacci.fib_number(0)
            for numbers in range(len(seq[1])):
                assert seq[1][numbers] == fibonacci.fib_number(numbers)
                
        # Check for negative number failure #        
        assert fibonacci.fib_sequence(-1) == -2, \
                'Negative numbers are not allowed'
        
        # Check for floating point number failure #
        assert fibonacci.fib_sequence(2.3) == -1, \
                'Floating point input not allowed'
        
        # Check for integer overflow failure #
        assert fibonacci.fib_sequence(47) == -2, \
                'number 47 and numbers greater than 47 causes overflow'
        
# Uncommect below lines to run this python module directly from command line #
# if __name__ == '__main__':
#   unittest.main()
