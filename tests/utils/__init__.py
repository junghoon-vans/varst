import argparse
from contextlib import contextmanager
from typing import Generator
from typing import Optional

import pytest


class ArgparseErrorWrapper:
    def __init__(self):
        self._error: Optional[argparse.ArgumentError] = None

    @property
    def error(self):
        assert self._error is not None
        return self._error

    @error.setter
    def error(self, value: object):
        assert isinstance(value, argparse.ArgumentError)
        self._error = value


@contextmanager
def argparse_error() -> Generator[ArgparseErrorWrapper, None, None]:
    wrapper = ArgparseErrorWrapper()

    with pytest.raises(SystemExit) as e:
        yield wrapper

    wrapper.error = e.value.__context__
