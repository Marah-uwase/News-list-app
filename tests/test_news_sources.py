import unittest
from app.models import News_sources

class NewsTest(unittest.TestCase):
    '''
    Test classs to test News_sources class
    '''
    def setUp(self):
        '''
        Runs before every Test
        '''
        self.new_source = News_sources ('bbc-sport','BBC Sport','The home of BBC Sport online',"http://www.bbc.co.uk/sport")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,News_sources))

    def test_init(self):
        '''
        Test to check initialization of variables
        '''
        self.assertEqual(self.new_source.id,"bbc-sport")
        self.assertEqual(self.new_source.name,"BBC Sport")
        self.assertEqual(self.new_source.description,"The home of BBC Sport online")
        self.assertEqual(self.new_source.url,"http://www.bbc.co.uk/sport")        
    