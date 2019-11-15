# Package Skeleton

## Introduction
This repository provides an example for writing packages and modules in Python3.

## Folder structure
```bash
.
├── docs
│   └── README.md
├── main_package
│   ├── __init__.py
│   ├── package_a
│   │   ├── __init__.py
│   │   ├── module_a1.py
│   │   └── utils.py
│   ├── package_b
│   │   ├── __init__.py
│   │   ├── module_b1.py
├── setup.py
└── tests
    ├── __init__.py
    ├── package_a
    │   ├── __init__.py
    │   └── test_module_a1.py
    ├── package_b
    │   ├── __init__.py
    │   └── test_module_b1.py
    └── test_package.py
```
`setup.py`: Containing information (such as package name, author, version, dependencies,...) for installation and distribution of the package. With this file, installation can be done with `pip` command.

`__init__.py`: is necessary to make a folder become a Python package (initialize package). Note that `__all__` variable in some files is to list module names in that package, so that they can be imported more shortly (see `tests/test_package`).

Note: Files in packages and modules uses relative import (`.` and `..`), so they can not be executed directly by the command
```bash
python main_package/{package_name}/{module_name}.py
```
because this command make `__name__` variable of executed file become `__main__` but not `{module_name}`.  
It is preferable to install and import the package as we do in the `Usage` part.

## Usage
To install the package and use as Python standard libraries, run this command from root directory of the package (containing `setup.py` file)
```bash
pip install -e .
```
or run this command from anywhere.
```bash
pip install git+https://github.com/KienMN/Package-Skeleton.git
```
Note: `-e` flag determines installation with editable mode, which means that installed package will be synchronized with updates in the source code.  

After installation, packages and modules can be imported as a Python standard libraries.
```Python
from main_package.package_a import ClassA
```

## Testing
Testcases files are written following format of `pytest` and can be run by the command.
```bash
pytest tests/{package_name}/{test_file_name}.py
```

## Reference
Hitchhiker's guide to the Python imports: https://alex.dzyoba.com/blog/python-import/