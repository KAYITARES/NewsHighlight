from app import app
import urllib.request,json
# getting api key
api_key = app.config['NEWZ_API_KEY']
# getting the movie base url
base_url = app.config["NEWZ_API_BASE_URL"]
def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        newz_results = get_news_response
        if get_news_response['results']:
            newz_results_list = get_news_response['results']
            newz_results = process_results(newz_results_list)
            return newz_results
def process_results(newz_list):
    '''
    Function that processes the newz result and transform them to a list of objects
    
    Args:
       newz_list: A list of dictionaries that contain newz details
    Returns:
       newz_results:A list of objects
    '''
    newz_results =[]
    for newz_item in newz_list:
        source = newz_item.get('name')
        author = newz_item.get('author')
        title = newz_item.get('title')
        description = newz_item.get('description')
        url = newz_item.get('url')
        urlToImage = newz_item.get('image')
        publishedAt = newz_item.get('published')
        content = newz_item.get('content')
        if source:
            newz_object = Newz(source,author,title,description,url,urlToImage,publishedAt,content)
            newz_results.append(newz_object)
    return newz_results
