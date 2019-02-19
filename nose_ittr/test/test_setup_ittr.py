__author__ = 'Sergey'

from nose.tools import ok_

from nose_ittr import IttrMultiplier, ittr


class TestSetupIttr(object, metaclass=IttrMultiplier):

    @ittr(param=['val_1', 'val_2'])
    def test_ittr_params_to_setup(self):
        ok_(hasattr(self, 'param'))
        ok_(self.param in ['val_1', 'val_2'])

    @ittr(param3=['a', 'b'], param2=['d', 'f', 'e'])
    def test_ittr_params_to_setup(self):
        ok_(self.param3 in ['a', 'b'])
        ok_(self.param2 in ['d', 'f', 'e'])

    @ittr(param2=['b', 'a'], param3=['d', 'f', 'e'], param4=['four'])
    def test_ittr_params_to_setup(self):
        ok_(self.param2 in ['b', 'a'])
        ok_(self.param3 in ['d', 'f', 'e'])
        ok_(self.param4 == 'four')
