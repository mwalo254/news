import urllib.request,json
from .models import Sources, Everything, Top_Headlines
from config import DevConfig

# Getting the api key
api_key = None

# getting the source base url
base_url = None
headlines_url = None
everything_url = None
sources_url = None

def configure_request(app):
    global api_key,base_url,everything_url,headlines_url,sources_url

    api_key = app.config['NEWS_HIGHLIGHT_API_KEY']
    base_url = app.config['NEWS_HIGHLIGHT_API_BASE_URL']
    headlines_url = app.config['TOP_HEADLINES_URL']
    everything_url = app.config['EVERYTHING_URL_KEY']
    sources_url = app.config['SOURCES_URL_KEY']

def get_sources():
    '''
    function that gets json to respond to our url
    '''
    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources_results(sources_results_list)


    return sources_results

def process_sources_results(sources_list):
    '''
    Function that processes the source result and transforms a list of objects
    Args:
        source_list: a list of dictionaries that contain source details
    Returns:
        source_results: A list of source objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')
        name = sources_item.get('name')
        description = sources_item.get('description')

        sources_object = Sources(id,url,category,language,country,name,description)

    return sources_results

def get_top_headlines(sources) :
    get_top_headlines_url = headlines_url.format(sources, api_key)

    with urllib.request.urlopen(get_top_headlines_url) as url :
        top_headlines_data = url.read()
        top_headlines_response = json.loads(top_headlines_data)

        top_headlines_results = None 

        if top_headlines_response['top_headlines'] :
            top_headlines_results_list = top_headlines_response['top_headlines']
            top_headlines_results = process_top_headlines_results(top_headlines_results_list)

    return(top_headlines_results)

def process_top_headlines_results(top_headlines_results_list) :
    '''
    process Top_headlines results and transforms a list of objects
    '''
    top_headlines_results = []
    for top_headlines_item in top_headlines_results_list:

        author = top_headlines_item.get('author')
        title = top_headlines_item.get('title')
        description = top_headlines_item.get('description')
        url = top_headlines_item.get('url')
        urlToImage = top_headlines_item.get('urlToImage')
        publishedAt = top_headlines_item.get('publishedAt')
        content = top_headlines_item.get('content')

        top_headlines_object = Top_Headlines(author, title, description, url, urlToImage, publishedAt, content)
        top_headlines_results.append(top_headlines_object)

    return top_headlines_results

def get_everything() :
    '''
    get the json response to our url request 
    '''
    get_everything_url = everything_url.format(api_key)

    with urllib.request.urlopen(get_everything_url) as url :
        get_everything_data = url.read()
        get_everything_response = json.loads(get_everything_data)

        everything_results =  None 

        if get_everything_response['articles'] :
            everything_results_list = get_everything_response['articles']
            everything_results = process_everything_results(everything_results_list)

    return everything_results 

def process_everything_results(everything_results_list) :

    '''
    process everything result and transform them to a list of objects
    '''
    everything_results = []
    for everything_item in everything_results_list :
        
        author = everything_item.get('author')
        title = everything_item.get('title')
        description = everything_item.get('description')
        url = everything_item.get('url')
        urlToImage = everything_item.get('urlToImage')
        publishedAt = everything_item.get('publishedAt')
        content = everything_item.get('content')

        everything_object = Everything(author, title, description, url, urlToImage, publishedAt, content)
        everything_results.append(everything_object)

    return everything_results