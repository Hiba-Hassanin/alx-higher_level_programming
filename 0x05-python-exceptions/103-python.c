#include <Python.h>
#include <floatobject.h>
#include <bytesobject.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %ld bytes:", size < 10 ? size + 1 : 10);
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02x", (unsigned char)str[i]);
	printf("\n");
}

void print_python_float(PyObject *p)
{
	PyObject *str;
	char *str_value;

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	str = PyObject_Str(p);
	str_value = PyUnicode_AsUTF8(str);

	printf("  value: %s\n", str_value);

	Py_DECREF(str);
}
