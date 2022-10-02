# The Python Zoo


## Table of Contents

0. [Prerequisites](#Prerequisites)
1. [Virtual Environments](#Virtual-Environments)

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

Any conda installs from this point go into the virtual environment.

Deactivate:
```bash
conda deactivate
```
