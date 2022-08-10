#include <Python.h>

long Csortn(long n)
{
    int digit_counts[10] = {0,0,0,0,0,0,0,0,0,0};
    while(n > 0) {
        digit_counts[n % 10]++;
        n /= 10;
    }

    long result = 0;
    for (int i = 1; i < 10; i++) {
        for (int j = 0; j < digit_counts[i]; j++) {
            result *= 10;
            result += i;
        }
    }

    return result;
}

long CdigitSquareSum(long n)
{
    long result = 0;
    while (n > 0) {
        int d = n % 10;
        result += d*d;
        n /= 10;
    }
    return result;
}


static PyObject* sortn(PyObject* self, PyObject* args)
{
    long n;
    if(!PyArg_ParseTuple(args, "l", &n))
        return NULL;
    return Py_BuildValue("l", Csortn(n));
}

static PyObject* digitSquareSum(PyObject* self, PyObject* args)
{
    long n;
    if(!PyArg_ParseTuple(args, "l", &n))
        return NULL;
    return Py_BuildValue("l", CdigitSquareSum(n));
}

static PyMethodDef myMethods[] = {
    { "sortn", sortn, METH_VARARGS, "Converts number by sorting digits" },
    { "digit_square_sum", digitSquareSum, METH_VARARGS, "Sums squares of digits" },
    { NULL, NULL, 0, NULL }
};


static struct PyModuleDef happyc = {
    PyModuleDef_HEAD_INIT,
    "happyc",
    "happy c extensions",
    -1,
    myMethods
};

PyMODINIT_FUNC PyInit_happyc(void)
{
    return PyModule_Create(&happyc);
}
