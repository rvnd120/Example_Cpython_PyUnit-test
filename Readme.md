# Embedded Programming Exercise
Functionality: Python script imports a library which is implemented in C and tests the functionalities of the library. The library finds fibonacci number and fibonacci sequence.

Assumptions Made: In C implementation functions fib_number & fib_sequence uses data type for fibonacci number is uint32_t. Whereas UINT_MAX is 4294967295 so at max we can find fib_number(46) with out integer overflow. I assumed it is only implemented till 46 (i.e for results upto 4 byte). I have included a check in C code to fail the code if the input is greater than 46. This can be changed if we use uint64_t or long long int depends up on the implementation need.

Testing Frame work: I have used PyUnit testing framework to check functionalities like fib_number and fib_sequence. Also written a test suite and included our test module. Using this suite include more test modules to the framework without duplicating the procedures.

Test Suite File Name: The name of the test suite file is fibo_test_suite.py

Command to Execute: python -m unittest -v fibo_test_suite.fibo_suite
