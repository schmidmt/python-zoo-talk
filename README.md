# The Python Zoo


## Table of Contents

0. [Prerequisites](#prerequisites)
1. [Virtual Environments](#virtual-environments)
2. [Standard Library](#standard-library)
3. [Plotting](#plotting)
4. [Analysis](#analysis)
5. [Development Tools](#development-tools)

## Prerequisites
__Please__ ensure you have Python installed, either via Conda or the python installer.

I'd suggest using one of the following:

* [Miniconda](https://docs.conda.io/en/main/miniconda.html) - I find the Conda ecosystem to be unnecessarily confusing, but if you already use it, you might want to continue.
* [Python](https://www.python.org/downloads/) - This is the vanilla python. It's my suggested version.

If you use Linux or MacOS, you can install python with the package manager for your system.

## Virtual Environments

When Python was created, it was convention to have all modules and libraries installed globally; i.e. every program you used, could only use the same version as every other program.
To address this, several different, but similar, solutions have been created.
The two most important are __Python's venv__ and __Conda's Envs__.


### Python's venv
This is built into Python's standard library and it's documentation is [here](https://docs.python.org/3/library/venv.html).

Creating a new Virtual Environment:
```bash
python -3 -m venv <venv>
```

Activating the environment depends on your shell:
| Platform | Shell           | Command to activate virtual environment |
| -------- | --------------- | --------------------------------------- |
| POSIX    | bash/zsh        | `$ source <venv>/bin/activate`          |
|          | fish            | `$ source <venv>/bin/activate.fish`     |
|          | csh/tcsh        | `$ source <venv>/bin/activate.csh`      |
|          | PowerShell Core | `$ <venv>/bin/Activate.ps1`             |
| Windows  | cmd.exe         | `C:\> <venv>\Scripts\activate.bat`      |
|          | PowerShell      | `PS C:\> <venv>\Scripts\Activate.ps1`   |


Any installs from this point are installed in the virtual environment.
To store the versions used, run `pip3 freeze > requirements.txt`.

Deactivation:
```bash
deactivate
```


### Conda's Virtual Environment

Create:
```bash
conda create --name myenv
```

Activate:
```bash
conda activate myenv
```

Any Conda installs from this point go into the virtual environment.

Deactivate:
```bash
conda deactivate
```

## Standard Library

The standard library for Python contains tools which are general and performant.
A full list can be found [here](https://docs.python.org/3/library/index.html).
What follows is a sampling I think is a good place to start.

### RE
[Docs](https://docs.python.org/3/library/re.html).

The `re` library contains tools to work with [Regular Expressions](https://en.wikipedia.org/wiki/Regular_expression) for pattern matching.
It's worth noting, not all regular expression syntax is the same.

#### Example

```python
import re

expression = re.compile(r"abc")

print(expression.match("abcdef"))
print(expression.match("defghi"))
```


### Itertools
[Docs](https://docs.python.org/3/library/itertools.html?highlight=itertools).

Itertools are useful for common enumerations to make iteration more efficient and easy to understand.

#### Example
```python
import itertools

list(itertools.permutations('ABCD', 2))
```

### Argparse
[Docs](https://docs.python.org/3/library/argparse.html?highlight=argparse)

Argparse is a tool for parsing command line arguments.

#### Example
```python
import argparse

parser = argparse.ArgumentParser(description="An example for Argparse")
parser.add_argument("-n", "--n-iterations", type=int, help="number of iterations to perform")
args = parser.parse_args()

print(args)
```


### Unittest

We'll use `pytest` as our test runner so let's make sure that it's installed:
```bash
$ pip3 install pytest
# OR
$ conda install pytest
```

Unit testing is the practice of testing each "unit" of code.
For example

```python
import unittest

def collatz_steps(n: int) -> int:
    steps = 0
    while n > 1:
        if n & 1 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1

    return steps


class CollatzStepsTest(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(collatz_steps(1), 0)

    def test_larger(self):
        self.assertEqual(collatz_steps(27), 111)
```

## Plotting

### [Matplotlib](https://matplotlib.org/stable/api/index.html)

### [Seaborn](https://seaborn.pydata.org/api.html)

### [Plotly](https://plotly.com/python/reference/)


## Analysis

### [Numpy](https://numpy.org/doc/stable/reference/index.html#reference)

### [Scipy](https://docs.scipy.org/doc/scipy/reference/)

### [Pandas](https://pandas.pydata.org/docs/reference/index.html)

### [Polars](https://www.pola.rs)



## Development Tools


### [Black](https://black.readthedocs.io/en/stable/)

### Linters

* [Pylint](https://pylint.pycqa.org/en/latest/)
* [Flake8](https://pypi.org/project/flake8/)

### Git
