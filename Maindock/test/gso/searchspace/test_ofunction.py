"""Tests for ObjectiveFunction interface"""

from Maindock.gso.searchspace.ofunction import ObjectiveFunction
from nose.tools import raises


class TestObjectiveFunction:
    @raises(NotImplementedError)
    def test_call(self):
        function = ObjectiveFunction()
        function(coordinates=[])
