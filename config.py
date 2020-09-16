import os

class Config:
    
    NEWS_API_SOURCES_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_API_KEY = 'dea57e8ead0d4b6fa8fe54a355df32f1'
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    NEWS_API_ARTICLES_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}