#include <Python.h>

/**
 * print_python_string - Prints Python string info
 * @p: Pointer to PyObject
 */

void print_python_string(PyObject *p)
{
    Py_ssize_t len;
    const char *str;
    PyUnicodeObject *unicode;

    printf("[.] string object info\n");
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    unicode = (PyUnicodeObject *)p;
    len = PyUnicode_GET_LENGTH(p);
    str = PyUnicode_AsUTF8(p);

    printf("  type: %s\n", (len == (Py_ssize_t)PyUnicode_GET_LENGTH(p)) ? "compact ascii" : "compact unicode object");
    printf("  length: %ld\n", len);
    printf("  value: %s\n", str);
}
