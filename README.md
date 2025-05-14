
# CLI report maker from scv files



## Installation

To install dependencies for testing and formatting code use this command

```bash
  poetry install
```
    
## How use

to get detailed information about the script use the command

```bash
  python main.py --help
```
Example help command output
```bash
  usage: cli reporter [-h] [-r REPORT] file path [file path ...]

  script for parsing data from csv files and subsequent report generation

  positional arguments:
  file path            file path

  options:
  -h, --help           show this help message and exit
  -r, --report REPORT  select report type
```

```bash
  python main.py --report payout path/to/file1.scv path/to/file2.scv path/to/file3.scv
```

Example of payout report output with one or more files

```bash
                     report
             name             hours rate payout
Marketing
------------ Alice Johnson    160   50.0 $8000.0
                              160        $8000.0
Design
------------ Bob Smith        150   40.0 $6000.0
------------ Carol Williams   170   60.0 $10200.0
                              320       $16200.0
```

```bash
                     report
             name             hours rate payout
Marketing
------------ Alice Johnson    160   50.0 $8000.0
                              160        $8000.0
Design
------------ Bob Smith        150   40.0 $6000.0
------------ Carol Williams   170   60.0 $10200.0
                              320       $16200.0

                     report
             name             hours rate payout
HR
------------ Grace Lee        160   45.0 $7200.0
------------ Ivy Clark        158   38.0 $6004.0
                              318       $13204.0
Marketing
------------ Henry Martin     150   35.0 $5250.0
                              150        $5250.0

                     report
             name             hours rate payout
Sales
------------ Karen White      165   50.0 $8250.0
------------ Mia Young        160   37.0 $5920.0
                              325       $14170.0
HR
------------ Liam Harris      155   42.0 $6510.0
                              155        $6510.0
```
## Running linters

```bash
  poetry run ruff check --fix
  poetry run ruff format
```

## Running Tests

To run tests, run the following command

```bash
  poetry run pytest --cov=.
```


## Test example result

Test and coverage

```bash
================== test session starts ===================
platform win32 -- Python 3.13.2, pytest-8.3.5, pluggy-1.5.0
rootdir: C:\path\to\file\cli_reporter
configfile: pyproject.toml
plugins: cov-6.1.1
collected 9 items

tests\test_core.py .........                        [100%]

===================== tests coverage =====================
____ coverage: platform win32, python 3.13.2-final-0 _____

Name                 Stmts   Miss  Cover
----------------------------------------
core\__init__.py         0      0   100%
core\cli.py              4      4     0%
core\entities.py        16      0   100%
core\exceptions.py       0      0   100%
core\parsers.py         20      0   100%
core\reports.py         42      0   100%
core\utils.py            6      0   100%
main.py                 12     12     0%
tests\__init__.py        0      0   100%
tests\conftest.py       32      0   100%
tests\test_core.py      44      0   100%
----------------------------------------
TOTAL                  176     16    91%
=================== 9 passed in 0.10s ====================
```


## Possibilities

- To add a new type of report, it is enough to inherit from the abstract report and add it to the factory
- If necessary, you can add a new parser type in the same way, you will also need to add a new argument for argparse to select the parser


