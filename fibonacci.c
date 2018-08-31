
/* Headers */

#include <Python.h>
#include <stdlib.h>
/* Internal Prototypes */

static unsigned int fib_number(unsigned int n);
static signed int fib_number_sequence(unsigned int n, unsigned int **sequence);

static PyObject *py_fib_number(PyObject *self, PyObject *args);
static PyObject *py_fib_sequence(PyObject *self, PyObject *args);

/* Internal Private Data */

/// Defines Python->C method mappings for this module.
PyMethodDef method_bindings[] = {
    { "fib_number", py_fib_number, METH_VARARGS, "Calculate and return the Fibonacci number." },
    { "fib_sequence", py_fib_sequence, METH_VARARGS, "Calculate and return the entire Fibonacci sequence." },
    { NULL, NULL, 0, NULL}  /* Sentinel */
};


/* Implementation */
static unsigned int fib_number(unsigned int number) {
	unsigned int fibo[(number+2)];
	unsigned int index;

	fibo[0] = 0;
	fibo[1] = 1;

	for(index = 2; index <= number; index++) {
	fibo[index] = fibo[(index-1)] + fibo[(index-2)];
	}
	
	return fibo[number];
}
	
  
/*!
   Computes the fibonacci sequence for a given number. Both the number and the sequence are returned.

   The 'sequence' parameter is a heap allocated object; ownership is passed to the caller.

   @note Uses the more modern Fibonacci sequence where the first value of the sequence is 0, rather than 1.

   @param n number to compute
   @param sequence pointer to heap allocated array that is the complete sequence

   @return returns the fibonacci number
 */
static signed int fib_number_sequence(unsigned int number, unsigned int **sequence) {
    *sequence = (unsigned int*)malloc(sizeof(unsigned int) * number);//check for malloc null & free the memory//
    if(*sequence == NULL) {
	return -1;
    }	
    // change i < n to i<=n //
    for(unsigned int index = 0; index <= number; index++) {
        (*sequence)[index] = fib_number(index);
    }
    // change n-1 to n //
    return (*sequence)[number];
}

static PyObject *py_fib_number(PyObject *self, PyObject *args) {
   //check for -ve number and change n to uint32_t// 
    int number;
    
    if(PyArg_ParseTuple(args, "i", &number) == 0){
	return Py_BuildValue("i",-1);
    }
    
    if((number < 0) || number >= 47){
	return Py_BuildValue("i",-2);
    }

    return Py_BuildValue("I", fib_number(number));
}

static PyObject *py_fib_sequence(PyObject *self, PyObject *args) {
    int number;
    
    if(PyArg_ParseTuple(args, "i", &number) == 0){
	return Py_BuildValue("i",-1);
    }

    if((number < 0) || number >= 47){
        return Py_BuildValue("i",-2);

    }

    // Get the number and sequence:
    unsigned int *sequence;
    signed int fibo_number = fib_number_sequence(number, &sequence);
    if(number == -1){
	return Py_BuildValue("i",-3);
    }
	
    // Now build a Python list from the C array:
    PyObject *pylist = PyList_New((number+1));

    if(pylist == NULL){
	return Py_BuildValue("i",-4);
    }

    for(int index = 0; index <= number; index++) {

        PyObject *obj = Py_BuildValue("I",sequence[index]);
	if((PyList_SetItem(pylist,index,obj)) == -1){
	     return Py_BuildValue("i",-5);
	}
         
    }	
    

    free(sequence);
    sequence = NULL;

    return Py_BuildValue("(IO)", fibo_number, pylist);
}

/* Module initialization */
PyMODINIT_FUNC initfibonacci(void) {
    (void)Py_InitModule("fibonacci", method_bindings);
}
