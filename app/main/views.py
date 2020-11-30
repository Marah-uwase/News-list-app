from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news_source,articles
from ..models import News_sources

@main.route('/')
def index():
    '''
    Function that returns the index page & its data
    '''
    # Fetch Technology 
    technology_news = get_news_source('technology')

    # Fetch General
    general_news = get_news_source('general')

    #Fetch Sports
    sports_news = get_news_source('sports')

    #Fetch Business
    business_news = get_news_source('business')

    #Fetch Entertainment
    entertainment_news = get_news_source('entertainment')

    #Fetch Health
    health_news = get_news_source('health')

    #Title
    title = 'Home, Get todays News headlines'

    return render_template('index.html', title = title, tech = technology_news, general = general_news, sports = sports_news, business = business_news, entertainment = entertainment_news, health = health_news)

@main.route('/articles/<news_id>')
def news_articles(news_id):
    '''
    A function that will return news articles plus data
    '''
    news_articles_source = articles(news_id)
    return render_template('articles.html', id_name = news_id, articles = news_articles_source)

