import urllib.request,json
from .models import News_sources,Articles


#Get API Key
api_key = None

#Getting the news base url
base_url = None

#Getting articles base url
articles_base_url = None

def configure_request(app):
    global api_key,base_url,articles_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_base_url = app.config['NEWS_SOURCES_BASE_URL']

def get_news_source(category):
    '''
    A Function that gets json response to our url request
    '''
    get_news_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_source_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)

        news_sources_results = None

        if get_news_source_response['sources']:
            news_sources_list = get_news_source_response['sources']
            news_sources_results = process_sources(news_sources_list)

    return news_sources_results

def process_sources(news_list):
    '''
    A function that will process news_list & transform them into a list of objects
    params:
        movie_list: A list of dictionaries that contain news details
    returns:
        news_results: A list of new objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')

        news_objects = News_sources(id,name,description,url)
        news_results.append(news_objects)

    return news_results

def articles(news_id):
    get_articles_url = articles_base_url.format(news_id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)

        articles_source_results = None
        if articles_response['articles']:        
            articles_source_results = process_articles(articles_response['articles'])
    return articles_source_results

def process_articles(articles_list):
    '''
    A Function to process & transfrom articles_list into a list of objects
    '''
    articles_results = []

    for article in articles_list:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')

        if urlToImage:
            articles_object = Articles(author,title,description,url,urlToImage,publishedAt)
            articles_results.append(articles_object)

    return articles_results


