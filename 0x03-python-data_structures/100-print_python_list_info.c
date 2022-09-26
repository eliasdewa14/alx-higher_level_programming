#include <Python.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size;
	int i = 0;

	printf("[*] Size of the Python List = %li\n", );
	printf("[*] Allocated = %li\n", );
	
	for (; i < size; i++)
		printf("Element %li: %s", i, );
}
