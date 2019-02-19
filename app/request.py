from app import app
import urllib.request,json
from .models import source
from .models import newz
Source = source.Source
Newz = newz.Newz

# getting api key
api_key = app.config['NEWZ_API_KEY']
# getting the news base url

base_url = app.config['SOURCE_API_BASE_URL']
articles_base_url=app.config['NEWZ_API_BASE_URL']

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        source_results = get_source_response
        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_result(source_results_list)
    return source_results
def process_result(source_list):
    '''
    Function that processes the newz result and transform them to a list of objects
    
    Args:
       newz_list: A list of dictionaries that contain newz details
    Returns:
       newz_results:A list of objects
    '''
    source_results =[]
    for source_item in source_list:
       
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        if source:
            source_object = Source(id,name,description)
            source_results.append(source_object)
    return source_results

def get_newz(id):
    get_newz_details_url = articles_base_url.format(id,api_key)
    with urllib.request.urlopen(get_newz_details_url) as url:
        newz_details_data = url.read()
        newz_details_response = json.loads(newz_details_data)
        newz_object = None
        
        if newz_details_response['articles']:
                newz_results_list=newz_details_response['articles']
                newz_results=process_newz(newz_results_list)
    return newz_results
def process_newz(newz_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
    newz_list: A list of dictionaries that contain news details
    Returns :
    news_results: A list of articles objects
    '''
    newz_results=[]
    for article in newz_list:
        author=article.get('author')
        title=article.get('title')
        description=article.get('description')
        url=article.get('url')
        imageUrl=article.get('urlToImage')
        publishedAt=article.get("publishedAt")
        content=article.get('content')

        if imageUrl:
            article_object=Newz(author,title,description,url,imageUrl,publishedAt,content)
            newz_results.append(article_object)
    return newz_results 