__author__ = 'Sergey'

from nose.tools import ok_

from nose_ittr import IttrMultiplier, ittr


class TestSetupIttr(object, metaclass=IttrMultiplier):

    @ittr(param=['val_1', 'val_2'])
    def test_ittr_params_to_setup(self):
        ok_(hasattr(self, 'param'))
