import pathlib

import pytest

_ROOT_DIR = pathlib.Path(__file__).parent


@pytest.fixture()
def data_dir():
    return _ROOT_DIR / "data"
