Step 1.

Name the file extension .pyx, e.g. hello.pyx
Hello.pyx contais your python/cython code 

Step 2.

Create setup.py file with below contents.
# Start of file.
from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Cython world app',
    ext_modules=cythonize("hello.pyx", compiler_directives={'language_level' : "3"}),
    zip_safe=False,
)
# End of file.

Use below compiler directive in ext_modules to use python3
compiler_directives={'language_level' : "3"} 

Step 3.
Run below command on command prompt
$python3 setup.py build_ext --inplace
# This will create library file with .so and .c files.

Step 4.
In your Python File, import new library and call functions.
import hello
hello.printMe('Hi There')

Few Tips.

