# Green Button Objects

This Python code parses an Energy Service Provider Interface
(ESPI), or "Green Button", XML file into Python objects.

Run `parse_feed()` from the `parse.py` file to get a list of `UsagePoint`
objects.  From there you should be able to explore all of the data in the
feed.  Documentation is a little lacking at the moment, but the class
members mostly match the names from the ESPI standard (or at least the XML
entities).

There's a bit of documentation in the `doc` directory about the ESPI
standard, mostly figured out from public sources and actual ESPI files.

Forked from the original repository [greenbutton-objects](https://github.com/asciipip/greenbutton-python)
and packaged to be published on PyPI.

Used by the Code for Boston [Home Energy Analysis Tool](https://github.com/codeforboston/home-energy-analysis-tool).

Dummy change do not merge


## Development
Simple steps for development setup:

1. Clone the git repository.
3. Navigate to any directory and create a [virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments) and activate it
4. The following commands can be run from inside the top-level greenbutton_objects folder while the virtual environment is active
5. `pip install -e .` installs the greenbutton_objects package into the virtual environment as an editable package. Meaning that any changes you make to the code will be reflected immediately without having to reinstall.
6. `pip install '.[dev]'` which installs the libraries required to develop greenbutton_objects.  Make sure to include single quotes around `[dev]` they are important.

Then, you should be able to run `pytest`, also from any directory, and see the test run successfully.

## Pre-commit Checks

This project uses [pre-commit](https://pre-commit.com/) to run various checks and formatters before each commit. To set it up:

1. Install pre-commit in your environment:
   ```
   pip install pre-commit
   ```

2. Install the pre-commit hooks:
   ```
   pre-commit install
   ```

Pre-commit checks will automatically run on every commit.
