import unittest
from .models import Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the source class
    '''
    def setUp(self):
        '''
        setup method that will run before every test
        '''
        self.new_source = Source(123,'name','description','url','category','english','Kenya')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))