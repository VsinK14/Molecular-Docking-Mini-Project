"""Tests for errors module"""

from Maindock.error.app_error import DockError, GSOError
from nose.tools import raises


class TestDockError:
    def test_create_exception(self):
        e = DockError("Testing")

        assert str(e) == "[DockError] Testing"

    @raises(DockError)
    def test_raising_exception(self):
        raise DockError("Testing")

    @raises(GSOError)
    def test_subclassing_base_exception(self):
        e = GSOError("Testing")

        assert str(e) == "[GSOError] Testing"
        raise e
