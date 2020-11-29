import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test class to test Articles class
    '''
    def setUp(self):
        '''
        Runs before any Test
        '''
        self.new_article = Articles('author','test_title','test_desc','https://www.aljazeera.com/news/2019/04/sudan-police-16-killed-stray-bullets-protests-sit-ins-190413064228484.html','https://www.aljazeera.com/mritems/Images/2019/4/13/05d7b81751a14d8d9849c697f4b79416_18.jpg','2019-04-13T10:13:00Z')


    def test_init(self):
        '''
        Test to check initialization of variables
        '''   
        self.assertEqual(self.new_article.author,'author')
        self.assertEqual(self.new_article.title,'test_title')
        self.assertEqual(self.new_article.description,'test_desc')
        self.assertEqual(self.new_article.url,'https://www.aljazeera.com/news/2019/04/sudan-police-16-killed-stray-bullets-protests-sit-ins-190413064228484.html')
        self.assertEqual(self.new_article.urlToImage,'https://www.aljazeera.com/mritems/Images/2019/4/13/05d7b81751a14d8d9849c697f4b79416_18.jpg')
        self.assertEqual(self.new_article.publishedAt,'2019-04-13T10:13:00Z')
        