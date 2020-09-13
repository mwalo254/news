import unittest
from .models import Top_headlines

class Top_headlines(unittest.TestCase):
    '''
    Top_headlines class that test the behaviour od the top headlines class
    '''
    
    def setUp(self):
        '''
        setup method that will run before every test
        '''
        self.new_headline = Top_headlines('author','title','description','url','urlToImage','publishedAt','content')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_headline,Top_headlines))